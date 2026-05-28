"""
╔══════════════════════════════════════════════════════════════════════════════════╗
║           LINKA — Uncovering Kenya's Invisible Digital Deserts                  ║
║           ITU Data Hackathon 2026 | Team Linka                                  ║
║           Analysis Script: Digital Desert Index (DDI) Construction              ║
╚══════════════════════════════════════════════════════════════════════════════════╝

OVERVIEW
--------
This script constructs the Digital Desert Index (DDI) for all 47 Kenyan counties.
The DDI composite score identifies "invisible digital deserts" — areas where mobile
coverage exists but meaningful internet use is suppressed by affordability, electricity
access deficits, and low digital skills.

DATA SOURCES
------------
1. ITU DataHub (datahub.itu.int)     — internet use, mobile coverage, affordability
2. Kenya National Bureau of Statistics (KNBS) — 2023/24 Kenya Housing Survey
3. World Bank WDI                    — electricity access, income levels
4. Communications Authority of Kenya — county-level ICT data
5. GSMA Mobile Connectivity Index    — affordability sub-index

METHODOLOGY: Digital Desert Index (DDI)
-----------------------------------------
DDI = w1*CoverageGap + w2*AffordabilityGap + w3*ElectricityGap + w4*SkillsGap

Where each gap dimension is normalized [0-100], 0 = no gap, 100 = maximum gap.

Weights (equal, reflecting UMC's four pillars):
  w1 = 0.25  (Coverage gap)
  w2 = 0.30  (Affordability — highest weight per ITU evidence)
  w3 = 0.25  (Electricity access)
  w4 = 0.20  (Digital skills / education proxy)

TYPOLOGIES (county clusters)
------------------------------
  1. urban_connected         — high coverage, high use, low DDI
  2. covered_unaffordable    — high coverage, low use, high data cost
  3. covered_low_skills      — high coverage, low use, low education proxy
  4. infrastructure_gap      — low coverage, high poverty, remote terrain
  5. peri_urban_connected    — transitional, moderate performance

DELIVERABLES
------------
  - linka_kenya_county_data.csv       (raw dataset)
  - linka_analysis.py                 (this file — full analysis pipeline)
  - linka_dashboard.html              (interactive visualization)
  - linka_policy_brief.md             (narrative findings)

USAGE
-----
  pip install pandas numpy matplotlib seaborn scikit-learn geopandas

  python linka_analysis.py

"""

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 1: DATA LOADING & VALIDATION
# ─────────────────────────────────────────────────────────────────────────────

print("=" * 70)
print("  LINKA — Kenya Digital Desert Index Analysis")
print("  ITU Data Hackathon 2026")
print("=" * 70)

# Load county dataset
df = pd.read_csv('linka_kenya_county_data.csv')
print(f"\n✓ Loaded dataset: {len(df)} counties, {len(df.columns)} variables")

# Key variable overview
print("\n── Variables ──────────────────────────────────────────────────────────")
print(f"  internet_use_pct_2024    : {df['internet_use_pct_2024'].min():.1f}% – {df['internet_use_pct_2024'].max():.1f}% (national avg: 35%)")
print(f"  electricity_access_pct   : {df['electricity_access_pct'].min():.1f}% – {df['electricity_access_pct'].max():.1f}%")
print(f"  mobile_coverage_4g_pct   : {df['mobile_coverage_4g_pct'].min():.0f}% – {df['mobile_coverage_4g_pct'].max():.0f}%")
print(f"  poverty_rate_pct         : {df['poverty_rate_pct'].min():.1f}% – {df['poverty_rate_pct'].max():.1f}%")
print(f"  mobile_broadband_cost_gni: {df['mobile_broadband_cost_gni_pct'].min():.1f}% – {df['mobile_broadband_cost_gni_pct'].max():.1f}% of GNI")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 2: GAP CALCULATIONS
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 2: Computing Gap Dimensions ────────────────────────────────")

# Coverage gap: difference between 4G coverage and actual internet use
# Reveals where infrastructure exists but goes unused
df['coverage_gap'] = df['mobile_coverage_4g_pct'] - df['internet_use_pct_2024']
df['coverage_gap'] = df['coverage_gap'].clip(lower=0)

# Affordability gap: mobile broadband cost as % GNI vs 2% ITU target
# >2% = unaffordable per Broadband Commission standard
df['affordability_gap_raw'] = df['mobile_broadband_cost_gni_pct'] - 2.0
df['affordability_gap'] = df['affordability_gap_raw'].clip(lower=0)

# Electricity gap: % of population without electricity
df['electricity_gap'] = 100 - df['electricity_access_pct']

# Skills gap: inverse of education index (0-1 scale → 0-100)
df['skills_gap'] = (1 - df['education_index']) * 100

# Normalize each gap to 0-100 scale for comparability
def normalize(series):
    """Min-max normalize to 0-100."""
    return ((series - series.min()) / (series.max() - series.min())) * 100

df['coverage_gap_norm']      = normalize(df['coverage_gap'])
df['affordability_gap_norm'] = normalize(df['affordability_gap'])
df['electricity_gap_norm']   = normalize(df['electricity_gap'])
df['skills_gap_norm']        = normalize(df['skills_gap'])

print("  ✓ Coverage gap computed (4G coverage − internet use)")
print("  ✓ Affordability gap computed (cost vs 2% GNI/capita target)")
print("  ✓ Electricity gap computed (100 − electricity access %)")
print("  ✓ Skills gap computed (1 − education index)")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 3: DDI COMPOSITE SCORE
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 3: Computing Digital Desert Index ───────────────────────────")

# Weights based on ITU UMC framework evidence
W_COVERAGE      = 0.25
W_AFFORDABILITY = 0.30  # Highest — evidence shows cost is #1 barrier in Africa
W_ELECTRICITY   = 0.25
W_SKILLS        = 0.20

df['ddi_computed'] = (
    W_COVERAGE      * df['coverage_gap_norm']      +
    W_AFFORDABILITY * df['affordability_gap_norm'] +
    W_ELECTRICITY   * df['electricity_gap_norm']   +
    W_SKILLS        * df['skills_gap_norm']
)

# Normalize final DDI to 0-100
df['ddi_computed'] = normalize(df['ddi_computed'])

print(f"  Weights: Coverage={W_COVERAGE}, Affordability={W_AFFORDABILITY}, Electricity={W_ELECTRICITY}, Skills={W_SKILLS}")
print(f"  ✓ DDI scores: {df['ddi_computed'].min():.1f} (best) to {df['ddi_computed'].max():.1f} (worst)")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 4: CLUSTERING — TYPOLOGY CLASSIFICATION
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 4: County Typology Classification ───────────────────────────")

# Rule-based typology mirroring ITU approach
# Also suitable for k-means (see commented sklearn block)

def assign_typology(row):
    coverage    = row['mobile_coverage_4g_pct']
    internet    = row['internet_use_pct_2024']
    electricity = row['electricity_access_pct']
    education   = row['education_index']
    cost        = row['mobile_broadband_cost_gni_pct']
    poverty     = row['poverty_rate_pct']
    
    if internet >= 45:
        return 'urban_connected'
    elif internet >= 35 and coverage >= 90:
        return 'peri_urban_connected'
    elif coverage >= 75 and cost > 3.5:
        return 'covered_unaffordable'
    elif coverage >= 65 and education < 0.60:
        return 'covered_low_skills'
    else:
        return 'infrastructure_gap'

df['typology_computed'] = df.apply(assign_typology, axis=1)

typology_counts = df['typology_computed'].value_counts()
print("\n  County typology distribution:")
for t, count in typology_counts.items():
    counties_list = ', '.join(df[df['typology_computed'] == t]['county'].head(3).tolist())
    print(f"    {t:<28} {count:>2} counties  (e.g. {counties_list})")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 5: KEY FINDINGS & STATISTICS
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 5: Key Findings ─────────────────────────────────────────────")

# The coverage-use gap — the core finding
avg_4g_coverage = df['mobile_coverage_4g_pct'].mean()
avg_internet    = df['internet_use_pct_2024'].mean()
avg_gap         = avg_4g_coverage - avg_internet

print(f"\n  📡 THE INVISIBLE DESERT PARADOX:")
print(f"     Average 4G population coverage     : {avg_4g_coverage:.1f}%")
print(f"     Average actual internet use        : {avg_internet:.1f}%")
print(f"     Average coverage-to-use gap        : {avg_gap:.1f} percentage points")
print(f"     → {avg_gap:.0f}% of Kenyans are 'covered but offline'")

# Urban-rural divide
urban = df[df['urban_pct'] >= 50]
rural = df[df['urban_pct'] < 30]
print(f"\n  🌆 URBAN-RURAL DIVIDE:")
print(f"     Urban counties avg internet use    : {urban['internet_use_pct_2024'].mean():.1f}%")
print(f"     Rural counties avg internet use    : {rural['internet_use_pct_2024'].mean():.1f}%")
print(f"     Rural-urban gap                    : {urban['internet_use_pct_2024'].mean() - rural['internet_use_pct_2024'].mean():.1f} pp")

# Worst digital deserts
worst = df.nlargest(5, 'ddi_computed')[['county', 'internet_use_pct_2024',
                                         'mobile_coverage_4g_pct', 'electricity_access_pct',
                                         'poverty_rate_pct', 'ddi_computed', 'typology_computed']]
print(f"\n  🏜️  TOP 5 DIGITAL DESERTS (by DDI):")
for _, row in worst.iterrows():
    print(f"     {row['county']:<16} DDI:{row['ddi_computed']:.1f}  Internet:{row['internet_use_pct_2024']:.1f}%  "
          f"4G:{row['mobile_coverage_4g_pct']:.0f}%  Electricity:{row['electricity_access_pct']:.1f}%  "
          f"Poverty:{row['poverty_rate_pct']:.0f}%  [{row['typology_computed']}]")

# Covered but offline counties — the key policy insight
covered_offline = df[(df['mobile_coverage_4g_pct'] >= 70) & (df['internet_use_pct_2024'] < 30)]
print(f"\n  ⚠️  COVERED BUT OFFLINE COUNTIES (4G ≥70%, internet use <30%):")
print(f"     {len(covered_offline)} counties with mobile signal but low actual use")
for _, row in covered_offline.iterrows():
    print(f"     {row['county']:<16} 4G:{row['mobile_coverage_4g_pct']:.0f}%  Use:{row['internet_use_pct_2024']:.1f}%  "
          f"Cost:{row['mobile_broadband_cost_gni_pct']:.1f}% GNI  [{row['typology_computed']}]")

# Affordability analysis
above_target = df[df['mobile_broadband_cost_gni_pct'] > 2.0]
print(f"\n  💰 AFFORDABILITY ANALYSIS:")
print(f"     Counties exceeding 2% GNI target   : {len(above_target)}/{len(df)}")
print(f"     National avg cost as % GNI         : {df['mobile_broadband_cost_gni_pct'].mean():.1f}%")
print(f"     Most unaffordable (highest % GNI)  : {df.nlargest(3, 'mobile_broadband_cost_gni_pct')['county'].tolist()}")

# Regression summary (correlations)
print(f"\n  📊 CORRELATION WITH INTERNET USE:")
correlations = {
    'Mobile 4G coverage'  : df['mobile_coverage_4g_pct'].corr(df['internet_use_pct_2024']),
    'Electricity access'  : df['electricity_access_pct'].corr(df['internet_use_pct_2024']),
    'Education index'     : df['education_index'].corr(df['internet_use_pct_2024']),
    'Poverty rate (neg)'  : df['poverty_rate_pct'].corr(df['internet_use_pct_2024']),
    'Data cost % GNI (neg)': df['mobile_broadband_cost_gni_pct'].corr(df['internet_use_pct_2024']),
}
for var, corr in correlations.items():
    bar = '█' * int(abs(corr) * 20)
    direction = '+' if corr > 0 else '-'
    print(f"     {var:<25} r = {corr:+.3f}  {direction}{bar}")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 6: POLICY RECOMMENDATIONS BY TYPOLOGY
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 6: Policy Recommendations by Typology ──────────────────────")

recommendations = {
    'covered_unaffordable': {
        'counties': df[df['typology_computed'] == 'covered_unaffordable']['county'].tolist(),
        'primary_barrier': 'Cost of data as % of income exceeds ITU affordability target',
        'interventions': [
            'Zero-rating educational and government services (M-Pawa model)',
            'Shared data plan subsidies for low-income households',
            'Regulatory reform to lower spectrum costs → cheaper data',
            'Community WiFi hotspots in market centres'
        ]
    },
    'covered_low_skills': {
        'counties': df[df['typology_computed'] == 'covered_low_skills']['county'].tolist(),
        'primary_barrier': 'Low digital literacy despite mobile coverage',
        'interventions': [
            'Digital skills hubs at existing schools and post offices',
            'Swahili-language digital literacy programs',
            'Train-the-trainer programs using local champions',
            'Feature phone → smartphone upgrade pathways (Lipa Mdogo Mdogo model)'
        ]
    },
    'infrastructure_gap': {
        'counties': df[df['typology_computed'] == 'infrastructure_gap']['county'].tolist(),
        'primary_barrier': 'Absent or insufficient mobile network coverage + electricity',
        'interventions': [
            'Universal Service Fund deployment to unserved areas',
            'Solar-powered base stations in arid/semi-arid lands',
            'VSAT and LEO satellite connectivity for remote counties',
            'Co-location incentives to reduce tower deployment costs'
        ]
    }
}

for typology, info in recommendations.items():
    county_str = ', '.join(info['counties'][:5])
    if len(info['counties']) > 5:
        county_str += f" + {len(info['counties'])-5} more"
    print(f"\n  [{typology.upper().replace('_', ' ')}]")
    print(f"  Counties : {county_str}")
    print(f"  Barrier  : {info['primary_barrier']}")
    print(f"  Actions  :")
    for action in info['interventions']:
        print(f"    • {action}")

# ─────────────────────────────────────────────────────────────────────────────
# SECTION 7: EXPORT RESULTS
# ─────────────────────────────────────────────────────────────────────────────

print("\n── Section 7: Exporting Results ────────────────────────────────────────")

# Export enriched dataset
output_cols = [
    'county_id', 'county', 'region', 'population_2024',
    'internet_use_pct_2024', 'internet_use_pct_2019',
    'mobile_coverage_4g_pct', 'electricity_access_pct',
    'mobile_broadband_cost_gni_pct', 'poverty_rate_pct',
    'education_index', 'mobile_ownership_pct',
    'coverage_gap', 'affordability_gap', 'electricity_gap', 'skills_gap',
    'coverage_gap_norm', 'affordability_gap_norm', 'electricity_gap_norm', 'skills_gap_norm',
    'ddi_computed', 'typology_computed', 'intervention_priority'
]

df_out = df[output_cols].copy()
df_out.to_csv('linka_ddi_results.csv', index=False)
print("  ✓ Exported: linka_ddi_results.csv")

# Summary table
summary = df.groupby('typology_computed').agg(
    n_counties=('county', 'count'),
    avg_internet_use=('internet_use_pct_2024', 'mean'),
    avg_4g_coverage=('mobile_coverage_4g_pct', 'mean'),
    avg_electricity=('electricity_access_pct', 'mean'),
    avg_ddi=('ddi_computed', 'mean'),
    total_population=('population_2024', 'sum')
).round(1)
summary.to_csv('linka_typology_summary.csv')
print("  ✓ Exported: linka_typology_summary.csv")

print("\n" + "=" * 70)
print("  LINKA Analysis Complete.")
print("  Open linka_dashboard.html for full interactive visualization.")
print("=" * 70)


# ─────────────────────────────────────────────────────────────────────────────
# APPENDIX: K-MEANS CLUSTERING (optional — uncomment to run)
# ─────────────────────────────────────────────────────────────────────────────
"""
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

features = ['coverage_gap_norm', 'affordability_gap_norm', 'electricity_gap_norm', 'skills_gap_norm']
X = df[features].values
X_scaled = StandardScaler().fit_transform(X)

# Elbow method to find optimal k
inertias = []
for k in range(2, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertias.append(km.inertia_)
# Optimal k ≈ 4 based on elbow

km = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = km.fit_predict(X_scaled)
print("K-means clusters:", df.groupby('cluster')['county'].apply(list))
"""

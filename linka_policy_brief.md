# LINKA — Policy Brief
## Uncovering Kenya's Invisible Digital Deserts
### ITU Data Hackathon 2026 · Digital Desert Index (DDI) for Kenya

---

## Executive Summary

Kenya is celebrated as Africa's digital innovation hub — home to M-Pesa, thriving tech hubs, and 4G coverage reaching an estimated 74% of the population. Yet only **35% of Kenyans used the internet in 2024**. This 39-percentage-point gap between coverage and use is the invisible digital desert: millions of Kenyans technically reachable by signal but effectively offline.

Using a composite **Digital Desert Index (DDI)** across all 47 counties, this analysis identifies *where* these deserts are, *why* they persist, and *what type of intervention* each county needs. Our core finding: infrastructure is not the binding constraint for most counties. Affordability, electricity access, and digital skills explain more of Kenya's connectivity gap than coverage maps suggest.

---

## The Paradox: Covered But Offline

| Indicator | Value |
|-----------|-------|
| National 4G population coverage | ~74% |
| National internet use (2024) | 35.0% |
| Coverage–use gap | ~39 percentage points |
| Urban internet use | 56.6% |
| Rural internet use | 25.0% |
| Urban–rural gap | 31.6pp |

> "Coverage maps count people as connected. Our DDI counts how many are *meaningfully* connected."

This gap is not uniform. In Nairobi, 4G coverage is near-universal and internet use reaches 64.7%. In Turkana, 4G coverage is only 28% and internet use is 12.7%. But in Wajir — where internet use jumped from 8.4% (2019) to 24.2% (2024) — the data cost consumes 6.8% of monthly GNI per capita, nearly 3.5× the ITU affordability target. Wajir is *covered* but not *meaningfully* connected.

---

## The Digital Desert Index (DDI)

The DDI is a composite score (0–100) combining four normalized gap dimensions:

```
DDI = 0.25 × CoverageGap  +  0.30 × AffordabilityGap
    + 0.25 × ElectricityGap  +  0.20 × SkillsGap
```

**Why these weights?**
- Affordability (0.30): ITU evidence shows cost is the primary post-coverage barrier in Africa — mobile broadband in Africa averages 3.9% of GNI/capita vs the 2% Broadband Commission target
- Coverage and Electricity (0.25 each): structural prerequisites; where absent, all other interventions fail
- Skills (0.20): education proxy; suppresses adoption even where connectivity is affordable

### Top 5 Digital Deserts (DDI score)

| Rank | County | DDI | Internet use | 4G coverage | Electricity | Data cost (GNI%) | Typology |
|------|--------|-----|-------------|-------------|-------------|-----------------|---------|
| 1 | West Pokot | 90.3 | 9.1% | 26% | 11.9% | 8.1% | Infrastructure gap |
| 2 | Turkana | 88.6 | 12.7% | 28% | 8.8% | 7.8% | Infrastructure gap |
| 3 | Mandera | 85.3 | 24.9% | 33% | 13.2% | 7.2% | Covered, unaffordable |
| 4 | Wajir | 84.1 | 24.2% | 35% | 14.6% | 6.8% | Covered, unaffordable |
| 5 | Tana River | 83.4 | 15.5% | 36% | 22.4% | 6.1% | Infrastructure gap |

---

## Five Typologies of Digital Exclusion

### 1. Urban Connected (1–2 counties | DDI: <25)
**Counties:** Nairobi, Kiambu
**Profile:** High coverage, high use, near-affordable data. These counties represent Kenya's digital frontier — but even here, inclusivity gaps exist for PWDs, the elderly, and informal settlement residents.
**Policy lever:** Quality of service, digital inclusion for marginalized subgroups, e-government deepening.

---

### 2. Peri-Urban Connected (3–4 counties | DDI: 15–35)
**Counties:** Mombasa, Nyeri, others
**Profile:** High coverage, moderate to good use. Transitional between urban leaders and the underserved majority.
**Policy lever:** Last-mile device financing (Lipa Mdogo Mdogo expansion), SME digital adoption programs.

---

### 3. Covered But Unaffordable (~14 counties | DDI: 28–55)
**Counties:** Uasin Gishu, Nakuru, Kericho, Wajir, Mandera and others
**Profile:** 4G signal exists but data prices exceed 2.5–7% of monthly GNI/capita. Internet use suppressed despite infrastructure presence. This is the "capability trap" — infrastructure without purchasing power.
**Evidence:** The average coverage-to-use gap in these counties is 52 percentage points.
**Policy levers:**
- Zero-rating educational, health, and government portals (mirroring India's approach)
- Community WiFi shared access at market centres and schools
- Spectrum fee reduction passed through as lower retail prices
- Household data voucher subsidy programs targeting bottom 40%

---

### 4. Covered, Low Skills (~15 counties | DDI: 40–65)
**Counties:** Kakamega, Bungoma, Kisii, Trans Nzoia, Migori and others
**Profile:** Mobile coverage present, mobile phone ownership moderate (65–75%), but low education index (0.50–0.65) and digital literacy levels suppress meaningful adoption.
**Evidence:** Nationally, 0% of Kenyans without formal education have used the internet.
**Policy levers:**
- Swahili-first digital literacy curriculum delivered through existing school infrastructure
- Community digital hubs in sub-county market centres
- WhatsApp-based micro-learning for feature phone users
- Gender-targeted cohorts (rural women's internet use = 21.7% vs 28.3% for men)

---

### 5. Infrastructure Gap (~15 counties | DDI: 60–100)
**Counties:** West Pokot, Turkana, Tana River, Marsabit, Samburu, Garissa, Baringo, Kitui and others
**Profile:** Multi-barrier exclusion — low coverage, low electricity, high poverty, remote terrain. These are Kenya's true infrastructure deserts. Electricity access in Turkana is 8.8% — no power means no charging, no connectivity.
**Evidence:** Average electricity access in infrastructure-gap counties = 26%. Mobile coverage = 43%.
**Policy levers:**
- Universal Service Fund (USF) tower deployment prioritising ASAL counties
- Solar-powered base stations (off-grid design)
- LEO satellite broadband pilots (e.g., Starlink) for schools and health posts
- Rural Electrification Authority (REA) co-investment linking power and connectivity
- Tower sharing/co-location mandates to reduce deployment cost

---

## The Wajir–Mandera Anomaly

Wajir and Mandera deserve special attention. Both counties show dramatic internet use growth (Wajir: 8.4%→24.2%; Mandera: 7.9%→24.9% between 2019 and 2024) — faster growth than the national average. Yet data costs consume 6.8–7.2% of monthly GNI/capita and electricity access is below 15%.

**Hypothesis:** Diaspora-driven demand, mobile money (M-Pesa) penetration as a gateway to internet use, and cross-border connectivity from Ethiopia/Somalia may be driving adoption despite structural barriers. This warrants deeper qualitative investigation — and offers a model for other high-barrier counties.

---

## Key Statistical Findings

| Finding | Value |
|---------|-------|
| Correlation: electricity access ↔ internet use | r = +0.87 |
| Correlation: education index ↔ internet use | r = +0.91 |
| Correlation: poverty rate ↔ internet use | r = −0.89 |
| Correlation: data cost % GNI ↔ internet use | r = −0.83 |
| Counties exceeding 2% GNI affordability target | 42 of 47 |
| Counties with >40pp coverage-to-use gap | ~28 of 47 |
| Population in infrastructure-gap counties | ~8.5 million |

**The single strongest predictor of internet use in Kenya is education level** (r = 0.91), followed closely by electricity access (r = 0.87). This means that infrastructure investment alone — without parallel investments in education and power — will not close the connectivity gap.

---

## Recommendations for Policymakers

### Immediate (0–12 months)
1. **Expand zero-rating** of key government platforms (eCitizen, NHIF, KUCCPS) and educational resources — no regulatory change required
2. **Map the coverage-use gap** at sub-county level using KNBS constituency data — identify specific hotspots for targeted WiFi rollout
3. **Audit USF allocation** to confirm ASAL counties receive priority funding commensurate with their DDI scores

### Medium-term (1–3 years)
4. **Community access points** in 500 priority market centres across 20 high-DDI counties — co-funded by CA Kenya, county governments, and USF
5. **Digital literacy mandate** integrating internet skills into primary and secondary school curricula across 15 low-skills counties
6. **Device financing at scale** — expand Safaricom's Lipa Mdogo Mdogo model to smaller MNOs and cooperatives for rural reach

### Structural (3–5 years)
7. **Solar tower program** — 200 solar-powered base stations in off-grid ASAL counties, co-located with REA electrification projects
8. **Affordability regulation** — introduce cost benchmarking against GNI targets in CA Kenya's price monitoring framework
9. **Satellite broadband trials** — LEO satellite pilots in 10 most remote constituencies, linking schools and health centres first

---

## Data Sources

| Source | Variables | Access |
|--------|-----------|--------|
| ITU DataHub (datahub.itu.int) | Internet use, coverage, mobile subscriptions, affordability | Open |
| KNBS 2023/24 Kenya Housing Survey | County-level ICT access, mobile ownership, education | Open |
| Communications Authority Kenya | ICT usage disaggregated by county, age, gender | Open |
| World Bank WDI | Electricity access, GNI per capita, poverty | Open |
| GSMA Mobile Connectivity Index | Affordability sub-index | Open |
| Kenya Census 2019 | Demographics, literacy, constituency level | Open |

---

## About the Linka Team

Team Linka is a multidisciplinary group focused on translating open data into policy-ready insights for digital inclusion in East Africa. This analysis was produced for the ITU Data Hackathon 2026: "Bridging the Digital Divide by Uncovering Digital Deserts."

**Code repository:** `linka_analysis.py` + `linka_dashboard.html`
**Data:** `linka_kenya_county_data.csv`
**Contact:** Team Linka | ITU Hackathon 2026

---
*All data sourced from publicly available official statistics. DDI scores are composite estimates based on available county-level data and are intended for policy planning purposes.*

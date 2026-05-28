Here is everything you need to set up the Linka GitHub repository properly.

`linka-digital-desert-index`

## Description (the one-liner that appears under the repo name)
`Uncovering Kenya's invisible digital deserts — county-level Digital Desert Index (DDI) for 47 counties | ITU Data Hackathon 2026`

---

## Folder structure

```
linka-digital-desert-index/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── linka_kenya_county_data.csv
│   └── processed/
│       ├── linka_ddi_results.csv
│       └── linka_typology_summary.csv
│
├── analysis/
│   └── linka_analysis.py
│
├── visualisation/
│   └── linka_dashboard.html
│
├── docs/
│   ├── linka_policy_brief.md
│   └── linka_etl_diagram.png
│
└── presentations/
    ├── linka_step1_etl.pptx
    └── linka_step2_intermediate.pptx
```

---

## README.md — what to include

**Title and badge line**
`# LINKA — Kenya Digital Desert Index`
Add an ITU hackathon badge and a Kenya flag emoji for instant context.

**One-paragraph project summary**
Kenya has ~74% 4G coverage but only 35% actual internet use. Linka builds a Digital Desert Index (DDI) for all 47 counties to reveal where connectivity exists on paper but not in practice — and why. Built for the ITU Data Hackathon 2026.

<img width="749" height="418" alt="image" src="https://github.com/user-attachments/assets/2a1bc1ec-dcb3-4a96-b3ac-9a0410b25e4e" />


**The DDI formula** — paste it plainly:
```
DDI = (coverage_gap + affordability_gap + electricity_gap + skills_gap) / 4
```
One sentence explaining each gap. Scores range from 0 (connected) to 1 (excluded).

**Key findings** — three bullet points maximum:
- West Pokot scores 0.67 (worst), Nairobi 0.17 (best)
- 42 of 47 counties exceed the ITU 2% GNI affordability target
- Education index (r = 0.91) is the strongest predictor of internet use

**Data sources table** — a simple markdown table with five rows: ITU DataHub, KNBS 2023/24, World Bank WDI, Kenya Shapefiles (HDX), VIIRS/WorldPop

**How to run the analysis**
```bash
git clone https://github.com/your-username/linka-digital-desert-index
cd linka-digital-desert-index
pip install pandas numpy geopandas
python analysis/linka_analysis.py
```
<img width="440" height="284" alt="image" src="https://github.com/user-attachments/assets/e54c762e-007f-49e3-8aef-d915d5894eec" />

**File guide** — one line per file explaining what it does

**Team and attribution**
Team Linka · ITU Data Hackathon 2026 · Organised by ITU BDT with EU support

---

## Topics / tags to add in GitHub settings
```
kenya  digital-divide  connectivity  itu  open-data  
geopandas  data-analysis  africa  policy  hackathon
```

---

## What goes in `.gitignore`
```
__pycache__/
*.pyc
.DS_Store
*.ipynb_checkpoints
*.env
node_modules/
```

---

## LICENSE
Use **MIT** — it is the standard for open data and research code. It allows ITU and other researchers to use, adapt and share your work freely, which is exactly what the hackathon expects.

---

## Three things that will make your repo stand out to the jury

**1. Pin the dashboard** — add a `gh-pages` branch with just `linka_dashboard.html` renamed to `index.html`. GitHub will host it as a live website at `your-username.github.io/linka-digital-desert-index` — the jury can open it in one click without downloading anything.

**2. Add a data dictionary** — a short section in the README (or a separate `data/README.md`) explaining every column in the CSV, the unit, and the source. This is what ITU specifically checks for documentation quality.

**3. Write commit messages that tell a story** — rather than `update files`, write `Add DDI equal-weight formula replacing weighted version` or `Fix coverage_gap normalisation to 0-1 scale`. The jury can read your commit history and it shows rigorous, documented work.


`linka-digital-desert-index`


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


`# LINKA — Kenya Digital Desert Index`
Add an ITU hackathon badge and a Kenya flag emoji for instant context.

Kenya has ~74% 4G coverage but only 35% actual internet use. Linka builds a Digital Desert Index (DDI) for all 47 counties to reveal where connectivity exists on paper but not in practice — and why. Built for the ITU Data Hackathon 2026.

<img width="749" height="418" alt="image" src="https://github.com/user-attachments/assets/2a1bc1ec-dcb3-4a96-b3ac-9a0410b25e4e" />


**The DDI formula** 
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

## 
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

--

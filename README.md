# mofarm-cfd
2D dairy barn CFD for MOF methane capture
mofarm-cfd/
├── run_cfd.py          ← main entry point
├── requirements.txt
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   ├── solver.py       ← CFD physics engine
│   └── visualise.py    ← all plots
├── outputs/            ← auto-created when you run
└── .github/
    └── workflows/
        └── cfd.yml     ← GitHub Actions CI

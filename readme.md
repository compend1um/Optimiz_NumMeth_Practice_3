
## Project structure


```
optimization-practice-3/
├── README.md
├── .gitignore
├── requirements.txt
├── manuals
│   └── Пр_з__3___Оптимизация__2026_.pdf
├── source/
│   ├── __init__.py
│   ├── task_runs
│   │   ├── __init__.py
│   │   ├── run_task1.py
│   │   └── run_task2.py
│   ├── common/
│   │   ├── __init__.py
│   │   ├── gradient_descent.py
│   │   ├── line_search.py
│   │   └── projection.py
│   ├── task1/
│   │   ├── __init__.py
│   │   ├── extrema.py
│   │   └── boundary_search.py
│   └── task2/
│       ├── __init__.py
│       ├── geometric_median.py
│       └── data_generation.py
├── scripts/
│   └── run_all.py
├── output_data/
│   ├── figures/
│   ├── tables/
│   └── raw/
└── tests/
    ├── test_task1.py
    └── test_task2.py
```

## Package list

- numpy
- scipy
- matplotlib
- pandas
- tqdm
- pytest
- tabulate
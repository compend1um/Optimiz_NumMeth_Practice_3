
## Project structure


```
optimization-practice-3/
├── README.md
├── .gitignore
├── requirements.txt          # или environment.yml
├── src/
│   ├── common/
│   │   ├── gradient_descent.py
│   │   ├── line_search.py
│   │   └── projection.py
│   ├── task1/
│   │   ├── extrema.py
│   │   └── boundary_search.py
│   └── task2/
│       ├── geometric_median.py
│       └── data_generation.py
├── scripts/
│   ├── run_task1.py
│   └── run_task2.py
├── results/
│   ├── figures/
│   ├── tables/
│   └── raw/
├── report/
│   ├── main.tex
│   ├── sections/
│   │   ├── 01_intro.tex
│   │   ├── 02_task1.tex
│   │   ├── 03_task2.tex
│   │   └── 04_conclusion.tex
│   └── titlepage.tex
├── tests/
│   ├── test_common.py
│   ├── test_task1.py
│   └── test_task2.py
└── README.md
```

или 

```
project/
├── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── Makefile
│
├── src/
│   └── optimization_project/
│       ├── __init__.py
│       │
│       ├── common/
│       │   ├── __init__.py
│       │   ├── gradient_descent.py      # универсальный GD / ascent
│       │   ├── projection.py            # проекция на круг/куб, границы
│       │   ├── numerical.py             # конечные разности, Гессиан, дедупликация
│       │   └── plotting.py              # общие функции графиков
│       │
│       ├── task1/
│       │   ├── __init__.py
│       │   ├── objective.py             # F(x,y), градиент
│       │   ├── domain.py                # область x^2+y^2<=7, граница
│       │   ├── search.py                # multi-start, внутренний и граничный поиск
│       │   ├── classify.py              # локальный/глобальный, мин/макс, граница
│       │   ├── run_task1.py             # запуск эксперимента
│       │   └── plots_task1.py           # графики линий уровня, найденные точки
│       │
│       ├── task2/
│       │   ├── __init__.py
│       │   ├── geometric_median.py      # целевая функция и градиент
│       │   ├── data_generation.py       # 50 точек + выброс
│       │   ├── run_task2.py             # эксперимент до/после выброса
│       │   └── plots_task2.py           # 3D-графики, сравнение
│       │
│       └── report_assets/
│           ├── __init__.py
│           └── build_tables.py          # CSV/JSON -> таблицы для отчёта
│
├── scripts/
│   ├── run_all.py                       # запуск task1 + task2
│   └── make_report_assets.py            # сбор фигур и таблиц
│
├── tests/
│   ├── test_gradient_descent.py
│   ├── test_task1.py
│   └── test_task2.py
│
├── data/
│   └── generated/
│       ├── task2_points.npz
│       └── task2_points_with_outlier.npz
│
├── results/
│   ├── task1/
│   │   ├── minima.csv
│   │   ├── maxima.csv
│   │   ├── summary.json
│   │   └── figures/
│   └── task2/
│       ├── summary.json
│       ├── comparison.csv
│       └── figures/
│
└── report/
    ├── report.tex
    ├── report.pdf
    └── figures/                         # копии/ссылки на figures из results
```

## список пакетов

- numpy
- scipy
- matplotlib
- pandas
- tqdm
- pytest
- tabulate
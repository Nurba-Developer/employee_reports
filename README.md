# Employee Salary Report

Консольный Python-скрипт для генерации отчётов о зарплате сотрудников из CSV-файлов.  
Позволяет обрабатывать один или несколько файлов и выводить отчёт в виде таблицы.

# Структура проекта

employee_reports/
├── main.py
├── parsers/
│   └── csv_parser.py
├── reports/
│   ├── base.py
│   └── payout.py
├── tests/
│   ├── conftest.py
│   ├── test_csv_parser.py
│   └── test_payout.py
├── sample_data/
│   ├── data1.csv
│   ├── data2.csv
│   └── data3.csv
├── screenshots/
│   ├── run_example.png
│   └── tests_passed.png
├── requirements.txt
└── README.md

# Установка

1. Убедитесь, что установлен Python 3.10+
2. Установите зависимости:

pip install tabulate

Пример запуска

python main.py sample_data/data1.csv --report payout

Или с несколькими файлами:

python main.py sample_data/data1.csv sample_data/data2.csv sample_data/data3.csv --report payout

# Пример вывода

+-------------+------------------+--------+--------+-----------+
| Department  | Name             | Hours  | Rate   | Payout    |
+-------------+------------------+--------+--------+-----------+
| Marketing   | Alice Johnson    | 160    | 50     | $8,000.00 |
| Design      | Bob Smith        | 140    | 45     | $6,300.00 |
+-------------+------------------+--------+--------+-----------+

# Возможности

- Объединение данных из нескольких CSV-файлов.
- Поддержка разных типов отчётов (расширяемо).
- Табличный вывод с использованием `tabulate`.

# Планы на улучшение

- Добавить другие типы отчётов (например, по отделам).
- Экспорт отчётов в `.txt` или `.xlsx`.
- Веб-интерфейс.
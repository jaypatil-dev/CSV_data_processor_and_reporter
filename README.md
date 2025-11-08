# 📈 CSV Data Processor & Reporter (Python & NumPy)

This project is a command-line tool designed to ingest structured data from a **CSV file**, perform comprehensive statistical analysis using the **NumPy library**, and output the results to a structured **report file**.

It demonstrates file handling and data processing skills necessary for working with real-world datasets.

## ✨ Features

* **CSV Ingestion:** Reads data from a specified CSV file (`data.csv`) using Python's built-in `csv` module.
* **Data Transformation:** Extracts and converts specific score columns into a flat NumPy array.
* **Statistical Analysis:** Calculates **Mean, Median, Standard Deviation, Variance, Minimum, and Maximum** for the dataset.
* **Report Generation:** Writes a clean, formatted analysis report to a text file (`report.txt`).

## 🛠️ Concepts Demonstrated

This project showcases a solid combination of basic and intermediate Python skills:

| Concept | Python Tool Used | Purpose |
| :--- | :--- | :--- |
| **File Handling** | `with open(...)` | Safely opens and closes both the input and output files. |
| **CSV Parsing** | `import csv`, `csv.reader` | Reads structured, comma-separated data row by row. |
| **Data Cleaning** | **List Comprehension** | Efficiently converts string data (scores) into numerical `float` types. |
| **Numerical Computing** | **NumPy** (`np.array`, `np.mean`, `np.std`) | Provides fast, vectorized statistical calculations. |
| **Functions & Scope** | `def analyze_data(...)` | Organizes the statistical calculation logic. |

## 🚀 How to Run

### Prerequisites

You need Python installed, and you must install the **NumPy** library.

1.  **Install NumPy:**
    ```bash
    pip install numpy
    ```

### Execution Steps

1.  **Setup Data:** Ensure you have a CSV file named `data.csv` in the same directory as the script. The file **must** have a header row and numeric data you wish to analyze (e.g., `Name,Score1,Score2`).

    > Example `data.csv` content:
    > ```csv
    > Name,Score1,Score2
    > Alice,85,90
    > Bob,70,75
    > Charlie,92,88
    > ```

2.  **Run the script** from your terminal:
    ```bash
    python your_script_name.py
    ```
3.  The script will execute silently and generate the `report.txt` file in the same folder.

## 💡 Example Report Output (`report.txt`)

```text
====================
Data Analysis Report
====================
Names: Alice, Bob, Charlie
Scores1: 85.0, 70.0, 92.0
Scores2: 90.0, 75.0, 88.0

Mean (Average) of class: 83.33
Median of class: 86.50
Standard Deviation of class: 7.78
Variance of class: 60.56
Minimum of class: 70.00
Maximum of class: 92.00

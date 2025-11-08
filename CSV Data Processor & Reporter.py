import numpy as np
import csv
# Function to calculate statistical measures
def analyze_data(scores):
        analysis = {}
        analysis['mean'] = np.mean(scores)
        analysis['median'] = np.median(scores)
        analysis['std_dev'] = np.std(scores)
        analysis['var'] = np.var(scores)
        analysis['min'] = np.min(scores)
        analysis['max'] = np.max(scores)
        return analysis
# Read data from CSV file
with open('data.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    try:
        header = next(reader)
    except StopIteration:
        print("Error: The CSV file is empty.")
        exit()
    data_rows = list(reader)
# Extract names and scores
    names = [row[0] for row in data_rows]
    scores1 = [float(row[1]) for row in data_rows]
    scores2 = [float(row[2]) for row in data_rows]
    scores = np.array([scores1, scores2]).flatten()
# Analyze data
results = analyze_data(scores)
# Generate report
with open('report.txt', 'w', newline='') as rf:
    rf.write("====================\n")
    rf.write("Data Analysis Report\n")
    rf.write("====================\n")
    rf.write(f"Names: {', '.join(names)}\n")
    rf.write(f"Scores1: {', '.join(map(str, scores1))}\n")
    rf.write(f"Scores2: {', '.join(map(str, scores2))}\n\n")
    rf.write(f"Mean (Average) of class: {results['mean']:.2f}\n")
    rf.write(f"Median of class: {results['median']:.2f}\n")
    rf.write(f"Standard Deviation of class: {results['std_dev']:.2f}\n")
    rf.write(f"Variance of class: {results['var']:.2f}\n")
    rf.write(f"Lowest Score of class: {results['min']:.2f}\n")
    rf.write(f"Highest Score of class: {results['max']:.2f}\n")
# Notify user
    print("Data analysis report generated in report.txt")
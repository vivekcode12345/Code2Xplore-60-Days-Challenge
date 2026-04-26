# 📊 Academic Data Drift & Copy Behavior Analyzer

## 📚 Course Information

* **Subject:** Hands-on Python
* **Course Code:** CSE205
* **Instructor:** Dr. Yasir Afaq

---

## 👨‍🎓 Student Details

* **Name:** Vivek Verma
* **Register Number:** *(AP24110011638)*
* **Section:** *(I)*

---

## 🚀 Project Overview

This project simulates a university academic system where student data is duplicated for analysis. The goal is to study how improper copying techniques (shallow vs deep copy) can lead to **data drift** and inconsistencies.

The system performs statistical analysis using **NumPy and Pandas**, applies transformations using **math functions**, and detects whether the system is stable or affected by drift.

---

## 🎯 Objectives

* Generate student data using random values
* Store data in nested structures (list of dictionaries)
* Analyze data using Pandas and NumPy
* Understand shallow vs deep copy behavior
* Detect data drift after mutation
* Classify system stability

---

## 🧠 Key Concepts Used

* Lists, Dictionaries, Tuples, Sets
* Functions (Modular Programming)
* Random Data Generation
* NumPy (mean, std deviation)
* Pandas DataFrame
* Math module (sqrt transformation)
* Shallow Copy vs Deep Copy

---

## ⚙️ Functional Components

### 1. `generate_data(n)`

Generates student data with:

* ID
* Marks
* Attendance
* Scores (internal, assignment)

---

### 2. `mutate_data(data, roll)`

Applies mutation rules:

* Marks updated using:

```python
marks = marks + sqrt(marks)
```

* Attendance modified
* Scores list updated
* Applied only on selected indexes

---

### 3. `analyze_data(df)`

Calculates:

* Mean (NumPy + Manual)
* Median
* Standard deviation

---

### 4. `detect_drift(original, modified)`

Calculates:

```python
drift = abs(original_mean - modified_mean)
```

---

## 🔄 Copy Behavior

### 🔹 Shallow Copy

* Shares nested structures
* Changes affect original data
* Causes unintended drift

### 🔹 Deep Copy

* Fully independent copy
* No effect on original data

---

## 🧪 Mutation Logic (Personalized)

```python
index_condition = i % (roll_number % 3) == 0
```

Only selected student records are modified based on roll number.

---

## 📊 Analysis Performed

* Mean, Median, Standard Deviation
* Drift Calculation
* Marks Normalization
* Pattern Detection

---

## 🚨 Drift Detection Rules

| Condition         | Classification        |
| ----------------- | --------------------- |
| Drift < Threshold | Stable Data           |
| Moderate Drift    | Minor Drift           |
| High Drift        | Critical Drift        |
| Original Modified | Copy Failure Detected |

---

## ⚠️ Key Insight

Shallow copy leads to **data drift** because it shares inner structures like lists and dictionaries.
When modified, both copied and original data change unintentionally.

Deep copy prevents this by creating completely separate memory references.

---

## 🧪 Sample Output

```text
Original Mean: 65.2
Modified Mean: 72.8
Drift: 7.6

Result:
Minor Drift

Tuple Output:
(72.8, 7.6, 12.4)
```

---

## 🛠️ How to Run

```bash
python analyzer.py
```

---

## 📁 Project Structure

```
📦 Academic-Data-Drift-Analyzer
 ┣ 📜 analyzer.py
 ┗ 📄 README.md
```

---

## 🎓 Learning Outcomes

* Difference between shallow and deep copy
* Data drift concept in real-world systems
* Statistical analysis using Python libraries
* Importance of data isolation

---

## 📌 Declaration

This project is created as part of academic coursework and reflects my understanding of Python data handling and analysis.
---

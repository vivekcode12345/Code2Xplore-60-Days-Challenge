# 📊 Multi-Dimensional Academic Intelligence System

## 📌 Project Overview

This project analyzes student performance using multiple factors such as marks, attendance, and assignment scores.
It uses Python along with powerful libraries like Pandas and NumPy to generate insights and classify students.

---

## 🎯 Objectives

* Generate student data using simulation
* Store data using Python data structures
* Perform statistical analysis
* Classify students into categories
* Detect patterns and generate final insights

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Math Module
* Random Module

---

## 📂 Data Structure

Each student record contains:

* `student_id`
* `marks (0–100)`
* `attendance (0–100)`
* `assignment score (0–50)`

Data is first stored in a list and then converted into a Pandas DataFrame.

---

## ⚙️ Features Implemented

### ✅ Data Generation

* Randomly generates student data using `random` module

### ✅ Data Storage

* Uses:

  * Lists
  * Tuples
  * Dictionary
  * Set

### ✅ Data Analysis

* Mean, Median, Standard Deviation (NumPy)
* Correlation between marks and attendance
* Manual calculation of maximum marks

### ✅ Normalization

Marks are normalized using:

```
(x - min) / (max - min)
```

### ✅ Classification Logic

| Condition                      | Category      |
| ------------------------------ | ------------- |
| marks < 40 OR attendance < 50  | At Risk       |
| marks 40–70                    | Average       |
| marks 71–90                    | Good          |
| marks > 90 AND attendance > 80 | Top Performer |

---

## 🧠 Performance Index Formula

```
performance_index = (marks * 0.6 + assignment * 0.4) * log(attendance + 1)
```

### Why this works:

* Gives more weight to marks
* Includes assignment contribution
* Uses logarithm to balance attendance impact

---

## 🔍 Pattern Detection

* **Consistency:** std deviation < 15
* **Attendance Risk:** more than 3 students have attendance < 50
* **High Achievement:** at least 2 top performers

---

## 📊 Output Includes

* DataFrame table
* Categorized dictionary
* Statistical summary
* Tuple → `(mean, std_dev, max_marks)`
* Final system insight

---

## 🧾 Final Insights Categories

* Stable Academic System
* Moderate Performance
* Critical Attention Required

---

## 🧩 Functions Used

* `create_records()` → Generates student data
* `assign_category()` → Classifies students
* `compute_stats()` → Performs analysis

---

## 🚀 How to Run

1. Install required libraries:

```
pip install pandas numpy
```

2. Run the Python file:

```
python filename.py
```

---

## 📚 Learning Outcomes

* Learned how to use Pandas and NumPy together
* Understood data analysis and classification
* Implemented real-world logic using Python
* Improved coding structure using functions

---

## 📎 Author

**Vivek Verma**
B.Tech CSE, SRM University–AP

---

## ⚠️ Disclaimer

This project is created for academic purposes as part of the Code2Xplore Challenge.

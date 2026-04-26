# 📦 Smart Inventory Mutation Tracker

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

This project simulates a warehouse inventory system using Python.
The inventory is represented as a nested data structure (list of dictionaries), where each product contains details like price, stock, and supplier rating.

The main objective is to analyze how data behaves when copied using:

* **Shallow Copy**
* **Deep Copy**

and observe how mutations affect original data.

---

## 🎯 Objectives

* Understand nested data structures in Python
* Learn the difference between shallow copy and deep copy
* Track how data changes after mutation
* Compare original and modified data

---

## 🧠 Key Concepts Used

* Lists and Dictionaries
* Functions (Modular Programming)
* Loops and Conditional Statements
* Shallow Copy (`copy.copy()`)
* Deep Copy (`copy.deepcopy()`)

---

## ⚙️ Functional Components

### 1. `create_inventory()`

Creates the initial inventory with nested product details.

### 2. `apply_discount(data, index)`

Applies:

* 10% price reduction
* Stock modification
  to a specific item based on index.

### 3. `compare_data(original, modified)`

Compares datasets and returns:

```
(changed_items_count, unchanged_items_count)
```

---

## 🔄 Copy Operations

### 🔹 Shallow Copy

* Copies only outer structure
* Nested objects are shared
* Changes in copy affect original

### 🔹 Deep Copy

* Creates completely independent copy
* No shared references
* Original remains unchanged

---

## 🧪 Mutation Logic

* Price reduced by **10%**
* Stock updated for selected item
* Selection based on personalization rule:

```
index = roll_number % len(inventory)
```

---

## 📊 Sample Output

```
Original Inventory:
[ {...}, {...} ]

Shallow Copy:
[ {...modified...} ]

Deep Copy:
[ {...modified...} ]

Comparison Results:
Shallow Copy → (1, 1)
Deep Copy → (1, 1)
```

---

## 🔍 Analysis

* **Shallow Copy Result:**
  Changes affected the original data because nested dictionaries are shared.

* **Deep Copy Result:**
  Original data remained unchanged due to independent memory allocation.

---

## ⚠️ Key Insight

Shallow copy fails to isolate changes because it only duplicates the top-level structure.
Nested objects remain linked, causing unintended modifications.

Deep copy avoids this issue by creating completely separate objects.

---

## 🧪 Test Cases

| Test Case | Description                    | Result |
| --------- | ------------------------------ | ------ |
| 1         | Shallow copy modifies original | ✅      |
| 2         | Deep copy remains independent  | ✅      |
| 3         | Mutation applied correctly     | ✅      |

---

## 🛠️ How to Run

```bash
python inventory_tracker.py
```

---

## 📁 Project Structure

```
📦 Smart-Inventory-Tracker
 ┣ 📜 inventory_tracker.py
 ┗ 📄 README.md
```

---

## 🎓 Learning Outcomes

* Clear understanding of shallow vs deep copy
* Hands-on experience with nested data structures
* Importance of data isolation in real-world systems
* Practical implementation of Python concepts

---

## 📌 Declaration

This project is developed as part of academic coursework and demonstrates original implementation and understanding of the concepts.

---


---

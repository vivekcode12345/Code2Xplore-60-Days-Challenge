# Emergency Resource Dispatch Analyzer

## 📌 Project Description

This program analyzes emergency resource requests from different disaster zones.
Each request is checked and classified into categories like low, moderate, high, or invalid demand.

After classification, the program applies a personalized filtering rule based on the length of the user’s name.
Finally, it generates a dispatch report showing valid requests, removed requests, and final demand lists.

---

## 🎯 Features

* Accepts multiple resource requests from the user
* Classifies each request into demand categories
* Identifies invalid and zero requests
* Applies personalized filtering using PLI (Personal Logic Index)
* Counts total valid requests
* Counts requests removed due to personalization
* Displays final categorized dispatch report

---

## 🧠 Classification Rules

| Request Value | Category        |
| ------------- | --------------- |
| Less than 0   | Invalid Request |
| 0             | No Demand       |
| 1 – 20        | Low Demand      |
| 21 – 49       | Moderate Demand |
| 50 or more    | High Demand     |

---

## 🔧 Personalization Rule (PLI)

1. Calculate name length (without spaces)
2. PLI = name length % 3

Filtering applied:

| PLI Value | Rule Applied                       |
| --------- | ---------------------------------- |
| 0         | Remove all Low Demand requests     |
| 1         | Remove all High Demand requests    |
| 2         | Keep only Moderate Demand requests |

---

## ▶ How to Run

1. Run the program
2. Enter number of resource requests
3. Enter each request value
4. Enter your full name
5. View the final dispatch report

---

## 📥 Example Input

Enter number of resource requests: 5
Enter request: 10
Enter request: 25
Enter request: 60
Enter request: -3
Enter request: 45
Enter your full name: Rahul Kumar

---

## 📤 Output Shows

* Name length and PLI
* Total valid requests
* Requests removed due to PLI
* Final lists of demand categories
* Invalid requests

---

## 🛠 Technologies Used

* Python
* Lists
* Loops
* Conditional statements

---

## 📚 Learning Outcome

From this project, I learned how to:

* Store and process data using lists
* Use loops and conditions for classification
* Apply personalized logic using modulus
* Filter data based on rules
* Generate structured program output
## Author
VIVEK VERMA

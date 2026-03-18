# 🚨 Smart Transaction Risk Detector

## 🏫 Academic Details
- **Course:** CSE205 – Hands-on Python  
- **Challenge:** Code2Xplore – DAY-6  
- **Department:** Computer Science and Engineering  
- **University:** SRM University–AP  

---

## 📌 Problem Understanding
This project analyzes daily digital payment transactions and detects suspicious spending patterns.  
Each transaction is categorized into **invalid**, **normal**, **large**, or **high-risk**.  
Pattern detection rules are then applied to determine the **overall risk level**.

---

## 🧠 Algorithm Explanation
1. Input the number of transactions and store them in a list.  
2. Classify transactions into categories: invalid, normal, large, high-risk.  
3. Calculate the total transaction value and count.  
4. Apply detection rules:
   - Frequent transactions → more than 5 entries  
   - Large spending → total amount > 5000  
   - Suspicious activity → 3 or more high-risk transactions  
5. Determine the final risk level:
   - High Risk → if suspicious activity detected  
   - Moderate Risk → if frequent transactions or large spending  
   - Low Risk → otherwise  

---

## ⚙️ Features Used
- Lists  
- For loops  
- Conditional statements  
- List comprehension  
- Dictionary for classification  
- Tuple for summary  

---

## ➕ Test Case Verification

### 🔹 Test Case 1
Input: 5 50 600 2200 0 1500  
Output:  
Categorized Transactions: {'invalid': [0], 'normal': [50], 'large': [600, 1500], 'high_risk': [2200]}  
Total Transaction Value: 4350  
Number of Transactions: 6  
Risk Classification: Low Risk  

---

### 🔹 Test Case 2
Input: 6 2500 2600 2700 100 200 300  
Output:  
Categorized Transactions: {'invalid': [], 'normal': [100, 200, 300], 'large': [], 'high_risk': [2500, 2600, 2700]}  
Total Transaction Value: 8400  
Number of Transactions: 6  
Risk Classification: High Risk  

---

### 🔹 Test Case 3
Input: 50 150 700 2500 3000 100  
Output:  
Categorized Transactions: {'invalid': [], 'normal': [50, 150, 100], 'large': [700], 'high_risk': [2500, 3000]}  
Total Transaction Value: 6500  
Number of Transactions: 6  
Risk Classification: High Risk  

---

### 🔹 Test Case 4
Input: 200 300 400 100  
Output:  
Categorized Transactions: {'invalid': [], 'normal': [200, 300, 400, 100], 'large': [], 'high_risk': []}  
Total Transaction Value: 1000  
Number of Transactions: 4  
Risk Classification: Low Risk  

---

### 🔹 Test Case 5
Input: 100 200 800 900 1200 300  
Output:  
Categorized Transactions: {'invalid': [], 'normal': [100, 200, 300], 'large': [800, 900, 1200], 'high_risk': []}  
Total Transaction Value: 3500  
Number of Transactions: 6  
Risk Classification: Moderate Risk  

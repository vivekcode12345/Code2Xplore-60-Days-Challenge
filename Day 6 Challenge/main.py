n = int(input("Enter number of transactions: "))
tns = []
for i in range(n):
    val = int(input("Enter transaction amount: "))
    tns.append(val)

tns_data = {
    "invalid": [val for val in tns if val <= 0],
    "normal": [val for val in tns if 1 <= val <= 500],
    "large": [val for val in tns if 501 <= val <= 2000],
    "high_risk": [val for val in tns if val > 2000]
}

valid_list = [val for val in tns if val > 0]
total_amt = sum(valid_list)
total_count = len(tns)

result = (total_amt, total_count)

freq_check = total_count > 5
spending_check = total_amt > 5000
sus_check = len(tns_data["high_risk"]) >= 3

if sus_check:
    risk = "High Risk"
elif spending_check or freq_check:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

print("Categorized Transactions:", tns_data)
print("Total Transaction Value:", result[0])
print("Number of Transactions:", result[1])
print("Risk Classification:", risk)
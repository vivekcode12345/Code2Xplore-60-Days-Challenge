D = 0
n = int(input("Enter number of activity scores: "))
scores = []
for i in range(n):
    value = int(input("Enter score: "))
    scores.append(value)
low = []
medium = []
high = []
critical = []
valid = 0
ignored = 0
for i in range(n):
    if scores[i] < 0:
        ignored += 1
    else:
        valid += 1
        if scores[i] <= 30:
            low.append(scores[i])
        elif scores[i] <= 60:
            medium.append(scores[i])
        elif scores[i] <= 100:
            high.append(scores[i])
        else:
            critical.append(scores[i])

print("Register Digit (D):", D)
print("Low Risk:", low)
print("Medium Risk:", medium)
print("High Risk:", high)
print("Critical Risk:", critical)
print("After Personalized Filtering:")
removed = len(low)
low = []
print("Low Risk:", low)
print("Medium Risk:", medium)
print("High Risk:", high)
print("Critical Risk:", critical)

print("Total Valid Entries:", valid)
print("Ignored Entries:", ignored)
print("Removed Due to Personalization:", removed)

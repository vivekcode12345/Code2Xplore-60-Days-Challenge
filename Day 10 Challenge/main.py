import random
import pandas as pd
import numpy as np
import math
import copy
def generate_data(n):
    data = []
    for i in range(n):
        student = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 25), random.randint(10, 25)]
        }
        data.append(student)
    return data

def mutate_data(data, roll):
    mod = roll % 3
    for i in range(len(data)):
        if mod != 0 and i % mod == 0:
            data[i]["marks"] = data[i]["marks"] + math.sqrt(data[i]["marks"])
            data[i]["attendance"] -= 5
            data[i]["scores"][0] += 2

def analyze_data(df):
    mean = np.mean(df["marks"])
    median = np.median(df["marks"])
    std = np.std(df["marks"])
    manual_mean = sum(df["marks"]) / len(df["marks"])

    return mean, median, std, manual_mean

def detect_drift(original_mean, modified_mean):
    return abs(original_mean - modified_mean)

data = generate_data(12)

roll_number = 12345  # change this
shallow_copy = copy.copy(data)
deep_copy = copy.deepcopy(data)

mutate_data(shallow_copy, roll_number)
mutate_data(deep_copy, roll_number)

df_original = pd.DataFrame(data)
df_shallow = pd.DataFrame(shallow_copy)
df_deep = pd.DataFrame(deep_copy)

mean_o, median_o, std_o, manual_o = analyze_data(df_original)
mean_d, median_d, std_d, manual_d = analyze_data(df_deep)

drift = detect_drift(mean_o, mean_d)

threshold = 5

if not df_original.equals(df_shallow):
    status = "Copy Failure Detected"
elif drift < threshold:
    status = "Stable Data"
elif drift < 10:
    status = "Minor Drift"
else:
    status = "Critical Drift"

print("\nOriginal Data:\n", df_original)
print("\nShallow Copy:\n", df_shallow)
print("\nDeep Copy:\n", df_deep)
print("\nDrift Value:", drift)
print("Tuple Output:", (mean_d, drift, std_d))
print("\nFinal Classification:", status)
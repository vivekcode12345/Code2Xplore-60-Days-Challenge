import random
import pandas as pd
import numpy as np
import math
def create_records(count):
    records = []
    for i in range(count):
        sid = i + 1
        m = random.randint(0, 100)
        att = random.randint(0, 100)
        assign = random.randint(0, 50)

        records.append((sid, m, att, assign))
    return records

def assign_category(df):
    result = {}

    for i in range(len(df)):
        marks = df.loc[i, 'marks']
        att = df.loc[i, 'attendance']

        if marks < 40 or att < 50:
            label = "At Risk"
        elif marks <= 70:
            label = "Average"
        elif marks <= 90:
            label = "Good"
        elif marks > 90 and att > 80:
            label = "Top Performer"
        else:
            label = "Average"

        result[df.loc[i, 'student_id']] = label

    return result

def compute_stats(df):
    marks_arr = df['marks'].values

    avg = np.mean(marks_arr)
    med = np.median(marks_arr)
    sd = np.std(marks_arr)
    max_val = marks_arr[0]
    for x in marks_arr:
        if x > max_val:
            max_val = x
    mn = np.min(marks_arr)
    mx = np.max(marks_arr)
    df['norm_marks'] = [(x - mn) / (mx - mn) for x in marks_arr]
    correlation = np.corrcoef(df['marks'], df['attendance'])[0][1]

    return avg, med, sd, max_val, correlation

num_students = 10

student_data = create_records(num_students)

df = pd.DataFrame(student_data, columns=['student_id', 'marks', 'attendance', 'assignment'])

df['perf_index'] = df.apply(
    lambda r: (r['marks'] * 0.6 + r['assignment'] * 0.4) * math.log(r['attendance'] + 1),
    axis=1
)

cat_map = assign_category(df)
avg, med, sd, max_val, corr = compute_stats(df)

is_consistent = sd < 15
low_attendance = sum(df['attendance'] < 50) > 3
top_count = list(cat_map.values()).count("Top Performer") >= 2

if is_consistent and not low_attendance:
    final_msg = "Stable Academic System"
elif top_count:
    final_msg = "Moderate Performance"
else:
    final_msg = "Critical Attention Required"

# OUTPUT
print("DataFrame:\n", df)
print("\nCategory Mapping:\n", cat_map)
print("\nStats Tuple:", (avg, sd, max_val))
print("\nCorrelation:", corr)
print("\nFinal Insight:", final_msg)
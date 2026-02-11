# Student Marks Evaluation Program

This Python program evaluates the marks of students and categorizes them based on performance. It also handles small adjustments to marks based on a predefined rule derived from a registration number.

---

## Features

- Accepts the number of students and their marks as input.
- Adjusts marks according to the last digit of a registration number:
  - If the last digit is **even**, subtracts 2 from each mark.
  - If the last digit is **odd**, adds 2 to each mark.
- Validates marks (should be between 0 and 100 after adjustment).
- Categorizes students based on marks:
  - `90-100` → Excellent
  - `75-89` → Very Good
  - `60-74` → Good
  - `40-59` → Average
  - `<40` → Fail
- Counts total valid students and failed students.

---

## How to Run

1. Clone or download the script.
2. Run the program in Python 3:

```bash
python student_marks.py
3. Enter the number of students.
4. Enter the marks of each student one by one.
5. The program will display each student’s performance category and summary statistics.

Author

Vivek Verma

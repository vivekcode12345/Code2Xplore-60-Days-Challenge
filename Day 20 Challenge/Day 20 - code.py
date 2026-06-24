
marks = []
m = int(input("enter the no. of entries: "))

for i in range(m):
    n = int(input("enter the marks: "))
    marks += [n]

print(marks)

x = int(input("enter 0/1 to insert or not: "))

while x:
    p = int(input("enter the position: "))
    num = int(input("enter the number: "))

    if p < 0 or p > m:
        print("out of range")
    else:
        marks += [0]
        m += 1
        for i in range(m - 1, p, -1):
            marks[i] = marks[i - 1]
        marks[p] = num
        print(marks)
    x=int(input("enter 0/1 to insert or not: "))

x=int(input("enter 0/1 to delete or not: "))
while x:
    p = int(input("enter the position: "))
    num = int(input("enter the number: "))
    if p < 0 or p > m:
        print("out of range")
    else:
        for i in range(p, m - 1):
            marks[i] = marks[i + 1]
        marks.pop()
        m -= 1
        print(marks)
    x = int(input("enter 0/1 to delete or not: "))

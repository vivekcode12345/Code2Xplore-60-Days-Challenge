regNo = "AP24110011638"
ld = int(regNo[-1])
n = int(input("Enter number of students: "))
marks = [0] * n
for i in range(n):
    marks[i] = int(input("Enter marks of students: "))
valid= 0
fail= 0
for i in marks:
    if ld % 2 == 0:
        i = i- 2
    else:
        i = i + 2
    if i < 0 or i > 100:
        print(i, "-> Invalid")
    else:
        valid = valid+ 1

        if i>= 90:
            print(i, "-> Excellent")

        elif i>= 75:
            print(i, "-> Very Good")

        elif i >= 60:
            print(i, "-> Good")

        elif i >= 40:
            print(i, "-> Average")

        else:
            print(i, "-> Fail")
            fail = fail + 1
print("Total Valid Students:", valid)
print("Total Failed Students:", fail)

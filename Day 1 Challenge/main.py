name=input("Enter your name: ")
email=input("Enter your email: ")
mobile=input("Enter your mobile number: ")
age=(input("Enter your age: "))
x=len(name)
flag=False
if x>=2 and name[0] != " " and name[-1] != " ":
    if "@" in email and "." in email and email[0] != "@":
        if len(mobile) == 10 and mobile.isdigit() and mobile[0] != '0':
            if age.isdigit():
                age = int(age)
                if age>=18 & age<=65:
                    flag=True
if flag:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")






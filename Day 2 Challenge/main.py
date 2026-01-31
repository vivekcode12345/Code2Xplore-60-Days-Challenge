stu_id = input("Enter Student ID: ")
email_id = input("Enter Email ID: ")
password = input("Enter Password: ")
ref_id = input("Enter Referral Code: ")
flag = False
if (len(stu_id) == 7 and stu_id[3] == "-" and stu_id[4].isdigit() and stu_id[0:3] == "CSE"
        and stu_id[5].isdigit() and stu_id[6].isdigit()):
    if (email_id.count("@") == 1 and email_id[0] != "@" and email_id[-4:] == ".edu"
            and "." in email_id[1:-4]):
        digit_found = False
        for ch in password:
            if ch.isdigit():  # checks if the character is a digit
                digit_found = True
                break
            if digit_found:
                if (len(ref_id) == 6 and ref_id[0:3] == "REF" and ref_id[3].isdigit() and
                        ref_id[4].isdigit() and ref_id[5] == "@"):
                     flag = True

if flag:
    print("APPROVED")
else:
    print("REJECTED")

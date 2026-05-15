percentage=[75,80,90,63,60,70]
count=0
for i in range(len(percentage)):
    if percentage[i]>=75:
        print("Eligible")
        count+=1
    elif percentage[i]>=65 and percentage[i]<=74:
        print("Condonation")
    else: 
        print("Not Eligible")
print(f"The number of eligible persons is {count}.")

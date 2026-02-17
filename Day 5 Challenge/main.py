n = int(input("Enter number of resource requests: "))
requests = []
for i in range(n):
    value = int(input("Enter request: "))
    requests.append(value)
name = input("Enter your full name: ")
val_len = name.replace(" ", "")
L = len(val_len) #real length
PLI = L % 3

low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

valid_count = 0

for r in requests:
    if r < 0:
        invalid_requests.append(r)
    else:
        valid_count = valid_count + 1
        if r == 0:
            pass
        elif r >= 1 and r <= 20:
            low_demand.append(r)
        elif r >= 21 and r <= 49:
            moderate_demand.append(r)
        elif r >= 50:
            high_demand.append(r)

rem_count = 0
if PLI == 0:
    rem_count = len(low_demand)
    low_demand = []

elif PLI == 1:
    rem_count = len(high_demand)
    high_demand = []

elif PLI == 2:
    rem_count = len(low_demand) + len(high_demand)
    low_demand = []
    high_demand = []

print("Name length without spaces:", L)
print("PLI:", PLI)
print("Total valid requests:", valid_count)
print("Requests removed due to PLI:", rem_count)
print("Low Demand:", low_demand)
print("Moderate Demand:", moderate_demand)
print("High Demand:", high_demand)
print("Invalid Requests:", invalid_requests)

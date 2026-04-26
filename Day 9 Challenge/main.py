import copy
def create_inventory():
    return [
        {
            "item": "Laptop",
            "details": {
                "price": 50000,
                "stock": 10,
                "supplier": {"name": "ABC Corp", "rating": 4.5}
            }
        },
        {
            "item": "Phone",
            "details": {
                "price": 20000,
                "stock": 25,
                "supplier": {"name": "XYZ Ltd", "rating": 4.2}
            }
        }
    ]
def apply_discount(data, index):
    for i in range(len(data)):
        if i == index:
            data[i]["details"]["price"] *= 0.9  # 10% discount
            data[i]["details"]["stock"] -= 2

def compare_data(original, modified):
    changed = 0
    unchanged = 0

    for i in range(len(original)):
        if original[i] == modified[i]:
            unchanged += 1
        else:
            changed += 1

    return (changed, unchanged)

inventory = create_inventory()

roll_number = 12345
index = roll_number % len(inventory)

shallow_copy = copy.copy(inventory)
deep_copy = copy.deepcopy(inventory)
apply_discount(shallow_copy, index)
apply_discount(deep_copy, index)

shallow_result = compare_data(inventory, shallow_copy)
deep_result = compare_data(inventory, deep_copy)

print("Original Inventory:")
print(inventory)

print("\nShallow Copy:")
print(shallow_copy)

print("\nDeep Copy:")
print(deep_copy)

print("\nComparison Results:")
print("Shallow Copy (changed, unchanged):", shallow_result)
print("Deep Copy (changed, unchanged):", deep_result)
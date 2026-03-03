import sys
lis = []
for argv in sys.argv[1:]:
    lis.append(argv)
dic = {}
for items in lis:
    name, count = items.split(":")
    dic[name] = int(count)
Total_items = 0
for values in dic.values():
    Total_items = Total_items + values
unique_items = len(dic)
print("=== Inventory System Analysis ===")
print(f"Total items in inventory: {Total_items}")
print(f"Unique item types: {unique_items}\n")
print("=== Current Inventory ===")
max_count = 0
max_key = ""
for key, value in dic.items():
    if value > max_count:
        max_count = value
        max_key = key
#print(f"{nam}: {coun} units ({(coun/Total_items)*100:.1f}%)")

for i in range (max_count, 0, -1):
    for ky , ve in dic.items():
        if i == ve:
            if ve > 1:
                unit = "units"
            else:
                unit = "unit"
            print(f"{ky}: {ve} {unit} ({(ve/Total_items)*100:.1f}%)")

print("\n=== Inventory Statistics ===")
print(f"Most abundant: {max_key} ({max_count} units)")
less_count = 100000000
less_key = ""
for k, v in dic.items():
    if v < less_count:
        less_count = v
        less_key = k
print(f"Least abundant: {less_key} ({less_count} unit)\n")
print("=== Item Categories ===")
moderate = {}
scarce = {}
for ke , va in dic.items():
    if va >= 5:
        moderate[ke] = va
    else:
        scarce[ke] = va
print(f"Moderate: {moderate}")
print(f"Scarce: {scarce}\n")
print("=== Management Suggestions ===")
stock = ""
for kk , vv in dic.items():
    if vv == less_count:
        stock = stock + kk + ", "
print(f"Restock needed: {stock[:-2]}\n")
print("=== Dictionary Properties Demo ===")
keystr=""
for kkk in dic.keys():
    keystr = keystr + kkk + ", "
print(f"Dictionary keys: {keystr[:-2]}")
valstr = ""
for vvv in dic.values():
    valstr = valstr + str(vvv) + ", "
print(f"Dictionary values: {valstr[:-2]}")
is_present = "sword" in dic
print(f"Sample lookup - 'sword' in inventory: {is_present}")














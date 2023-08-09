dict1 = { "k2": [5, 18, 16, 18, 18], 
        "k1": [17, 18, 5, 17, 17, 16], 
        "k3": [17, 18, 16, 5, 9] 
        }

sort_keys = {}
keys = sorted(dict1.keys())
for key in keys:
    sort_keys[key] = dict1[key]



avgs = []
for values in sort_keys.values():
    average = sum(values) / len(values)
    avgs.append(average)
median = sorted(avgs)[len(avgs) // 2]



highdiff = 1
maxdis = ""
for key, values in sort_keys.items():
    difvalues = set(values)
    difcount = len(difvalues)
    if difcount > highdiff:
        highdiff = difcount
        maxdis = key


N=16
for key in dict1:
    values = dict1[key]
    new_values = []
    for value in values:
        if value <= N:
            new_values.append(value)
    dict1[key] = new_values


print()
print(sort_keys)
print()
print("median=",median)
print()
print("key with max distint value=",maxdis)
print()
print("After Deletion:", dict1)
print()

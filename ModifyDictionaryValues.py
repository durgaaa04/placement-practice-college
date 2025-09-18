# Modify the values of a dictionary by increasing it by 1
d = {"k1" : 10, "k2" : 20, "k3" : 30}
for i in d.keys():
    d[i] += 1
print(d.values())

# Merge Dictionaries using for Loop
d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}

print("dictonary 1",d1)
print("dictonary 2",d2)


for k,v in d2.items():
    d1[k]=v

print("merged dictonary using loop",d1)

print("****************************************************************")

# Merge Dictionaries using update()
print("Merge Dictionaries using update()")
d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}


print("dictonary 1",d1)
print("dictonary 2",d2)


print(d1)
d1.update(d2)
print("merged dictonary using update",d1)

# Merge Dictionaries using Union Operator
print("Merge Dictionaries using Union Operator")
d1={'A1': 20, 'B1': 25, 'C1': 40, 'D1': 50}
d2={"X1":100, "Y1":200, "b1":25, "A1":22,"D1":"Hello"}
print("dictonary 1",d1)
print("dictonary 2",d2)

print(d1 | d2 )
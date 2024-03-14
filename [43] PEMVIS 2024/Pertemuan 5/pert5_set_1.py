# melibatkan data berjenis set(1)
Set_1 = {"Toyota", "Daihatsu", "Honda"}
Set_2 = set(("Toyota", "Daihatsu", "Honda"))

print("Tipe data Set_1 adalah ", type(Set_1))
print("Tipe data Set_2 adalah ", type(Set_2))
print("Data Set_1:", Set_1)
print("Data Set_2:", Set_2)
print("-------------------------------")

for x in Set_1:
    print(x)
print("-------------------------------")

print(len(Set_1))

if "Daihatsu" in Set_1:
    print("Yes", 'Daihatsu is an item in Set_1')

Set_1.add("Mitsubishi")
print(Set_1)

Set_1.update(["Suzuki", "Mazda", "Nissan"])
print(Set_1)

# remove
Set_1.remove('Honda')
print(Set_1)

# discard
Set_1.discard("Mazda")

# pop
Set_1.pop()
print(Set_1)

# clear
Set_1.clear()
print(Set_1)

# delete
del Set_1
print("-------------------------------")

# union of two sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
print("-------------------------------")

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
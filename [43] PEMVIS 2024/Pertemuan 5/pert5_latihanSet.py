# LATIHAN SET
set_1 = {"Orange", "Apple", "Banana", "Peach", "Watermelon", "Melon"}
set_2 = {"Apple", "Tomato", "Sauce", "Watermelon"}

print("Tipe data set_1:", type(set_1))
print("Tipe data set_2:", type(set_2))
print("Data set_1:", set_1)
print("Data set_2:", set_2)
print("=========================================")
opt = int(input("set_1(1), set_2(2): "))

if opt == 1:
    data = ""
    tools = int(input("add(1), update(2), remove(3), discard(4), pop(5), clear(6): "))
    if tools == 1:
        data = input("data: ")
        set_1.add(data)
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    elif tools == 2:
        data = input("data: ")
        set_1.update(data)
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    elif tools == 3:
        data = input("data: ")
        set_1.update(data)
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    elif tools == 4:
        data = input("data: ")
        set_1.discard(data)
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    elif tools == 5:
        set_1.pop()
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    elif tools == 6:
        set_1.clear()
        print("=========================================")
        print("Data set_1:", set_1)
        print("=========================================")
    else:
        print("Wrong order!")
elif opt == 2:
    data = ""
    tools = int(input("add(1), update(2), remove(3), discard(4), pop(5), clear(6): "))
    if tools == 1:
        data = input("data: ")
        set_2.add(data)
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    elif tools == 2:
        data = input("data: ")
        set_2.update(data)
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    elif tools == 3:
        data = input("data: ")
        set_2.update(data)
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    elif tools == 4:
        data = input("data: ")
        set_2.discard(data)
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    elif tools == 5:
        set_2.pop()
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    elif tools == 6:
        set_2.clear()
        print("=========================================")
        print("Data set_2:", set_2)
        print("=========================================")
    else:
        print("Wrong order!")
else:
    print("Wrong commands!")


    
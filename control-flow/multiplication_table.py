num = int(input("Enter a number to see its multiplication table: "))

for i in range(1, 11):
    number = num * i
    print(f"{number} * {i} = {number}")

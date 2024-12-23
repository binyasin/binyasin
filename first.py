num = int(input("Enter a number for the table: "))

for i in range(1, 12):  # Use range(1, 12) to include 11
    print(f"{num} x {i} = {num * i}")
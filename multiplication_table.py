try:
    table_of = int(input("Enter a Number: "))
except ValueError:
    print("!!Enter a Valid Number!!")
else:
    for i in range(1, 11):
        print(f"{table_of} x {i} = {table_of*i}")

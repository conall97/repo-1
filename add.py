option = input('enter 1 to add, or 2 to muliply')

if option == "1":
    num1 = input('#1 enter a number: ')
    num2 = input('#2 enter a number: ')
    answer = int(num1) + int(num2)
    print(f"{num1} + {num2} = {answer} ")

if option == "2":
    num1 = input('#1 enter a number: ')
    num2 = input('#2 enter a number: ')
    answer = int(num1) * int(num2)
    print(f"{num1} x {num2} = {answer} ")

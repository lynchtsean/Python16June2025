def add_numbers(current_sum, number):
    return current_sum + number

i = True
total_sum = 0

while i == True:
    number = int(input("Input a number: "))
    total_sum = add_numbers(total_sum, number)
    validation = input("Do you want to enter another number? (Yes/No): ")
    if validation.lower() == "yes":
        continue
    else:
        print("Final Sum:", total_sum)
        print("See Ya!!")
        break


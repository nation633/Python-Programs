#Gets numbers from user then adds, Subtracts and multiplies

user_num1 = float(input("Enter your first number: "))
user_num2 = float(input("Enter your second number: "))
user_num3 = float(input("Enter your Third number: "))

sum_of_all_num = user_num1 + user_num2 + user_num3

sub_num1_num2 = user_num1 - user_num2

mult_num3_num1 = user_num3 * user_num1

sum_of_all_num_div = ((user_num1 + user_num2 + user_num3)/user_num3)


print("The sum of all the numbers: " + str(sum_of_all_num))
print("The first number minus the second number: " + str(sub_num1_num2 ))
print("The third number multiplied by the first number: "+ str(mult_num3_num1))
print("The sum of all three numbers divided by the third number: "+ str(sum_of_all_num_div))
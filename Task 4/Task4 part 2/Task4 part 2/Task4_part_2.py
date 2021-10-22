
#Calculate the price of groceries and average them

#Get the list of products from the user
str_prod1 = input("Enter the name of the product: ")
str_prod2 = input("Enter the name of the product: ")
str_prod3 = input("Enter the name of the product: ")

#Get product prices from user
prod_price1 = float(input("Enter the price of " + str_prod1 + ": "))
prod_price2 = float(input("Enter the price of " + str_prod2 + ": "))
prod_price3 = float(input("Enter the price of " + str_prod3 + ": "))

#Total of all the products listed
float_total = prod_price1 + prod_price2 + prod_price3

#Average price of all products listed
fl_average = ((prod_price1 + prod_price2 + prod_price3)/3)

print("The Total of " + str_prod1 + ", " + str_prod2 + ", " + str_prod3 + " is: " +  "R" + str(float_total) + "and the average price of the items are R" + str(fl_average))

# 10/1/2026

# Use branching and functions to display coin combination

money = float(input("Enter an amount of money: $"))
if money == 0.00:
    print("No change")

# Convert money to an integer
money_int = int(money * 100)

#print(money_int)

#---------------Dollars-----------------

# Determine how many dollars are needed
dollars = money_int // 100

#Remove the dollars from money_int
money_int = money_int  % 100

#print(f"Dollars {dollars}")
#print(f"Leftover: {money_int}")

#---------------Quaters-----------------

# Determine how many quaters are needed
quaters = money_int // 25

#Remove the dollars from money_int
money_int = money_int  % 25

#print(f"Quaters {quaters}")
#print(f"Leftover: {money_int}")

#---------------Dimes-----------------

# Determine how many dimes are needed
dimes = money_int // 10

#Remove the dimes from money_int
money_int = money_int  % 10

#print(f"Dimes {dimes}")
#print(f"Leftover: {money_int}")

#---------------Nickles-----------------

# Determine how many nickles are needed
nickles = money_int // 5

#Remove the dimes from money_int
money_int = money_int  % 5

#print(f"Nickles {nickles}")
#print(f"Leftover: {money_int}")

#---------------Pennies-----------------

# Determine how many pennies are needed
pennies = money_int // 1

#print(f"Pennies {pennies}")
#print(f"Leftover: {money_int}")

# Define a function to show coins only if needed
def show_coins(coin, coin_name):
    if coin > 0: 
        if coin == 1:
            print(f"1 {coin_name}")
        if coin > 1:
            if coin_name == "Penny":
                print(f"{coin} Pennies")
            else:
                print(f"{coin} {coin_name}s")

# Call function for each of the coins
show_coins(dollars, "Dollar")
show_coins(quaters, "Quater")
show_coins(dimes, "Dime")
show_coins(nickles, "Nickel")
show_coins(pennies, "Penny")

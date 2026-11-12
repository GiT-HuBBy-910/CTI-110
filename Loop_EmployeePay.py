# Shawn Kahele
# 10/22/2026
# Use a loop to calculate pay for ALL employees

# Create variables for the total values taht display upon Done
total_employees = 0
total_overtime = 0
total_regular = 0
total_gross = 0

# Request employee information

name = input("Enter employee's name: ")

# Create while loop using name 

while name != "done":

    hoursWorked = float(input("Enter number of hours worked: "))

    payRate = float(input("Enter employee's pay rate: "))

    #evalute overtime

    if hoursWorked > 40 :

        #calculate overtime
        overtimeHours = hoursWorked - 40
        #Calculate overPay
        overPay = overtimeHours * (payRate * 1.5)

        #calculate salary for reg hours

        regPay = 40 * payRate

        # calculate gross pay

        grossPay = regPay + overPay
    else:

        overPay = 0
        overtimeHours = 0

        regPay = hoursWorked * payRate
        grossPay = regPay

    # Display output

    print("-------------------------------------")
    print("Employee name:  ",name,"\n")

    print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<20}{"RegHour Pay":<20}{"Gross Pay"}')
    print('--------------------------------------------------------------------------------------------------')
    print(f'{hoursWorked:<15}{payRate:<12}{overtimeHours:<12}{overPay:<20}{"$"}{regPay:<20.2f}{"$"}{grossPay:.2f}')
    print()
    print()
    # Ask user for the next employee or Done
    name = input("Enter another employee or done to quit: ").lower()
    print()
    
    total_employees = total_employees + 1  
    total_overtime = total_overtime + overPay
    total_regular = total_regular + regPay
    total_gross = total_gross + grossPay

# Loop breaks here. Displaying totals
print(f"Total number of employees entered: {total_employees}")
print(f"Total amount paid for overtime: ${total_overtime:.2f}")
print(f"Total amount paid for regular hours: ${total_regular:.2f}")
print(f"Total amount paid in gross: ${total_gross:.2f}")
print()
print("Thank you for using the employee pay calculator!")

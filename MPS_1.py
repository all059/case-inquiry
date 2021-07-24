import sys

ANNUAL_INTEREST_RATE = .04
NUMBER_OF_MONTHS_IN_A_YEAR = 12

def down_pay_house():
    month = 0    
    current_savings = 0
    ## Variables that are set, should be named better and extracted as constants to the top
    # r = .04
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))

    ## Extract all magic numbers to the top
    portion_down_payment = float(total_cost) * .25
    monthly_salary = float(annual_salary) / NUMBER_OF_MONTHS_IN_A_YEAR
    while current_savings < portion_down_payment:
        month += 1
        current_savings = current_savings + monthly_salary * portion_saved + (current_savings * ANNUAL_INTEREST_RATE / 12)
        # F strings
    print(f"Number of months: " + month)

# def down_pay_with_raise():
#     month = 0    
#     current_savings = 0
#     r = .04
#     annual_salary = float(input("Enter your annual salary: "))
#     portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
#     total_cost = float(input("Enter the cost of your dream home: "))
#     semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
#     portion_down_payment = float(total_cost) * .25
#     monthly_salary = annual_salary / 12
#     while current_savings < portion_down_payment:
#         month += 1
#         current_savings = current_savings + monthly_salary * portion_saved + (current_savings * r / 12)
#         if month % 6 == 0:
#             monthly_salary = monthly_salary * (1 + semi_annual_raise)
#     print("Number of months: " + str(month))

## Part 2

def down_pay_with_raise(annual_salary, portion_saved, total_cost, semi_annual_raise):
    month = 0    
    current_savings = 0
    r = .04
    portion_down_payment = float(total_cost) * .25
    monthly_salary = annual_salary / 12
    while current_savings < portion_down_payment:
        month += 1
        current_savings = current_savings + monthly_salary * portion_saved + (current_savings * r / 12)
        if month % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    print("Number of months: " + str(month))
    return month

def find_amount_2():
    starting_salary = float(input("Enter the starting salary: "))
    steps = 0
    rate_met = False
    binary_value = 10000
    rate_saved = (int(binary_value))/10000
    target = 36 ## 36months to save
    while rate_met == False:
        steps += 1
        number_of_months = down_pay_with_raise(starting_salary, rate_saved, 1000000, .07)
        print(number_of_months)
        if number_of_months < target:
            rate_saved = rate_saved/2
        elif number_of_months > target:
            rate_saved += (rate_saved*0.5)
        else:
            rate_met = True
    print("Best savings rate: " + str(((rate_saved*10000)//1)/10000))
    print("Steps in bisection search: " + str(steps))



def find_amount():
    rate_met = False
    semi_annual_raise = .07
    r = .04
    #25% of 1 million
    down_pay_cost = 250000
    months = 36
    right_value = 10000
    left_value = 0
    binary_value = right_value - left_value
    steps = 0
    starting_salary = float(input("Enter the starting salary: "))
    while rate_met == False:
        monthly_salary = starting_salary / 12
        total_saved = 0
        steps += 1
        rate_saved = (int(binary_value))/10000
        print(rate_saved)
        for i in range(months):
            total_saved = total_saved + monthly_salary * rate_saved + (total_saved*r/12)
            if (i+1) % 6 == 0:
                monthly_salary = monthly_salary * (1 + semi_annual_raise)
        if rate_saved == 1 and total_saved < down_pay_cost:
            print("It is not possible to pay the down payment in three years.")
            break
        if abs(total_saved - down_pay_cost) <= 100:
            print("Best savings rate: " + str(rate_saved))
            print("Steps in bisection search: " + str(steps))
            rate_met = True

        ## 0, 100 -> 50 2. -> 50 ->  right = .25 -> .125 -> left = .125 
        if (total_saved - down_pay_cost) > 100:
            right_value = binary_value
            binary_value = (right_value + left_value) / 2

        if (total_saved - down_pay_cost) < 100:
            left_value = binary_value
            binary_value = (right_value + left_value) / 2
        
        print(left_value, right_value)


# down_pay_house()
# down_pay_with_raise()
# find_amount()

## if name  == sys.argv[0]
if __name__ == "__main__":
                 
    ## python [ MPS_1.py,  {1,2,3} ]
    programNumber = sys.argv[1]

    if programNumber == "1":
        down_pay_house()
    elif programNumber == "2":

        annual_salary = float(input("Enter your annual salary: "))
        portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
        total_cost = float(input("Enter the cost of your dream home: "))
        semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

        down_pay_with_raise(annual_salary, portion_saved, total_cost, semi_annual_raise)
    elif programNumber == "3":
        find_amount()
    elif programNumber == "4":
        find_amount_2()
    else:
        print("You fucked up the input.")
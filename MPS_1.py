def down_pay_house():
    month = 0    
    current_savings = 0
    r = .04
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    portion_down_payment = float(total_cost) * .25
    monthly_salary = float(annual_salary)/12
    while current_savings < portion_down_payment:
        month+= 1
        current_savings = current_savings + monthly_salary*portion_saved + (current_savings*r/12)
    print("Number of months: " + str(month))

def down_pay_with_raise():
    month = 0    
    current_savings = 0
    r = .04
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
    portion_down_payment = float(total_cost) * .25
    monthly_salary = annual_salary/12
    while current_savings < portion_down_payment:
        month+= 1
        current_savings = current_savings + monthly_salary*portion_saved + (current_savings*r/12)
        if month % 6 == 0:
            monthly_salary = monthly_salary * (1 + semi_annual_raise)
    print("Number of months: " + str(month))

def find_amount():
    rate_met = False
    semi_annual_raise = .07
    r = .04
    #25% of 1 million
    down_pay_cost = 250000
    months = 36
    binary_value = 10000
    rate = 0
    steps = 0
    starting_salary = float(input("Enter the starting salary: "))
    while rate_met == False:
        monthly_salary = starting_salary/12
        total_saved = 0
        steps+= 1
        rate_saved = (int(binary_value))/10000
        for i in range(months):
            total_saved = total_saved + monthly_salary*rate_saved + (total_saved*r/12)
            if (i+1) % 6 == 0:
                monthly_salary = monthly_salary * (1 + semi_annual_raise)
        if rate_saved == 1 and total_saved < down_pay_cost:
            print("It is not possible to pay the down payment in three years.")
            break
        if abs(total_saved - down_pay_cost) <= 100:
            rate = rate_saved
            print("Best savings rate: " + str(rate))
            print("Steps in bisection search: " + str(steps))
            rate_met = True
        if (total_saved - down_pay_cost) > 100:
            binary_value = binary_value/2
        if (total_saved - down_pay_cost) < 100:
            binary_value += (binary_value*0.5)
       

# down_pay_house()
down_pay_with_raise()
# find_amount()

# if __name__ == "__main__":
import Tax_calculator as Tc

while True:
    name = str(input("enter your name: \n"))
    try:
        age = int(input("enter your age: \n"))
        gross_pay = int(input("enter your pay: \n"))
        net_pay = Tc.total_calc_tax(gross_pay, age)
        print(name, "Your take away home salary ,", net_pay)
    except ValueError:
        print("Invalid Data")
    except KeyboardInterrupt:
        print("The program was stopped by the user")
        exit()


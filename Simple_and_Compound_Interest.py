def simple_and_compound_interest(principle,rate,time):
    SI = float((principle * rate * time)/100)
    CI = float(principle*(1+rate/100)**time)
    return SI,CI
    

principle = int(input("Enter you Principle : "))
rate = float(input("Enter rate : "))
time = float(input("Enter the time in year; "))
SIMP_INT,COMP_INT = simple_and_compound_interest(principle,rate,time)
print(f"The simple interest is {SIMP_INT} And COMPOUND INTEREST IS {COMP_INT}")

welc = '''''Welcome 
lets calculate your BMI'''
print(welc)
num1 = float(input("Enter your weight in kilograms: "))
num2 = float(input("Enter your height in meters: "))
if num1 > 0 and num2 > 0:
    result = num1/(num2**2)
else:
    result = " ERROR!!"
print(f"Your BMI is: {result}")
if result < 18.5:
    print(f"You are Underweight with a BMI of {result}")
elif result < 24.9:
    print(f"You have normal weight with a BMI of {result}")
elif result  < 29.9:
    print(f"You are Overweightwith a BMI of {result}")
elif result < 34.9:
    print(f"You have obesity class 1 with a BMI of {result}")
elif result < 39.9:
    print(f"You have Obesuty class 2 with a BMI of {result}" )
elif result > 40:
    print(f"You have Obesity class 3 with a BMI of {result}")
else:
    print("Try Again")
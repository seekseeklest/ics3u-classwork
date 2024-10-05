height = float(input("What is your height? (m) "))
weight = float(input("What is your weight? (kg) "))
bmi = weight / (height ** 2)

print(f"your BMI is {bmi}.")
if bmi < 15.0: 
    print("you are very severely underweight.")
elif bmi >= 15.0 and bmi <= 16.0:
    print("you are severely underweight.")
elif bmi > 16.0 and bmi <= 18.4:
    print("you are underweight.")
elif bmi > 18.4 and bmi <= 24.9:
    print("you are normal weight.")
elif bmi > 24.9 and bmi <= 25.9:
    print("you are overweight.")
elif bmi > 25.9 and bmi <= 34.9:
    print("you are moderately obese.")
elif bmi > 34.9 and bmi <= 39.9:
    print("you are severely obese.")
else:
    print("you are morbidly obese.")
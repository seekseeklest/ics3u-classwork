height = float(input("What is your height? (m) "))
weight = float(input("What is your weight? (kg) "))
bmi = weight / height ** 2

print(f"your BMI is {bmi}.")
if bmi < 18.5:
    print("you are underweight.")
elif bmi >= 18.5 and bmi <= 24.9:
    print("you are normal weight.")
elif bmi > 24.9 and bmi <= 25.9:
    print("you are overweight.")
else:
    print("you are obese.")
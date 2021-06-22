# BMI calculator
print("This program is to calculate your BMI\n")
name = input("Enter your name: ")
weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height ** 2 )

if bmi < 25:
    print(f"{name} is underweight by {bmi} BMI")

else:
    print(f"{name} is underweight by {bmi} BMI")


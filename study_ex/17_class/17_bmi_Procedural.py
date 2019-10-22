weight = float(input("Enter weight in Kg"))
height = float(input("Enter height in cm"))


bmi = weight / pow(height * 0.01, 2)

print("BMI is", format(bmi, ".2f"))

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

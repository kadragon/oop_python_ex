def get_bmi(name, weight, height):
    bmi = weight / pow(height * 0.01, 2)

    print("BMI is", format(bmi, ".2f"))

    print(name, "is", end=' ')
    
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")


name = input("Enter Name: ")
weight = float(input("Enter weight in Kg: "))
height = float(input("Enter height in cm: "))

get_bmi(name, weight, height)
#Calcualar el BMI - FORMULA: BMI = WHEIGHT / HEIGHT **2

heightlab = input("Inserta la altura en m: ")
weightlab = input("Inserta el peso en kg: ")

height = float(heightlab)
weight = int(weightlab)

bmi = weight / height ** 2

print(int(bmi))
print("lets calculate body mass index")
weight=input("what is your weight")
print("weight= ",weight)
height=input("what is your height")
print("height= ",height)
print("BMI = weight(kg)/height^2(m)  ")
weight=float(weight)
height=float(height)
BMI=weight/(height)**2
BMI=float(BMI)
print("BMI = ",BMI)
if BMI<=18.0:
    print("my name is naveed  and my BMI is =",BMI,"i am underweight")
if BMI>18.0 and BMI<24.0:
    print("my name is Amir  and my BMI is =",BMI,"i am normal weight")
if BMI>24.0:
    print("my name is naveed  and my BMI is =",BMI,"i am over weight") 
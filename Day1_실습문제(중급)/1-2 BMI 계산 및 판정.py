weight = 70  # kg
height = 1.75  # m

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"BMI: {BMI:.2f} - 저체중")

elif 18.5 <= BMI <  23:
    print(f"BMI: {BMI:.2f} - 정상체중")

elif 23 <= BMI < 25:
    print(f"BMI: {BMI:.2f} - 과체중")

elif 25 <= BMI:
    print(f"BMI: {BMI:.2f} - 비만")
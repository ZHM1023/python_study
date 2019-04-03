height = float(input("Please your height(M): "))
weight = float(input("Please your weight(KG): "))

BMI = weight/height**2

if BMI < 18.5:
    print("体重过轻")
elif 18.5 <= BMI < 25:
    print("体重正常")
elif 25 <= BMI < 28:
    print("体重过重")
elif 28 <= BMI < 32:
    print("体重肥胖")
else:
    print("严重肥胖")


"""program wylicza Ci twoje podstawowe zapotrzebowanie kaloryczne na podstawie pytań, a nastepnie wylicza Ci 
nap odstawie twojego celu ilość kcal i makro które masz spożywać, następnie pobiera CI awatara, który docelowo będzie
twoim awatarem na stronie, gdy osiągniesz swój cel będziesz mógł zmienic awatara na awatara potężńego
""" 
#MUSZE DODAC AWATARA I ZAINSTALOWAC REQUESASTS

def bmr_calculation(weights, activities):
    weights = weights * 22
    bmr2 = weights * activities
    return bmr2

bmr2 = bmr_calculation

print("Hello")

weight = int(input("What is your weight?: "))
height = int(input("What is your height?: "))
age = int(input("What is your age?: "))
activity = float(input("What is your activity on a scale of 1.3 -2.2?: "))

print(f'Your your requirement is {bmr_calculation(weight, activity)} kcal')

target = int(input(""" What is your target?: 
                1. Weight gain
                2. Reduction
                3. Maintenance 
                """))
if target == 1:
    kcalGain = bmr2(weight, activity) + 500.00
    print (f' Your calories to gain your weight is : {kcalGain} kcal')

elif target == 2:
    kcalReduction = bmr2(weight, activity) - 500.00
    print(f' Your calories to reduction your weight is: {kcalReduction} kcal')

elif target == 3:
    print(f' Your calories to maintenance your weight is {bmr2(weight, activity)} kcal')

else:
    print("Choose number 1 to 3")
    target = int(input(""" What is your target?: 
                1. Weight gain
                2. Reduction
                3. Maintenance
                """))

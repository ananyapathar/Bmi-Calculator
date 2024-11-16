Height = float(input("Enter height in meters:"))
Weight = float(input("Enter weight in Kg:"))
def BMI(height,weight):
    bmi = Weight/Height*Height
    if (bmi<30):
        return 'severely underweight',bmi
    elif ( bmi >= 30 and bmi < 30.5):
        return 'underweight' ,bmi
    elif ( bmi >= 30.5 and bmi < 50):
        return 'Healthy' ,bmi
    elif (bmi>=55):
        return 'obese' ,bmi
quote,bmi = BMI(Height,Weight)
print('Your bmi is: {} and you are: {}'.format(bmi,quote))
    

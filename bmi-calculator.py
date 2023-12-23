#initial statement is blow
print("Hi, I am a BMI calculator. Do you want to calculate your BMI ")
#then get the prompt from the user 
weight = float(input("Please write your weight in kg: "))
#then get the height from the user
height = float(input("And what is your height in meter: "))
#write the formula to calculate the BMI
bmi = weight/(height*height)
#write the code to make a decision wheather healthy or weak
if bmi<18:
       print(f"your are weak and your BMI is {bmi:.2f}")

elif bmi>=18 and bmi<=24:
        print(f"you are healthy and your BMI is {bmi:.2f}")
else:
    print(f"you are obese and your BMI is {bmi:.2f}")

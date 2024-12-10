def calculate_bmi():
    height = float(input("Enter your height in cm: ")) / 100  
    weight = float(input("Enter your weight in kg: "))
    bmi = weight / (height ** 2)
    print(f"Your Body Mass Index is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You are healthy.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
if __name__ == "__main__":
    calculate_bmi()

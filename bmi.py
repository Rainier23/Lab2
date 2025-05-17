
def calculate_bmi(height, weight):
    # Convert inputs to float
    height = float(height)
    weight = float(weight)

    # Print input values
    print("Height =", height)
    print("Weight =", weight)

    # Calculate BMI
    bmi = weight / (height ** 2)    
    print("BMI =", round(bmi, 2))

    # Conditional classification
    if bmi < 18.5:
        print("Category: Underweight")
        return -1
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
        return 0
    elif bmi > 25:
        print("Category: Overweight")
        return 1
    
# Call the function
calculate_bmi(weight=57, height=1.73)

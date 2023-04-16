height = float(input("Height: "))
weight = int(input("Weight: "))

bmi = weight / height ** 2

if height > 2.5:
    raise ValueError("Human height should not be over 2.5 meters.")

print(round(bmi, 2))

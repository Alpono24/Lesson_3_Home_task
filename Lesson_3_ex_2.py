print("Lesson 3. Home task №2.")
"""
Дан прямоугольный треугольник с катетами cat_a и cat_b. Найти площадь треугольника и его гипотенузу.
"""
cat_a = float(input("Enter the first side of the right triangle cat_a in meters: "))
cat_b = float(input("Enter the second side of the right triangle cat_b in meters: "))
print("You have entered the following sides of the right triangle: cat_a =", cat_a, "m, cat_b =", cat_b, "m;")
print("")
print("The area of the right triangle is: ", (cat_a * cat_b) / 2, "m^2;")
print("The hypotenuse of the right triangle is: ", round((cat_a ** 2 + cat_b ** 2) ** (1 / 2), 2), "m;")

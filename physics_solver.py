print("PHYSICS FORMULA SOLVER")
print("1. Speed")
print("2. Force")
print("3. Kinetic Energy")

choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    d = float(input("Enter distance (m): "))
    t = float(input("Enter time (s): "))
    print("Speed =", d / t, "m/s")

elif choice == 2:
    m = float(input("Enter mass (kg): "))
    a = float(input("Enter acceleration (m/s²): "))
    print("Force =", m * a, "N")

elif choice == 3:
    m = float(input("Enter mass (kg): "))
    v = float(input("Enter velocity (m/s): "))
    print("Kinetic Energy =", 0.5 * m * v * v, "J")

else:
    print("Invalid choice")

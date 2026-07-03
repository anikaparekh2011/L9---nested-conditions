energy = int(input("Please enter how much energy units you have used: "))

if energy <= 50:
    amount = 50 * 2.60
    tax = 25
elif energy <= 100:
    amount = 130 + (energy - 50) * 3.25
    tax = 35
elif energy <= 200:
    amount = 130 + 162.5 + (energy - 100) * 5.26
    tax = 45
else:
    energy > 200
    amount = 130 + 162.5 + 526 + (energy - 200) * 8.45
    tax = 75
total = amount + tax
print("total energy costs: ", total)


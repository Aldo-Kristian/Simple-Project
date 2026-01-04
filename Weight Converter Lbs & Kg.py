def integer_checker(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("PERINGATAN: Input harus bilangan bulat. Coba lagi.")


weight = integer_checker("Weight: ")

while True:
    unit = input("Whats your weight type. (L) For Lbs, and (K) For Kg: ")

    if unit.upper() == "L":
        converted = weight * 0.45359237
        print(f"You are {converted} kilograms")
    elif unit.upper() == "K":
        converted = weight / 0.45359237
        print(f"You are {converted} pounds")
    else:
        print("Your input is incorrect")
        continue

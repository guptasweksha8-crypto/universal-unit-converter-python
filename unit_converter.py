def convert_length(value, from_unit, to_unit):
    factors = {
        "m": 1.0,
        "km": 1000.0,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.344,
        "ft": 0.3048,
        "in": 0.0254,
        "yd": 0.9144,
    }
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported length unit")
    return value * factors[from_unit] / factors[to_unit]


def convert_weight(value, from_unit, to_unit):
    factors = {
        "kg": 1.0,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.45359237,
        "oz": 0.028349523125,
    }
    if from_unit not in factors or to_unit not in factors:
        raise ValueError("Unsupported weight unit")
    return value * factors[from_unit] / factors[to_unit]


def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        raise ValueError("Unsupported temperature unit")

    if to_unit == "C":
        return celsius
    if to_unit == "F":
        return celsius * 9 / 5 + 32
    if to_unit == "K":
        return celsius + 273.15
    raise ValueError("Unsupported temperature unit")


def main():
    print("Unit Converter")
    print("Categories: 1) Length  2) Weight  3) Temperature")

    while True:
        choice = input("Choose a category (1/2/3) or q to quit: ").strip().lower()
        if choice == "q":
            print("Goodbye!")
            break

        if choice == "1":
            category = "length"
            units = ["m", "km", "cm", "mm", "mi", "ft", "in", "yd"]
        elif choice == "2":
            category = "weight"
            units = ["kg", "g", "mg", "lb", "oz"]
        elif choice == "3":
            category = "temperature"
            units = ["C", "F", "K"]
        else:
            print("Invalid choice")
            continue

        try:
            value = float(input("Enter the value: "))
            from_unit = input(f"Enter the source unit ({'/'.join(units)}): ").strip()
            to_unit = input(f"Enter the target unit ({'/'.join(units)}): ").strip()

            if category == "length":
                result = convert_length(value, from_unit, to_unit)
            elif category == "weight":
                result = convert_weight(value, from_unit, to_unit)
            else:
                result = convert_temperature(value, from_unit, to_unit)

            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Convert again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

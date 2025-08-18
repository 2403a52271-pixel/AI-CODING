def convert_temperature():
    """
    Converts temperature between Celsius and Fahrenheit with clear instructions.
    Prompts the user to select the conversion direction and enter the temperature.
    Handles invalid input gracefully.
    """
    print("=== Temperature Converter ===")
    print("This tool converts temperatures between Celsius and Fahrenheit.")
    print("Please choose the conversion direction:")
    print("  1. Celsius to Fahrenheit")
    print("  2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        temp_str = input("Enter temperature in Celsius: ").strip()
        try:
            celsius = float(temp_str)
            fahrenheit = celsius * 9 / 5 + 32
            print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for temperature.")
    elif choice == "2":
        temp_str = input("Enter temperature in Fahrenheit: ").strip()
        try:
            fahrenheit = float(temp_str)
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for temperature.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    while True:
        convert_temperature()
        again = input("Do you want to convert another temperature? (y/n): ").strip().lower()
        if again != "y":
            print("Thank you for using the Temperature Converter. Goodbye!")
            break


def weather_app():
    while True:
        weather = input("How does the weather look today?? ").strip().lower()

        if weather == "hot":
            print("Stay cool and drink plenty of water.\n")
        elif weather == "cold":
            print("Keep warm and wear a jacket.\n")
        elif weather == "rainy":
            print("Don't forget your umbrella.\n")
        else:
            print("Sorry, didn’t get you. Please try again.\n")
            continue

        again = input("Would you like to check the weather again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break

weather_app()
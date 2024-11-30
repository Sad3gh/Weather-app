from weather import Weather
from user import User


def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    weather = Weather(api_key)

    user_name = input("Enter your name: ")
    user = User(user_name)

    while True:
        print("\n--- Weather App ---")
        print("1. Get current weather")
        print("2. Get weather forecast")
        print("3. Add favorite location")
        print("4. Remove favorite location")
        print("5. View favorites")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            city = input("Enter city name: ")
            current_weather = weather.get_current_weather(city)
            if current_weather:
                print(
                    f"Current weather in {city}: {current_weather['weather'][0]['description']}, {current_weather['main']['temp']}°C")
            else:
                print("City not found.")

        elif choice == '2':
            city = input("Enter city name: ")
            forecast = weather.get_forecast(city)
            if forecast:
                print(f"Weather forecast for {city}:")
                for item in forecast['list'][:5]:  # Displaying first 5 items
                    print(f"{item['dt_txt']}: {item['weather'][0]['description']}, {item['main']['temp']}°C")
            else:
                print("City not found.")

        elif choice == '3':
            city = input("Enter city name to add to favorites: ")
            user.add_favorite(city)

        elif choice == '4':
            city = input("Enter city name to remove from favorites: ")
            user.remove_favorite(city)

        elif choice == '5':
            print("Favorite locations:", user.favorites)

        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 6.")


if __name__ == "__main__":
    main()

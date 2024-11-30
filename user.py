class User:
    def __init__(self, name):
        self.name = name
        self.favorites = []

    def add_favorite(self, city):
        if city not in self.favorites:
            self.favorites.append(city)
            print(f"{city} added to favorites.")
        else:
            print(f"{city} is already in favorites.")

    def remove_favorite(self, city):
        if city in self.favorites:
            self.favorites.remove(city)
            print(f"{city} removed from favorites.")
        else:
            print(f"{city} not found in favorites.")
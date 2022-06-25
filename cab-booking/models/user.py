

class User:

    def __init__(self, name):
        self.name = name
        self.trips = []

    def add_trip(self, trip):
        self.trips.append(trip)

    def get_ratings(self):
        return [t.customer_rating for t in self.trips]

    def get_avg_rating(self):
        try:
            return sum(self.get_ratings())/(len(self.get_ratings()))
        except Exception as e:
            return 0

    def print_details(self):
        print(f"{self.name} rating is {self.get_avg_rating()}")

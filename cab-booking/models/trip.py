

class Trip:
    trip_id = 1
    def __init__(self, customer, driver, customer_rating, driver_rating):
        self.trip_id = Trip.trip_id
        self.customer = customer
        self.driver = driver
        self.customer_rating = customer_rating
        self.driver_rating = driver_rating
        Trip.trip_id += 1

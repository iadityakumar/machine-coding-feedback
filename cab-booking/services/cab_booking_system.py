
from services.customer_service import CustomerService
from services.driver_service import DriverService
from services.rating_based_stragedy_service import RatingBasedStragedyService
from models.driver import Driver
from models.customer import Customer
from models.trip import Trip

class CabBookingSystem:

    # obj = None
    def __init__(self):
        # if not CabBookingSystem.obj:
        #     CabBookingSystem.obj = self
        # return CabBookingSystem.obj
        self.customers = []
        self.drivers = []
        self.trips = []
        self.stragedy = RatingBasedStragedyService()


    def add_customer(self, customer_name):
        if not CustomerService.get_customer(self.customers, customer_name):
            self.customers.append(Customer(customer_name))

    def add_driver(self, driver_name):
        if not DriverService.get_driver(self.drivers, driver_name):
            self.drivers.append(Driver(driver_name))


    def seed_data(self, trips=[]):
        for t in trips:
            self.add_customer(t['customer_name'])
            self.add_driver(t['driver_name'])
        for t in trips:
            customer = CustomerService.get_customer(self.customers, t['customer_name'])
            driver = DriverService.get_driver(self.drivers, t['driver_name'])
            trip = Trip(customer, driver, t['customer_rating'], t['driver_rating'])
            self.trips.append(Trip)
            customer.add_trip(trip)
            driver.add_trip(trip)


    def set_values(self, customers=[], drivers=[], trips=[]):
        self.customers = customers
        self.drivers = drivers
        self.trips = trips

    def set_stragedy(self, stragedy=RatingBasedStragedyService):
        self.stragedy = stragedy


    def get_driver(self, customer_name):
        customer = CustomerService.get_customer(self.customers, customer_name)
        return self.stragedy.get_cabs(customer, self.trips, self.drivers)


    def print_matching_drivers(self, customer_name):
        drivers = self.get_driver(customer_name)
        print(f"Matched drivers for {customer_name}: ")
        for d in drivers:
            d.print_details()

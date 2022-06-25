from services.cab_booking_system import CabBookingSystem
from services.driver_service import DriverService
from constants import INACTIVE

if __name__ == '__main__':
    cabBookingSystem = CabBookingSystem()
    seed_trips = [{
        'driver_name': 'd1',
        'customer_name': 'c1',
        'driver_rating': 4,
        'customer_rating': 5
    },{
        'driver_name': 'd2',
        'customer_name': 'c2',
        'driver_rating': 5,
        'customer_rating': 4
    },{
        'driver_name': 'd3',
        'customer_name': 'c3',
        'driver_rating': 3,
        'customer_rating': 1
    },{
        'driver_name': 'd4',
        'customer_name': 'c4',
        'driver_rating': 2,
        'customer_rating': 4
    }
    ]

    cabBookingSystem.seed_data(seed_trips)

    # finding driver for c3
    cabBookingSystem.print_matching_drivers('c3')

    d1 = DriverService.get_driver(cabBookingSystem.drivers, 'd1')
    d1.set_status(INACTIVE)
    print('Devativated d1 driver \n ')
    cabBookingSystem.print_matching_drivers('c3')

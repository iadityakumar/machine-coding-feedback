
from services.stragedy_service import StragedyService
from services.customer_service import CustomerService


class RatingBasedStragedyService(StragedyService):



    def get_cabs(self, customer, trips, cabs):
        # breakpoint()
        cabs = sorted(cabs, key = lambda x: -x.get_avg_rating())
        cabs = [c for c in cabs if c.get_avg_rating() > 1 and c.get_avg_rating() > customer.get_avg_rating() and not c.is_inactive()]
        customer.print_details
        # breakpoint()
        if not cabs:

            customer_trips = CustomerService.get_customer_trips(customer, trips)
            cabs = sorted([trip.driver for trip in customer_trips], key = lambda x: -x.get_avg_rating())
        cabs = [c for c in cabs if not c.is_inactive()]
        return cabs

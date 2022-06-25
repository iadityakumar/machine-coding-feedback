

class TripService:


    @classmethod
    def get_trip(self, trips, id):
        for trip in trips:
            if trip.id == id:
                return trip

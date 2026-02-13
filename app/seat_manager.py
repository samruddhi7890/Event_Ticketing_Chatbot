class SeatManager:
    def __init__(self):
        self.seats = {
            f"R{row}S{seat}": "available"
            for row in range(1, 11)
            for seat in range(1, 21)
        }

        self.ticket_owners = {}

    def get_available_seats(self):
        return [seat for seat, status in self.seats.items() if status == "available"]

    def book_seats(self, seat_list, user="Guest"):
        for seat in seat_list:
            if self.seats.get(seat) == "available":
                self.seats[seat] = "booked"
                self.ticket_owners[seat] = user
            else:
                raise Exception(f"{seat} not available")
        return True

    def transfer_ticket(self, from_user, to_user, seat):
        if self.ticket_owners.get(seat) == from_user:
            self.ticket_owners[seat] = to_user
            return f"Ticket for {seat} transferred to {to_user}"
        return "Transfer failed. Ownership mismatch."

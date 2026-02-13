def optimize_group_seating(available_seats, group_size):

    seat_map = {}

    for seat in available_seats:
        row = seat.split("S")[0]
        if row not in seat_map:
            seat_map[row] = []
        seat_map[row].append(seat)

    for row, seats in seat_map.items():
        seats_sorted = sorted(seats, key=lambda x: int(x.split("S")[1]))

        for i in range(len(seats_sorted) - group_size + 1):
            group = seats_sorted[i:i+group_size]
            seat_numbers = [int(s.split("S")[1]) for s in group]

            if max(seat_numbers) - min(seat_numbers) == group_size - 1:
                return group

    return []

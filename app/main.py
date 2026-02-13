from fastapi import FastAPI
from app.seat_manager import SeatManager
from app.pricing import calculate_price
from app.ticketing_platforms import fetch_events_from_eventbrite, fetch_events_from_ticketmaster
from app.group_booking import optimize_group_seating

app = FastAPI()
seat_manager = SeatManager()

@app.get("/")
def home():
    return {"message": "Ticket Sales Bot Running"}

@app.get("/events")
def get_events():
    events = fetch_events_from_eventbrite() + fetch_events_from_ticketmaster()
    return {"events": events}

@app.get("/available-seats")
def available_seats():
    return seat_manager.get_available_seats()

@app.post("/book")
def book(seats: list[str], base_price: float, demand_factor: float):

    seat_manager.book_seats(seats)

    total_price = calculate_price(base_price, demand_factor, len(seats))

    return {
        "status": "success",
        "total_price": total_price
    }

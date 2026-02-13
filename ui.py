import streamlit as st
import datetime

from app.seat_manager import SeatManager
from app.pricing import calculate_price
from app.ticketing_platforms import (
    fetch_events_from_eventbrite,
    fetch_events_from_ticketmaster,
)
from app.group_booking import optimize_group_seating
from app.recommendations import recommend_events
from app.groq_client import call_groq


st.set_page_config(page_title="EventGPT", layout="wide")
st.title("🎟 Event Ticketing Chatbot")


# =============================
# Session Setup
# =============================
if "seat_manager" not in st.session_state:
    st.session_state.seat_manager = SeatManager()

if "visits" not in st.session_state:
    st.session_state.visits = 0

if "purchases" not in st.session_state:
    st.session_state.purchases = 0

st.session_state.visits += 1
seat_manager = st.session_state.seat_manager


# =============================
# Fetch Events
# =============================
events = fetch_events_from_eventbrite() + fetch_events_from_ticketmaster()

# Default event (still using dropdown)
event_names = [event["name"] for event in events]
selected_event = st.selectbox("📅 Choose Event", event_names)

selected_event_data = next(e for e in events if e["name"] == selected_event)


# ✅ DYNAMIC VALUES FROM DATASET
event_date = selected_event_data.get("date", "Not specified")
event_venue = selected_event_data.get("venue", "Not specified")


# =============================
# 🎫 Event Overview
# =============================
st.markdown("### 🎭 Event Details")
st.info(
    f"""
**Event:** {selected_event_data['name']}  
**Date:** {event_date}  
**Venue:** {event_venue}
"""
)


# =============================
# Main Layout Columns
# =============================
col1, col2 = st.columns([1.2, 1])

# =============================
# 🪑 LEFT COLUMN → Seats & Booking
# =============================
with col1:

    st.markdown("## 🪑 Seat Selection")

    # Smart Group Booking
    st.markdown("### 👥 Smart Group Booking")
    group_size_input = st.number_input("Group Size", 1, 10, 1)

    if st.button("Find Best Seats"):
        best_group = optimize_group_seating(
            seat_manager.get_available_seats(),
            group_size_input
        )
        if best_group:
            st.success(f"Recommended Seats: {best_group}")
        else:
            st.error("No contiguous seats found")

    # Seat Multiselect
    available_seats = seat_manager.get_available_seats()
    selected_seats = st.multiselect("Select Seats", available_seats[:100])

    # Pricing
    st.markdown("### 💰 Pricing")
    demand_factor = st.slider("Demand Level", 1.0, 2.0, 1.2)

    if selected_seats:
        total_price = calculate_price(
            selected_event_data["base_price"],
            demand_factor,
            len(selected_seats)
        )

        st.metric("Total Price", f"₹{total_price}")

        if len(selected_seats) >= 5:
            st.success("🎉 Group Discount Applied")

    # Booking
    if st.button("🎫 Confirm Booking"):
        if selected_seats:
            seat_manager.book_seats(selected_seats, user="Guest")
            st.session_state.purchases += 1
            st.success("Booking Successful 🎉")
            st.balloons()
        else:
            st.error("Select seats first")


# =============================
# 🤖 RIGHT COLUMN → AI Features
# =============================
with col2:

    st.markdown("## 🤖 AI Assistant")

    # AI Recommendations
    st.markdown("### 🎯 AI Recommendations")
    user_interest = st.text_input("What are you interested in?")

    if st.button("Get Recommendations"):
        recommendation = recommend_events(user_interest, events)
        st.write(recommendation)

    st.divider()

    # Chatbot
    st.markdown("### 💬 Ticketing Chatbot")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_msg = st.text_input("Ask anything about events...")

    if st.button("Send"):

        prompt = f"""
        You are an event assistant chatbot.

        Available events:
        {events}

        User question:
        {user_msg}

        Answer helpfully.
        """

        response = call_groq(prompt)
        bot_reply = response["choices"][0]["message"]["content"]

        st.session_state.chat_history.append(("You", user_msg))
        st.session_state.chat_history.append(("Bot", bot_reply))

    for sender, msg in st.session_state.chat_history:
        st.write(f"**{sender}:** {msg}")


# =============================
# 🔄 Ticket Transfer
# =============================
st.divider()
st.markdown("## 🔄 Ticket Transfer")

from_user = st.text_input("From")
to_user = st.text_input("To")
seat_transfer = st.text_input("Seat ID")

if st.button("Transfer Ticket"):
    msg = seat_manager.transfer_ticket(from_user, to_user, seat_transfer)
    st.write(msg)


# =============================
# ⏰ Event Reminder
# =============================
st.divider()
st.markdown("## ⏰ Event Reminder")

reminder_email = st.text_input("Reminder Email")
reminder_date = st.date_input("Event Date")

if st.button("Set Reminder"):
    st.success(f"Reminder set for {reminder_date} to {reminder_email}")


# =============================
# 📊 Conversion Rate
# =============================
if st.session_state.visits > 0:
    conversion = (st.session_state.purchases / st.session_state.visits) * 100
    st.sidebar.metric("Conversion Rate", f"{round(conversion, 2)}%")

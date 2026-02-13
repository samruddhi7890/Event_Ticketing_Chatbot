# Event-Ticketing-Chatbot (EventGPT)

EventGPT is an **AI-powered ticket booking and event assistance application** built using **Streamlit**, **FastAPI**, and the **Groq LLM API**.

The system simulates a modern ticketing platform featuring:

- Intelligent event recommendations
- Conversational AI support
- Dynamic pricing
- Smart seat selection
- Group booking optimization

---

## Key Features

### Ticket Booking

- Event selection
- Multi-seat booking
- Real-time pricing calculation
- Demand-based dynamic pricing

### Seat Selection

- Displays available seats
- Prevents double booking
- Interactive seat choice

### Smart Group Booking

- Automatically finds contiguous seats
- Optimized seating for groups

### AI Event Recommendations

- Suggests events based on user interest
- Supports categories like:
  - Music
  - Comedy
  - Tech
  - Sports
  - Festivals
  - Workshops
  - Business Events

### AI Chatbot (Groq Powered)

- Answers event-related queries
- Context-aware responses
- Natural language interaction

### Ticket Transfer

- Simulated ticket ownership transfer

### Event Reminder

- Reminder scheduling interface

### Dynamic Pricing

- Demand factor simulation
- Seat-based price scaling
- Group discount logic

---

## Tech Stack

**Frontend:** Streamlit  
**Backend:** FastAPI  
**AI Engine:** Groq LLM API  
**Language:** Python  
**Data Storage:** JSON Dataset  
**Seat Logic:** Custom SeatManager

---

## Project Structure

## Project Structure

```
EventGPT/
│
├── streamlit_app.py        # Streamlit frontend
├── requirements.txt
├── .env
│
├── app/
│   ├── main.py             # FastAPI backend
│   ├── seat_manager.py
│   ├── pricing.py
│   ├── group_booking.py
│   ├── recommendations.py
│   ├── groq_client.py
│   └── ticketing_platforms.py
│
└── data/
    └── events.json         # Event dataset
```

---

```
## ⚙ Setup Instructions

### 1. Clone the Repository


git clone https://github.com/username/EventGPT.git
cd EventGPT


2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key
MODEL_NAME=llama-3.3-70b-versatile

4. Run the Application
streamlit run streamlit_app.py

---
```

## AI Capabilities

EventGPT leverages the Groq LLM API to deliver:

- Conversational Chatbot  
  Provides natural, context-aware responses to user queries

- Intelligent Recommendations  
  Suggests events based on user interests and input

- Natural Language Understanding  
  Interprets flexible user requests (e.g., "comedy show", "tech events")

---

## Simulated Benefits

- Faster ticket discovery
- Improved seat selection experience
- Smarter group booking
- Enhanced AI-driven interaction
- Reduced manual search effort

---

## Future Enhancements

- Real Eventbrite / Ticketmaster API integration
- Persistent database (PostgreSQL / MongoDB)
- Payment gateway integration
- User authentication and profiles
- Seat heatmap visualization
- Admin dashboard
- Analytics and reporting

---

## Developed By

Samruddhi Kadre

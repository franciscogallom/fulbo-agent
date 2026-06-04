from langchain.tools import tool

@tool
def create_booking(date: str, time: str, customer_name: str) -> str:
    """
    Create a football court booking for a specific day and start time.

    Use this when the user wants to reserve, book, schedule, or confirm a slot
    (e.g. "I want to book today at 8pm", "reservar mañana a las 19").

    Args:
        date: Day for the booking: "today", "tomorrow", or YYYY-MM-DD.
        time: Start time in 24h form, e.g. "20:00", "20", or "20hs".
        customer_name: Full name of the person booking (required).
    """
    
    return "Reserva confirmada"
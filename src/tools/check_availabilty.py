from langchain.tools import tool

@tool
def check_availability(date: str) -> str:
    """
    Check which football court time slots are still available on a given day.

    Use this when the user asks about free slots, availability, open bookings,
    or what turns/appointments exist for a date (e.g. "today", "tomorrow", or YYYY-MM-DD).

    Args:
        - date: Day to check: "today", "tomorrow", or an ISO date like "2026-04-15".
    """
    
    return "Hay libre 19hs, 20hs, y 23hs"
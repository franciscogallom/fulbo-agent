from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver

# The system prompt defines your agent’s role and behavior. Keep it specific and actionable.

SYSTEM_PROMPT = """You are a virtual assistant for a football court booking service. Your role is to help customers with their inquiries in a friendly, clear and concise way.

## Capabilities

- `check_availability`: Check which football court time slots are still available on a given day.
"""

# Tools let a model interact with external systems by calling functions you define. 
# Tools can depend on runtime context and also interact with agent memory.

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

# Tools should be well-documented: their name, description, and argument names become part of the model’s prompt. 
# LangChain’s @tool decorator adds metadata and enables runtime injection with the ToolRuntime parameter. 
# Learn more in the tools guide -> https://docs.langchain.com/oss/python/langchain/tools


model = init_chat_model(
    "gemma4:31b-cloud",
    model_provider="ollama",
    temperature=0.5,
    timeout=600,
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer 9d9fcb41665c49a99698a4d5b0a7ec28.JzsztdvYWXq9LGhO0JOoU52X"}},
)

# Add memory to your agent to maintain state across interactions. 
# This allows the agent to remember previous conversations and context.

checkpointer = InMemorySaver()

# There are two different frameworks for creating agents: LangChain agents and deep agents. 
# Both LangChain and deep agents provide you with fine-grained control over tools, memory, and more. 
# The main difference between both is that deep agents come with a range of commonly useful 
# capabilities already built in, such as planning, file system tools, and subagents.
# Use deep agents when you want maximum capability with minimal setup; choose LangChain agents when you need fine-grained control.

deep_agent = create_deep_agent(
    model=model,
    tools=[check_availability],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

content = f"""que canchas hay libres hoy?"""

deep_agent_result = deep_agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-da"}},
)

print("\n")
print(deep_agent_result["messages"][-1].content_blocks)

# The deep agent can:
#   - Plans its approach using the built-in write_todos tool to break down the research task.
#   - Loads the file by calling the fetch_text_from_url tool to gather information.
#   - Manages context by using file system tools (grep and read_file).
#   - Spawns subagents as needed to delegate complex subtasks to specialized subagents.
# 
# For LangChain agents, you must implement more capabilities to get a similar level of service 
# and can customize them along the way as needed.
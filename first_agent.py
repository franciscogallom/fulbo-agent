from langchain.agents import create_agent
from langchain_ollama import ChatOllama

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

model = ChatOllama(
    model="gemma4:31b-cloud",  # un modelo disponible en cloud
    base_url="https://ollama.com",
    client_kwargs={"headers": {"Authorization": f"Bearer 9d9fcb41665c49a99698a4d5b0a7ec28.JzsztdvYWXq9LGhO0JOoU52X"}},
)

agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in San Francisco?"}]}
)

print(result["messages"][-1].content_blocks)
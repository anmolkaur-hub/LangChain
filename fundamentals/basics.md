
Building basic agents

from langchain.chat_models import init_chat_model

model = init_chat_model(
    "openai:gpt-5.5",
    temperature=0.5,
    timeout=300,
    max_tokens=25000,
)



from langgraph.checkpoint.memory import InMemorySaver
checkpointer = InMemorySaver()


deep agents
from langchain.agents import create_agent
from deepagents import create_deep_agent

agent = create_agent(
    model=model,
    tools=[fetch_text_from_url],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

deep_agent = create_deep_agent(
    model=model,
    tools=[fetch_text_from_url],
    system_prompt=SYSTEM_PROMPT,
    checkpointer=checkpointer,
)

content = f"""Project Gutenberg hosts a full plain-text copy of F. Scott Fitzgerald's The Great Gatsby.
URL: https://www.gutenberg.org/files/64317/64317-0.txt

Answer as much as you can:

1) How many lines in the complete Gutenberg file contain the substring `Gatsby` (count lines, not occurrences within a line, each line ends with a line break).
2) The 1-based line number of the first line in the file that contains `Daisy`.
3) A two-sentence neutral synopsis.

Do your best on (1) and (2). If at any point you realize you cannot **verify** an exact answer with
your available tools and reasoning, do not fabricate numbers: use `null` for that field and spell out
the limitation in `how_you_computed_counts`. If you encounter any errors please report what the error was and what the error message was."""

print("Running create_agent...", flush=True)
agent_result = agent.invoke(
    {"messages": [{"role": "user",
     "content": content
     }
     ]},
    config={"configurable": {"thread_id": "great-gatsby-lc"}},
)
print("Running create_deep_agent...", flush=True)

deep_agent_result = deep_agent.invoke(
    {"messages": [{"role": "user", "content": content}]},
    config={"configurable": {"thread_id": "great-gatsby-da"}},
)
print("\ncreate_agent:")
print(agent_result["messages"][-1].content_blocks)
print("\ncreate_deep_agent:")
print(deep_agent_result["messages"][-1].content_blocks)
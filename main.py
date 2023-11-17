import time
import asyncio
from agents.MyAgent import MyAgent

if __name__ == "__main__":
    # Create instances of your agents
    agent1 = MyAgent("agent1@myserver.com", "password1")
    agent2 = MyAgent("agent2@myserver.com", "password2")

    # Start the agents
    asyncio.run(agent1.start())
    asyncio.run(agent2.start())

    # Keep the program running
    try:
        while agent1.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        asyncio.run(agent1.stop())
        asyncio.run(agent2.stop())
        print("Agents stopped")
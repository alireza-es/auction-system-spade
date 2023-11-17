from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class MyAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def run(self):
            print("Running behaviour...")

    async def setup(self):
        print("Agent starting...")
        b = self.MyBehav()
        self.add_behaviour(b)
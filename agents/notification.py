from spade.agent import Agent
from behaviours import ReceiveEndAuctionBehaviour


class NotificationAgent(Agent):
    def __init__(self, jid, password, verify_security=False):
        super().__init__(jid, password, verify_security)

    async def setup(self):
        print("NotificationAgent started")
        b = ReceiveEndAuctionBehaviour()
        self.add_behaviour(b)

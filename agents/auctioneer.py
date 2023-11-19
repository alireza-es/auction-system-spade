from spade.agent import Agent
from behaviours.receive_bid import ReceiveBidsBehaviour

class AuctioneerAgent(Agent):
    def __init__(self, jid, password, verify_security=False):
        super().__init__(jid, password, verify_security)
        self.auctions = {}

    async def setup(self):
        print("AuctioneerAgent started")
        b = ReceiveBidsBehaviour()
        self.add_behaviour(b)
from spade.agent import Agent
from behaviours.monitor_auction import MonitorAuctionBehaviour


class BidderAgent(Agent):
    def __init__(self, jid, password, verify_security=False):
        super().__init__(jid, password, verify_security)
        self.auctions = {}

    async def setup(self):
        print("BidderAgent started")
        b = MonitorAuctionBehaviour(period=10)  # Check auctions every 10 seconds
        self.add_behaviour(b)

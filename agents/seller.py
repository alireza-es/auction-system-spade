from spade.agent import Agent
from behaviours import InitiateAuctionBehaviour


class SellerAgent(Agent):
    def __init__(self, jid, password, verify_security=False, auctioneer_jid=None, item_name=None, starting_price=None,
                 time_left=None):
        super().__init__(jid, password, verify_security)
        self.auctioneer_jid = auctioneer_jid
        self.item_name = item_name
        self.starting_price = starting_price
        self.time_left = time_left

    async def setup(self):
        print("SellerAgent started")
        b = InitiateAuctionBehaviour(auctioneer_jid=self.auctioneer_jid, item_name=self.item_name,
                                     starting_price=self.starting_price, time_left=self.time_left)
        self.add_behaviour(b)

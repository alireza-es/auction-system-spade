from spade.agent import Agent
from behaviours import ReceiveBidBehaviour, ReceiveInitiateAuctionBehaviour


class AuctioneerAgent(Agent):
    def __init__(self, jid, password, verify_security=False):
        super().__init__(jid, password, verify_security)
        self.auctions = {}

    async def setup(self):
        print("AuctioneerAgent started")

        receive_bid_behaviour = ReceiveBidBehaviour()
        self.add_behaviour(receive_bid_behaviour)

        receive_auction_behaviour = ReceiveInitiateAuctionBehaviour()
        self.add_behaviour(receive_auction_behaviour)

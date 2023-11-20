from spade.agent import Agent
from spade.template import Template

from behaviours import ReceiveBidBehaviour, ReceiveInitiateAuctionBehaviour
from constants import Performative, Actions


class AuctioneerAgent(Agent):
    def __init__(self, jid, password, verify_security=False):
        super().__init__(jid, password, verify_security)
        self.auctions = {}

    async def setup(self):
        print("AuctioneerAgent started")

        receive_bid_behaviour = ReceiveBidBehaviour()
        bid_template = Template()
        bid_template.set_metadata("performative", Performative.REQUEST.value)
        bid_template.set_metadata("action", Actions.PLACE_BID.value)
        self.add_behaviour(receive_bid_behaviour, bid_template)

        auction_template = Template()
        auction_template.set_metadata("performative", Performative.REQUEST.value)
        auction_template.set_metadata("action", Actions.START_AUCTION.value)
        receive_auction_behaviour = ReceiveInitiateAuctionBehaviour()
        self.add_behaviour(receive_auction_behaviour, auction_template)

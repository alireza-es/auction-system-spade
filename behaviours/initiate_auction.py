# behaviours/initiate_auction.py
import json
from spade.behaviour import OneShotBehaviour
from spade.message import Message
from constants import DEFAULT_AUCTION_TIME_LEFT, Performative, Actions


class InitiateAuctionBehaviour(OneShotBehaviour):
    def __init__(self, auctioneer_jid, item_name, starting_price, time_left=DEFAULT_AUCTION_TIME_LEFT):
        super().__init__()
        self.auctioneer_jid = auctioneer_jid
        self.item_name = item_name
        self.starting_price = starting_price
        self.time_left = time_left

    async def run(self):
        print(f"SellerAgent is initiating an auction for {self.item_name}")
        msg = Message(to=self.auctioneer_jid)
        msg.set_metadata("performative", Performative.REQUEST.value)
        msg.set_metadata("action", Actions.START_AUCTION.value)
        msg.body = json.dumps({
            "auctioneer": self.auctioneer_jid,
            "item_name": self.item_name,
            "starting_price": self.starting_price,
            "time_left": self.time_left,
            "seller": str(self.agent.jid),
        })
        await self.send(msg)

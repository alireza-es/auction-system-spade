# behaviours/place_bid.py
import json
from spade.behaviour import OneShotBehaviour
from spade.message import Message


class PlaceBidBehaviour(OneShotBehaviour):
    def __init__(self, auctioneer_jid, auction_id, amount):
        super().__init__()
        self.auctioneer_jid = auctioneer_jid
        self.auction_id = auction_id
        self.amount = amount

    async def run(self):
        print(f"BidderAgent is placing a bid of {self.amount} on auction {self.auction_id}")
        msg = Message(to=self.auctioneer_jid)
        msg.body = json.dumps({
            "auction_id": self.auction_id,
            "amount": self.amount,
        })
        await self.send(msg)

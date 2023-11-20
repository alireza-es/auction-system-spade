# behaviours/receive_bid.py
import json
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from constants import Performative, Actions
from models.bid import Bid


class ReceiveBidBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            # if msg.get_metadata('performative') == Performative.REQUEST.value and msg.get_metadata('template') == Actions.PLACE_BID.value:
            print(f"AuctioneerAgent received a bid: {msg.body}")
            data = json.loads(msg.body)
            bid = Bid(msg.sender, int(data["amount"]))
            auction_id = int(data["auction_id"])
            if auction_id in self.agent.auctions:
                self.agent.auctions[auction_id].place_bid(bid)

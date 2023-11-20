# behaviours/receive_initiate_auction.py
import json
from spade.behaviour import CyclicBehaviour
from spade.message import Message
from constants import Performative, Actions
from models import Auction


class ReceiveInitiateAuctionBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            print(f"AuctioneerAgent received an initiate auction message: {msg.body}")
            data = json.loads(msg.body)
            auction = Auction(data["item_name"], int(data["starting_price"]), int(data["time_left"]), data["seller"],
                              data["auctioneer"])
            self.agent.auctions[auction.id] = auction

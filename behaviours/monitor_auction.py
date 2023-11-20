# behaviours/monitor_auction.py
from datetime import datetime

from spade.behaviour import PeriodicBehaviour
from behaviours.place_bid import PlaceBidBehaviour
from random import randint


class MonitorAuctionBehaviour(PeriodicBehaviour):
    async def run(self):
        print("Monitoring auctions")
        for auction_id, auction in list(self.agent.auctions.items()):
            auction.time_left -= (datetime.now() - auction.created_on).total_seconds()
            if auction.time_left > 0:
                highest_bid_amount = auction.bidder.amount if hasattr(auction, 'bidder') else 0
                print(
                    f"Auction {auction_id} for {auction.item_name} is ongoing with highest bid {highest_bid_amount}")
                if self.should_place_bid(auction):
                    amount = randint(highest_bid_amount + 1, highest_bid_amount + 10)
                    b = PlaceBidBehaviour(auctioneer_jid=auction.auctioneer, auction_id=auction_id, amount=amount)
                    self.agent.add_behaviour(b)

    def should_place_bid(self, auction):
        # Add your bidding strategy here. For example, you might check if the current highest bid is less than a certain amount.
        # return auction.highest_bid < 100
        return True

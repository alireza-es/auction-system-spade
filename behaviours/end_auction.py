# behaviours/end_auction.py
from spade.behaviour import PeriodicBehaviour
from datetime import datetime, timedelta
from behaviours.notify_winner import NotifyWinnerBehaviour
from constants import NOTIFICATION


class EndAuctionBehaviour(PeriodicBehaviour):
    async def run(self):
        print("Checking if any auctions should be ended")
        for auction_id, auction in list(self.agent.auctions.items()):
            auction.time_left -= (datetime.now() - auction.created_on).total_seconds()
            if auction.time_left <= 0:
                print(f"Auction {auction_id} has ended")
                if auction.highest_bid:
                    print(f"The highest bid was {auction.highest_bid.amount} from {auction.highest_bid.bidder}")
                    b = NotifyWinnerBehaviour(notification_jid=NOTIFICATION.jid, auction=auction)
                    self.agent.add_behaviour(b)
                else:
                    print("There were no bids")
                del self.agent.auctions[auction_id]
            else:
                print(f"Auction {auction_id} has {auction.time_left} seconds left")

import asyncio
import time
from agents import AuctioneerAgent, BidderAgent, SellerAgent, NotificationAgent
from constants import AUCTIONEER, BIDDER, SELLER, NOTIFICATION

if __name__ == "__main__":
    # Create instances of each agent
    auctioneer = AuctioneerAgent(AUCTIONEER.jid, AUCTIONEER.password)
    seller = SellerAgent(SELLER.jid, SELLER.password, auctioneer_jid=AUCTIONEER.jid, item_name="Car", starting_price=100, time_left=10)
    bidder1 = BidderAgent(BIDDER.jid, BIDDER.password, auctions=auctioneer.auctions)
    # bidder2 = BidderAgent(BIDDER.jid, BIDDER.password, auctions=auctioneer.auctions)
    notification = NotificationAgent(NOTIFICATION.jid, NOTIFICATION.password)

    # Create a single event loop
    loop = asyncio.get_event_loop()

    # Start the agents
    loop.run_until_complete(auctioneer.start())
    loop.run_until_complete(seller.start())
    loop.run_until_complete(bidder1.start())
    # loop.run_until_complete(bidder2.start())
    loop.run_until_complete(notification.start())

    # Keep the program running
    try:
        while auctioneer.is_alive():
            time.sleep(1)
    finally:
        loop.close()
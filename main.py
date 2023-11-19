import time
import asyncio
from constants import AUCTIONEER, BIDDER, SELLER, NOTIFICATION
from agents import AuctioneerAgent, BidderAgent, SellerAgent, NotificationAgent

if __name__ == "__main__":
    # Create instances of each agent
    auctioneer = AuctioneerAgent(AUCTIONEER.jid, AUCTIONEER.password)
    bidder1 = BidderAgent(BIDDER.jid, BIDDER.password)
    bidder2 = BidderAgent(BIDDER.jid, BIDDER.password)
    seller = SellerAgent(SELLER.jid, SELLER.password)
    notification = NotificationAgent(NOTIFICATION.jid, NOTIFICATION.password)

    # Start the agents
    asyncio.run(auctioneer.start())
    asyncio.run(bidder1.start())
    asyncio.run(bidder2.start())
    asyncio.run(seller.start())
    asyncio.run(notification.start())

    # Keep the program running
    try:
        while auctioneer.is_alive():
            time.sleep(1)
    except KeyboardInterrupt:
        asyncio.run(auctioneer.stop())
        asyncio.run(bidder1.stop())
        asyncio.run(bidder2.stop())
        asyncio.run(seller.stop())
        asyncio.run(notification.stop())
        print("Agents stopped")
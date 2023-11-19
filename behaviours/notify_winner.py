# behaviours/notify_winner.py
from spade.behaviour import OneShotBehaviour
from spade.message import Message

class NotifyWinnerBehaviour(OneShotBehaviour):
    def __init__(self, notification_jid, auction):
        super().__init__()
        self.notification_jid = notification_jid
        self.auction = auction

    async def run(self):
        print(f"AuctioneerAgent is notifying the winner of auction {self.auction.id}")
        msg = Message(to=self.notification_jid)
        msg.body = f"{self.auction.seller},{self.auction.highest_bid.bidder},{self.auction.item_name},{self.auction.highest_bid.amount}"
        await self.send(msg)
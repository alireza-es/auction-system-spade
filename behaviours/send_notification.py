from spade.behaviour import OneShotBehaviour
from spade.message import Message

class SendNotificationBehaviour(OneShotBehaviour):
    def __init__(self, seller_jid, bidder_jid, item_name, highest_bid):
        super().__init__()
        self.seller_jid = seller_jid
        self.bidder_jid = bidder_jid
        self.item_name = item_name
        self.highest_bid = highest_bid

    async def run(self):
        print(f"NotificationAgent is sending a notification about {self.item_name}")
        msg = Message(to=self.seller_jid)
        msg.body = f"The auction for {self.item_name} has ended. The highest bid was {self.highest_bid}."
        await self.send(msg)
        msg = Message(to=self.bidder_jid)
        msg.body = f"You have won the auction for {self.item_name} with a bid of {self.highest_bid}."
        await self.send(msg)
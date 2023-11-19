from spade.behaviour import CyclicBehaviour
from spade.message import Message
from behaviours.send_notification import SendNotificationBehaviour

class ReceiveEndAuctionBehaviour(CyclicBehaviour):
    async def run(self):
        msg = await self.receive(timeout=10)
        if msg:
            print(f"NotificationAgent received an end auction message: {msg.body}")
            seller_jid, bidder_jid, item_name, highest_bid = msg.body.split(',')
            b = SendNotificationBehaviour(seller_jid, bidder_jid, item_name, highest_bid)
            self.agent.add_behaviour(b)
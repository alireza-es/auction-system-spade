# constants.py
from dataclasses import dataclass

DEFAULT_AUCTION_TIME_LEFT = 15  # in minutes

@dataclass
class AgentInfo:
    jid: str
    password: str

AUCTIONEER = AgentInfo(jid="auctioneer@localhost", password="123")
BIDDER = AgentInfo(jid="bidder@localhost", password="123")
SELLER = AgentInfo(jid="seller@localhost", password="123")
NOTIFICATION = AgentInfo(jid="notification@localhost", password="123")
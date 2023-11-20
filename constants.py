# constants.py
from dataclasses import dataclass
from enum import Enum

DEFAULT_AUCTION_TIME_LEFT = 15  # in minutes


@dataclass
class AgentInfo:
    jid: str
    password: str


AUCTIONEER = AgentInfo(jid="auctioneer@localhost", password="123")
BIDDER = AgentInfo(jid="bidder@localhost", password="123")
SELLER = AgentInfo(jid="seller@localhost", password="123")
NOTIFICATION = AgentInfo(jid="notification@localhost", password="123")


class Template(Enum):
    START_AUCTION = 'start_auction'
    PLACE_BID = 'place_bid'


class Performative(Enum):
    INFORM = 'inform'
    REQUEST = 'request'
    CONFIRM = 'confirm'
    REJECT = 'reject'

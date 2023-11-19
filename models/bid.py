# models/bid.py
from datetime import datetime

class Bid:
    def __init__(self, bidder, amount):
        self.bidder = bidder
        self.amount = amount
        self.created_on = datetime.now()
# models/auction.py
import time
from datetime import datetime


class Auction:
    def __init__(self, item_name, starting_price, time_left, seller):
        self.id = int(time.time())
        self.item_name = item_name
        self.starting_price = starting_price
        self.time_left = time_left
        self.seller = seller
        self.created_on = datetime.now()
        self.bids = []
        self.highest_bid = None

    def place_bid(self, bid):
        self.bids.append(bid)
        if self.highest_bid is None or bid.amount > self.highest_bid.amount:
            self.highest_bid = bid

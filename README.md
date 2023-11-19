# Auction System SPADE

This project is an implementation of a multi-agent online auction system using the SPADE (Smart Python multi-Agent Development Environment) framework.

## Project Structure

The project has the following structure:
```
.
├── auction-system-spade
│   ├── models
│   │   ├── __init__.py
│   │   ├── auction.py
│   │   └── bid.py
│   ├── agents
│   │   ├── __init__.py
│   │   ├── auctioneer.py
│   │   ├── bidder.py
│   │   ├── seller.py
│   │   └── notification.py
│   ├── behaviours
│   │   ├── __init__.py
│   │   ├── receive_bids.py
│   │   ├── place_bid.py
│   │   ├── initiate_auction.py
│   │   ├── monitor_auction.py
│   │   ├── end_auction.py
│   │   └── notify_winner.py
│   ├── constants.py
│   ├── main.py
│   └── README.md
```
## Setting Up the XMPP Server

We use Prosody as the XMPP server. To install Prosody on Ubuntu, run the following command:

```bash
sudo apt-get install prosody
```

## Creating Agents

To create the agents we need, use the following commands:

```bash
prosodyctl register auctioneer localhost password
prosodyctl register bidder localhost password
prosodyctl register seller localhost password
prosodyctl register notification localhost password
```

Replace `password` with a secure password for each agent.

Next steps could include running the auction system, or configuring the XMPP server.


## Agents

The system includes the following agents:

- `AuctioneerAgent`: This agent handles the creation of auctions, receiving and processing bids, updating auction status, and closing the auction.
- `BidderAgent`: This agent can place bids on items in the auction.
- `SellerAgent`: This agent can initiate an auction and monitor the auction.
- `NotificationAgent`: This agent is responsible for informing the winning Bidder Agent and the Seller Agent about the auction outcome.

## Behaviours

The system includes the following behaviours:

- `InitiateAuctionBehaviour`: This behaviour is used by the `SellerAgent` to initiate an auction by sending a request to the `AuctioneerAgent`.
- `MonitorAuctionBehaviour`: This behaviour is used by the `BidderAgent` to monitor ongoing auctions and decide when to place a bid.
- `PlaceBidBehaviour`: This behaviour is used by the `BidderAgent` to place a bid on an auction.
- `ReceiveBidsBehaviour`: This behaviour is used by the `AuctioneerAgent` to receive bids from `BidderAgent`s.
- `EndAuctionBehaviour`: This behaviour is used by the `AuctioneerAgent` to end auctions when their time is up.
- `NotifyWinnerBehaviour`: This behaviour is used by the `AuctioneerAgent` to notify the `NotificationAgent` when an auction ends.

Each behaviour is responsible for a specific part of the auction process, and they work together to create a complete online auction system.

## Running the Project

To run the project, execute the `main.py` script:

```bash
python main.py
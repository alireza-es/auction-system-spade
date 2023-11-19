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
│   │   └── notify_winner.py
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

- `ReceiveBidsBehaviour`: This behaviour allows the AuctioneerAgent to receive and process bids.
- `PlaceBidBehaviour`: This behaviour allows the BidderAgent to place bids.
- `MonitorAuctionBehaviour`: This behaviour allows the SellerAgent to monitor the auction.
- `NotifyWinnerBehaviour`: This behaviour allows the NotificationAgent to notify the winner and the seller about the auction outcome.

## Running the Project

To run the project, execute the `main.py` script:

```bash
python main.py
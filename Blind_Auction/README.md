# Blind Auction

A **blind auction** where multiple bidders secretly submit their bids, and the program determines the highest bidder after all participants have finished bidding.

## 💰 How the Auction Works

In a blind auction, bidders submit their bids without seeing the bids made by other participants.

The program:

1. Asks each bidder for their name.
2. Records their bid in a dictionary.
3. Asks whether another bidder wants to participate.
4. Hides previous bids from the next bidder.
5. Compares all submitted bids.
6. Determines the bidder with the highest bid.
7. Displays the winner and winning bid.

## 📁 Project Structure

```text
blind-auction/
│
├── main.py          # Main auction program
├── art.py           # ASCII logo used by the program
├── README.md        # Project documentation
└── .gitignore       # Git configuration
```

## 🔒 Blind Bidding

After each bidder submits their bid, the program prints multiple blank lines to separate the previous bidder's information from the next bidder's screen.

This provides a simple command-line implementation of the idea of a blind auction.

```python
print("\n" * 30)
```

This is not a security mechanism—someone with access to the terminal history or program environment could still potentially recover previous information.


from art import Auction_logo
print(Auction_logo)


# bidder_name = input("What is your name?: ")
# bidding_amount = int(input("What is your bid?: $ "))

# bidding_dictionary = {}
# bidding_dictionary[bidder_name] = bidding_amount



bidding_continues = True
bidding_dictionary = {}

while bidding_continues:
    bidder_name = input("What is your name?: ")
    bidding_amount = int(input("What is your bid?: $ "))

    bidding_dictionary[bidder_name] = bidding_amount
    restart = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if restart == "yes":
        print(20 * "\n")
        
    if restart == "no":
        bidding_continues = False

# print(bidding_dictionary)

highest_bid = 0
highest_bidder = ""

for key in bidding_dictionary:
    if bidding_dictionary[key] > highest_bid:
        highest_bid = bidding_dictionary[key]
        highest_bidder = key

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")











    
import os
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for i in bidder_details:
        bidding_price=bidder_details[i]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=i
    print(f"here is the list of all bidders:{bidder_details}")        
    print(f"The winner is {winner} with a bid price of {highest_bid}")        



bidder_details={}
bidders_flag=True
while bidders_flag:
    name=input("What is your name? :")
    price=int(input("What is your bid price? :"))
    bidder_details[name]=price
    more_bidders=input("Are there more bidders? Type 'yes' or 'no' : ").lower()
    if more_bidders=='no':
        bidders_flag=False
        find_winner(bidder_details)
    elif more_bidders=='yes':
        os.system('cls')    

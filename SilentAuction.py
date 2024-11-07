
print("Welcome to the silent auction")

bid_dict = {}
if_true = True

while if_true:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: $"))


    bid_dict[name] = bid
    for name, bid in bid_dict.items():
        print(f"{name}: ${bid}")
        print("\n"*10)

    choice = input("Are there more bidders? (yes/no): ").lower()
    if choice == 'no':
        if_true = False



winner = max(bid_dict, key=bid_dict.get)
winning_bid = bid_dict[winner]
print(f"\nThe winner is {winner} with a bid of ${winning_bid}")

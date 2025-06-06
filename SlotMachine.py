import random

def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐️"]

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
    print("*************")
    print("|".join(row))
    print("*************")

def get_payoff(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 2
        elif row[0] == "🍉":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 5
        elif row[0] == "⭐️":
            return bet * 10
    return 0

def main():
    balance = 100

    print("************************")
    print("Welcome to the Python Slots!")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐️")
    print("************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Enter your bet amount: ")
        if not bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient balance for this bet.")
            continue
        if bet <= 0:
            print("Bet amount must be greater than zero.")
            continue
        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payoff(row, bet)

        if payout > 0:
            print(f"Congratulations! You won ${payout}!")
        else:
            print("Sorry, you didn't win this time.")
        
        balance += payout

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thank you for playing! Your final balance is $", balance)
            break

if __name__ == "__main__":
    main()
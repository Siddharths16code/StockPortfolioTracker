
import csv

# Hardcoded stock prices (as per task)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 320,
    "AMZN": 135
}

portfolio = {}

print("📈 Welcome to the Stock Portfolio Tracker!")
print("Available Stocks:", ', '.join(stock_prices.keys()))
print("Enter 'done' when you are finished.\n")

# 🔹 Input stock name and quantity
while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the available list.")
        continue
    try:
        qty = int(input(f"Enter quantity for {stock}: "))
        if qty <= 0:
            print("❌ Quantity should be a positive number.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("❌ Please enter a valid integer quantity.")

# 🔹 Calculate total investment
total_value = 0
print("\n📊 Your Investment Summary:")
print("-------------------------------------")
print(f"{'Stock':<10} {'Qty':<10} {'Price':<10} {'Value':<10}")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock:<10} {qty:<10} {price:<10} {value:<10}")
print("-------------------------------------")
print(f"💰 Total Investment Value: ${total_value}")

# 🔹 Optionally save to file
save_option = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save_option == "yes":
    file_type = input("Choose file type (.txt / .csv): ").strip().lower()
    if file_type == ".txt":
        with open("portfolio_summary.txt", "w") as f:
            f.write("Stock\tQty\tPrice\tValue\n")
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                f.write(f"{stock}\t{qty}\t{price}\t{value}\n")
            f.write(f"\nTotal Investment Value: ${total_value}")
        print("✅ Saved as 'portfolio_summary.txt'")
    elif file_type == ".csv":
        with open("portfolio_summary.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Stock", "Qty", "Price", "Value"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = price * qty
                writer.writerow([stock, qty, price, value])
            writer.writerow(["", "", "Total", total_value])
        print("✅ Saved as 'portfolio_summary.csv'")
    else:
        print("❌ Invalid file type selected. File not saved.")

print("\n✅ Thank you for using the Stock Portfolio Tracker!")

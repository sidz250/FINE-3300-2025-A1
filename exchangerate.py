import csv

class ExchangeRates:
    def __init__(self, filename="/Users/siddhanthnarayanan/Fine 3300 class 2/FINE-3300-2025-A1/BankOfCanadaExchangeRates.csv"):
                # Store filename and read latest USD/CAD rate
        self.filename = filename
        self.rate = self.read_latest_rate()

    def read_latest_rate(self):
                # Read last row in CSV to get latest USD/CAD rate
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            last_row = None
            for row in reader:
                last_row = row

            if last_row and "USD/CAD" in last_row:
                return float(last_row["USD/CAD"])
            else:
                raise ValueError("USD/CAD rate not found in CSV.")

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate
        else:
            raise ValueError("Unsupported currency conversion.")


if __name__ == "__main__":
    print("\n--- Exchange Rate Calculator ---")

    exchange = ExchangeRates()  # filename is hardcoded

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("From currency (USD/CAD): ").upper()
    to_currency = input("To currency (USD/CAD): ").upper()

    try:
        converted = exchange.convert(amount, from_currency, to_currency)
        print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    except ValueError as e:
        print("Error:", e)

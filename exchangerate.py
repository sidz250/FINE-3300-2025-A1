print("\n--- Exchange Rate Calculator ---")
amount = float(input("Enter the amount to convert: "))
from_currency = input("Enter the currency you’re converting from (e.g., USD): ").upper()
to_currency = input("Enter the currency you’re converting to (e.g., CAD): ").upper()

# Simplified example (in a real version, you could read from a CSV)
# Example rates — replace these with values from your CSV if needed
usd_to_cad = 1.37
cad_to_usd = 1 / usd_to_cad

if from_currency == "USD" and to_currency == "CAD":
    converted = amount * usd_to_cad
elif from_currency == "CAD" and to_currency == "USD":
    converted = amount * cad_to_usd
else:
    converted = None

# Show result
if converted is not None:
    print(f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
else:
    print("Sorry, conversion not supported in this version.")
import math

class MortgagePayment:
    def __init__(self, rate, years):
        self.rate = rate / 100  
        self.years = years

    def pva(self, r, n):
        return (1 - (1 + r) ** (-n)) / r

    def payments(self, principal):
        effective_annual = (1 + self.rate / 2) ** 2 - 1

        frequencies = {
            "monthly": 12,
            "semi_monthly": 24,
            "bi_weekly": 26,
            "weekly": 52
        }

        results = {}
        for key, freq in frequencies.items():
            r = (1 + effective_annual) ** (1 / freq) - 1
            n = self.years * freq
            factor = self.pva(r, n)
            results[key] = principal / factor

        results["rapid_bi_weekly"] = results["monthly"] / 2
        results["rapid_weekly"] = results["monthly"] / 4

        return (
            round(results["monthly"], 2),
            round(results["semi_monthly"], 2),
            round(results["bi_weekly"], 2),
            round(results["weekly"], 2),
            round(results["rapid_bi_weekly"], 2),
            round(results["rapid_weekly"], 2)
        )

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the quoted interest rate (as a percent, e.g. 5.5): "))
years = int(input("Enter the amortization period in years: "))

mortgage = MortgagePayment(rate, years)
payments = mortgage.payments(principal)


print(f"\nMonthly Payment: ${payments[0]:,.2f}")
print(f"Semi-monthly Payment: ${payments[1]:,.2f}")
print(f"Bi-weekly Payment: ${payments[2]:,.2f}")
print(f"Weekly Payment: ${payments[3]:,.2f}")
print(f"Rapid Bi-weekly Payment: ${payments[4]:,.2f}")
print(f"Rapid Weekly Payment: ${payments[5]:,.2f}")

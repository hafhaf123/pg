import sys
from cviceni6 import download_rates


def convert_amount(amount, currency):
    rates = download_rates()
    rate = rates[currency]
    converted_amount = amount / rate
    return converted_amount

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(f"Použití: {sys.argv[0]} částka měna")
        sys.exit(1)

    amount = float(sys.argv[1])
    currency = sys.argv[2]

    print(convert_amount(amount, currency))
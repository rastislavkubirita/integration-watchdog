"""
Integration Watchdog - prvy testovaci skript.

Co robi:
1. Zavola verejne API (Frankfurter) a ziska aktualny kurz EUR -> USD.
2. Vypise ho do konzoly.
3. Porovna ho s nastavenym limitom.
4. Ak je kurz nad limitom, vypise ALERT (v dalsom kroku z toho urobime
   realne upozornenie, napr. draft v Gmaile).
"""

import urllib.request
import json

API_URL = "https://api.frankfurter.dev/v1/latest?from=EUR&to=USD"

# Limit, pri ktorom chceme byt upozorneni (priklad: EUR/USD nad 1.12)
THRESHOLD = 1.12


def get_eur_usd_rate() -> float:
    """Stiahne aktualny kurz EUR/USD z verejneho API a vrati ho ako cislo."""
    with urllib.request.urlopen(API_URL, timeout=10) as response:
        data = json.load(response)
    return data["rates"]["USD"]


def main() -> None:
    rate = get_eur_usd_rate()
    print(f"Aktualny kurz EUR/USD: {rate}")

    if rate > THRESHOLD:
        print(f"ALERT: kurz {rate} prekrocil limit {THRESHOLD}!")
    else:
        print(f"OK: kurz {rate} je v norme (limit {THRESHOLD}).")


if __name__ == "__main__":
    main()

import requests

base_url = "https://v6.exchangerate-api.com/v6/"
api_key = "YOUR API KEY HERE"

def get_info(base_currency):
    url = f"{base_url}{api_key}/latest/{base_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        print("Success")
        data = response.json()
        return data
    else:
        print("Something went wrong!")

while True:
    currency = input("Enter the base currency: ")
    if len(currency) == 3:
        if currency.isdigit() == False:
            if currency.isalpha() == True:
                try:
                    if currency in get_info(currency):
                        break
                except TypeError:
                    print("Enter a valid 3 letter code")
    else:
        print("Enter the 3 letter code of the currency")
currency_conversions = get_info(currency)

while True:
    convert_currency = input(f"Enter the curreny you want to convert {currency} into: ")
    if currency_conversions:
        print(f"1 {currency} is equal to {currency_conversions['conversion_rates'][convert_currency]} {convert_currency}")
    else:
        print("Couldn't convert")
    choice = input("Want to convert again (Y/N)?: ").upper()
    if choice == "Y":
       continue
    elif choice == "N":
        print("Goodbye!")
        break
    else:
        print("Enter Y or N")

CurrencyRates = {
    'AUD':55.55,
    'USD':82.23,
    'DKK':11.73,
    'JPY':0.60,
    'CAD':60.14,
    'CNY':11.14,
    'CZK':3.71,
    'EUR':87.05,
    'GBP':98.42,
    'NOK':4.82,
    'NZD':50.81,
}


from_cur = input("Enter from currency : " )
to_cur = input("Enter to currency to convert : ")
amount = float(input("Enter amount to convert : "))

def currency_converter(from_cur,to_cur, amount):
    if from_cur in CurrencyRates.values():
        v1 = CurrencyRates[from_cur]
        v2 = CurrencyRates[to_cur]
        convert1 = v1/v2
        convert = round((amount * convert1),2)
        print ("From :", from_cur, amount, "\n", "To :", to_cur, convert)
    else:
        print("uanble to find rate for", from_cur, to_cur)

currency_converter(from_cur, to_cur, amount)
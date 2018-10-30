# Currency Convert
CurrencyStr = input()
if CurrencyStr[0: 3] == "RMB":
    USD = eval(CurrencyStr[3:]) / 6.78
    print("USD{:.2f}".format(USD))
elif CurrencyStr[0: 3] == "USD":
    RMB = 6.78 * eval(CurrencyStr[3:])
    print("RMB{:.2f}".format(RMB))

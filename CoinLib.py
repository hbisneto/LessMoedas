CoinsArray = []
RealValue = int()

def MakeCoinChange(CoinValueList, CoinChange, MinCoins, CoinsUsed):
   for Cents in range(CoinChange+1):
      CoinCount = Cents
      NewCoin = 1
      for j in [c for c in CoinValueList if c <= Cents]:
            if MinCoins[Cents-j] + 1 < CoinCount:
               CoinCount = MinCoins[Cents-j]+1
               NewCoin = j
      MinCoins[Cents] = CoinCount
      CoinsUsed[Cents] = NewCoin
   return MinCoins[CoinChange]

def printCoins(CoinUsed,CoinChange):
   PrintCoinCount = CoinChange
   while PrintCoinCount > 0:
      ThisCoin = CoinUsed[PrintCoinCount]
      CoinsArray.append(ThisCoin)
      PrintCoinCount = PrintCoinCount - ThisCoin

def main():
    OneCoin = 0
    FiveCoin = 0
    TenCoin = 0
    TwentyFiveCoin = 0
    FiftyCoin = 0

    CentCoin = int(input(">> Informe os centavos [2 Digitos]: "))
    CoinList = [1, 5, 10, 25, 50]
    CoinUsed = [0]*(CentCoin+1)
    CoinCount = [0]*(CentCoin+1)

    print("="*80)
    print(f'>> Valor digitado foi R$ {RealValue},{CentCoin}')
    print("="*80)

    CoinsNumber = MakeCoinChange(CoinList,CentCoin,CoinCount,CoinUsed)
    print(CoinsNumber, "Moedas")
    printCoins(CoinUsed, CentCoin)
    print("="*80)

    print("="*80)
    print(">> Quantidade de moedas <<")
    print("="*80)

    for j in CoinsArray:
        if j == 1:
            OneCoin += 1
        elif j == 5:
            FiveCoin += 1
        elif j == 10:
            TenCoin += 1
        elif j == 25:
            TwentyFiveCoin += 1
        elif j == 50:
            FiftyCoin += 1

    print("="*80)
    # 1
    if OneCoin > 0 and OneCoin < 2:
        print(f'{OneCoin} moeda de 0,{CoinList[0]} centavo')
    else:
        if OneCoin >=2:
            print(f'{OneCoin} moedas de 0,{CoinList[0]} centavo')

    ## 5
    if FiveCoin > 0 and FiveCoin < 2:
        print(f'{FiveCoin} moeda de 0,{CoinList[1]} centavo')
    else:
        if FiveCoin >=2:
            print(f'{FiveCoin} moedas de 0,{CoinList[1]} centavos')

    ## 10
    if TenCoin > 0 and TenCoin < 2:
        print(f'{TenCoin} moeda de 0,{CoinList[2]} centavo')
    else:
        if TenCoin >=2:
            print(f'{TenCoin} moedas de 0,{CoinList[2]} centavos')

    ## 25
    if TwentyFiveCoin > 0 and TwentyFiveCoin < 2:
        print(f'{TwentyFiveCoin} moeda de 0,{CoinList[3]} centavo')
    else:
        if TwentyFiveCoin >=2:
            print(f'{TwentyFiveCoin} moedas de 0,{CoinList[3]} centavos')

    ## 50
    if FiftyCoin > 0 and FiftyCoin < 2:
        print(f'{FiftyCoin} moeda de 0,{CoinList[4]} centavo')
    else:
        if FiftyCoin >=2:
            print(f'{FiftyCoin} moedas de 0,{CoinList[4]} centavos')
    print("="*80)

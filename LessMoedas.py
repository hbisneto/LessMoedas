## LessMoedas
from datetime import date
import CoinLib

AnoAtual = date.today().year
SoftwareName = "LessMoedas"
Version = "1.0"
CopyrightName = "Heitor Bisneto"

print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)
if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print()


NotasArray = []

def MakeChange(RealValueList,RealChange,MinReal,RealUsed):
   for Real in range(RealChange+1):
      RealCount = Real
      NewReal = 1
      for j in [c for c in RealValueList if c <= Real]:
            if MinReal[Real-j] + 1 < RealCount:
               RealCount = MinReal[Real-j]+1
               NewReal = j
      MinReal[Real] = RealCount
      RealUsed[Real] = NewReal
   return MinReal[RealChange]

def PrintReal(RealUsed,RealChange):
   PrintCount = RealChange
   while PrintCount > 0:
      ThisReal = RealUsed[PrintCount]
      NotasArray.append(ThisReal)
      PrintCount = PrintCount - ThisReal

def Main():
   OneCount = 0
   TwoCount = 0
   FiveCount = 0
   TenCount = 0
   TwentyCount = 0
   FiftyCount = 0
   HandredCount = 0
   TwoHandredCount = 0
   
   RealPapel = int(input(">> Informe um valor (sem os centavos): "))
   RealList = [1, 2, 5, 10, 20, 50, 100, 200]
   RealUsed = [0]*(RealPapel+1)
   RealCount = [0]*(RealPapel+1)

   print("="*80)
   print(">> Quantidade de notas <<")
   print("="*80)
   NotesNumber = MakeChange(RealList, RealPapel, RealCount, RealUsed)
   print(NotesNumber, "Notas")
   PrintReal(RealUsed,RealPapel)
   print("="*80)

   for i in NotasArray:
      if i == 1:
         OneCount += 1
      if i == 2:
         TwoCount += 1
      elif i == 5:
         FiveCount += 1
      elif i == 10:
         TenCount += 1
      elif i == 20:
         TwentyCount += 1
      elif i == 50:
         FiftyCount += 1
      elif i == 100:
         HandredCount += 1
      elif i == 200:
         TwoHandredCount += 1

   ## One: 1
   if OneCount > 0 and OneCount < 2:
      print(f'{OneCount} moeda de {RealList[0]} real')
   else:
      if OneCount >= 2:
         print(f'{OneCount} moedas de {RealList[0]} real')
         
   ## Two: 2
   if TwoCount > 0 and TwoCount < 2:
     print(f'{TwoCount} nota de {RealList[1]} reais')
   else:
     if TwoCount >= 2:
         print(f'{TwoCount} notas de {RealList[1]} reais')

   ## Five: 5
   if FiveCount > 0 and FiveCount < 2:
     print(f'{FiveCount} nota de {RealList[2]} reais')
   else:
     if FiveCount >= 2:
         print(f'{FiveCount} notas de {RealList[2]} reais')

   ## Ten: 10
   if TenCount > 0 and TenCount < 2:
     print(f'{TenCount} nota de {RealList[3]} reais')
   else:
     if TenCount >= 2:
         print(f'{TenCount} notas de {RealList[3]} reais')

   ## Ten: 20
   if TwentyCount > 0 and TwentyCount < 2:
     print(f'{TwentyCount} nota de {RealList[4]} reais')
   else:
     if TwentyCount >= 2:
         print(f'{TwentyCount} notas de {RealList[4]} reais')

   ## Fifty: 50
   if FiftyCount > 0 and FiftyCount < 2:
     print(f'{FiftyCount} nota de {RealList[5]} reais')
   else:
     if FiftyCount >= 2:
         print(f'{FiftyCount} notas de {RealList[5]} reais')

   ## One-Handred
   if HandredCount > 0 and HandredCount < 2:
     print(f'{HandredCount} nota de {RealList[6]} reais')
   else:
     if HandredCount >= 2:
         print(f'{HandredCount} notas de {RealList[6]} reais')

   ## Two-Handred
   if TwoHandredCount > 0 and TwoHandredCount < 2:
     print(f'{TwoHandredCount} nota de {RealList[7]} reais')
   else:
     if TwoHandredCount >= 2:
         print(f'{TwoHandredCount} notas de {RealList[7]} reais')
   print("="*80)

   ## Import CoinLib to keep in execution
   import CoinLib
   CoinLib.RealValue = RealPapel
   
Main()
CoinLib.main()

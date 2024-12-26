#SafeIntegerGenerator
while True:
 Mode=input("Decode/Encode? ")
 if Mode == "Encode":
     Number = int(input("Type a number to Encode: "))
     Calculation1 = Number*17
     Calculation2 = Calculation1*79
     Calculation3 = Calculation2*120
     Calculation4 = Calculation3*3844
     FinalResault = Calculation4
     print(FinalResault)
 elif Mode == "Decode":
    Number = int(input("Type the number to Decode: "))
    Calculation1 = Number/3844
    Calculation2 = Calculation1/120
    Calculation3 = Calculation2/79
    Calculation4 = Calculation3/17
    FinalResault = Calculation4
    print(FinalResault)
 else:
    print("error")
class Calculation:
    def __init__(self):
        self.line = ""

    def SetCalculationLine(self, newLine):
        self.line = newLine

    def SetLastSymbolCalculationLine(self, symbol):
        self.line = self.line + symbol

    def GetCalculationLine(self):
        return self.line

    def GetLastSymbol(self):
        if self.line:
            return self.line[-1]
        else:
            return ""

    def DeleteLastSymbol(self):
        if self.line:
            self.line = self.line[:-1]

calc = Calculation()

calc.SetCalculationLine("1 + 1")
print(calc.GetCalculationLine())
calc.SetLastSymbolCalculationLine(" = ")
print(calc.GetCalculationLine())
print(calc.GetLastSymbol())
calc.DeleteLastSymbol()
print(calc.GetCalculationLine())
calc.SetLastSymbolCalculationLine(" 2 ")
print(calc.GetCalculationLine())

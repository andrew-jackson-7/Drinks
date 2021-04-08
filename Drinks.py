class Drink:
    def __init__(self, drinkName: str, carbonated: bool):
        self.DrinkName = drinkName
        self.Carbonated = carbonated
        carbonatedAnswer = ""
        if (self.Carbonated == True):
            carbonatedAnswer = "carbonated"
        elif (self.Carbonated == False):
            carbonatedAnswer = "not carbonated"
        self.BaseDescription = self.DrinkName + ", " + carbonatedAnswer + ", "

class Juice(Drink):
    def __init__(self, drinkName: str, carbonated: bool):
        super().__init__(drinkName, carbonated)
        self.JuiceKind = self.DrinkName.split(" Juice")[0]
        ending = self.JuiceKind[(len(self.JuiceKind)-1):len(self.JuiceKind)]
        sentenceEnding = "s."
        fruit = self.JuiceKind.lower()
        if (ending == "y"):
            sentenceEnding = "ies."
            fruit = fruit[0:(len(fruit)-1)]
        elif (ending == "h"):
            sentenceEnding = "es."
        self.Description = self.BaseDescription + "made from " + fruit + sentenceEnding

class Beer(Drink):
    def __init__(self, drinkName: str, carbonated: bool, alcohol: int):
        super().__init__(drinkName, carbonated)
        self.Alcohol = alcohol
        self.Description = self.BaseDescription + str(self.Alcohol) + "%."

class Soda(Drink):
    def __init__(self, drinkName: str, carbonated: bool):
        super().__init__(drinkName, carbonated)
        self.Description = self.BaseDescription[0:len(self.BaseDescription)-2] + "."

drinkList = []

drinkList.append(Juice("Orange Juice", False))
drinkList.append(Beer("Budweiser", True, 5))
drinkList.append(Soda("Pepsi", True))

totalDrinkString = ""

for drinkObj in drinkList:
    totalDrinkString = totalDrinkString + drinkObj.Description + " "

print(totalDrinkString)
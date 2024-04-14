class Slime:
    def __init__(self,color,name,weight,size):
         self.color=color
         self.name=name
         self.weight=weight
         self.size=size
    def introduceyourself(self):
        print("Привет, меня зовут ",self.name)
    def scared(self):
        print("Ты такой большой мне страшно")
Artem=Slime("red","Artem",12,23)
Artem.introduceyourself()
Ivan=Slime("blue","Ivan",13,40)
Ivan.introduceyourself()
if Ivan.size > Artem.size :
    Artem.scared()
else:
    Ivan.scared

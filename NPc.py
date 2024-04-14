class NPC:
    def __init__(self,name,height,hp,services):
         self.height=height
         self.name=name
         self.hp=hp
         self.services=services
    def introduceyourself(self):
        print("Привет, меня зовут ",self.name)
    def bb(self):
        print("удачи ждем твоего возвращения")
    def rabota(self):
        print("и я умею делать",self.services)
Artem=NPC("Artem",160,25,"bild home")
Ivan=NPC("Ivan",178,15,"print photos")
Adolf=NPC("Adolf",199,100,"paint oil paintings")
Artem.introduceyourself()
Artem.rabota()

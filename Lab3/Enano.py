from Personaje import Personaje

class Enano(Personaje):
    def __init__(self, no="", ra="", ar="", vi="", da="", bo="", cl=""):
        super().__init__(no, ra, ar, vi, da, bo)
        self.__cl=cl
    
    def GetClan(self):
        return self.__cl
    def SetClan(self, cl):
        self.__cl=cl

    def Historia(self):
        print("Los Enanos son una raza que ha permanecido oculta desde milenios atrás, esto debido a la constante caza de ellos. Con el timepo los enanos decidieron pelear por la paz de su pueblo y se rebelaron ante sus cazadores.")
        
    def AumentaVida(self, aumento):
        if aumento < 50 and aumento > 100:
            print("Has ingresado un valor erróneo")
        else:
            self.SetVida(self.GetVida+aumento)
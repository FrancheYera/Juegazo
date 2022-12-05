from Personaje import Personaje

class Humano(Personaje):
    def __init__(self, no="", ra="", ar="", vi="", da="", bo="", fa=""):
        super().__init__(no, ra, ar, vi, da, bo)
        self.__fa=fa
    
    def GetFamilia(self):
        return self.__fa
    def SetFamilia(self, fa):
        self.__fa=fa

    def Historia(self):
        print("Los humanos desde tiempos inmemorables han habitado la Tierra, debido a su larga estadía estos han desarrollado jerarquías de poder que han vuelto loca a la gente, con el tiempo la locura los hacía huir desde sus pueblos a los bosques.")

    def SuperBono(self):
        bono=int(input("ingrese un valor entre 50 y 100 para sumar a su vida"))
        if bono < 15 and bono > 25:
            print("Has ingresado un valor erróneo")
        else:
            super().SetDaño(super().GetDaño() + int(bono))
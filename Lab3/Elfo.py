from Personaje import Personaje

class Elfo(Personaje):
    def __init__(self, no="", ra="", ar="", vi="", da="", bo="", re=""):
        super().__init__(no, ra, ar, vi, da, bo)
        self.__re=re
    
    def GetReino(self):
        return self.__re
    def SetReino(self, re):
        self.__re=re

    def Historia(self):
        print("Los elfos son una raaz prveniente de otro mundo, un día probando su tecnología esta les falló y cayó una tripulación de 202 elfos en la Tierra, desde el incidente han habitado el planeta ocultos en la naturaleza.")

    def QuitaVida(self):
        super().SetVida(super().GetVida() * 0.1)
class Personaje():
    def __init__(self, no="", ra="", ar="", vi="", da="", bo=""):
        self.__no=no
        self.__ra=ra
        self.__ar=ar
        self.__vi=vi
        self.__da=da
        self.__bo=bo

    def __str__(self):
        return "Nombre: {}  Raza: {}  Arma: {}  Vida: {} Daño{}  Bonificación: {}".format(self.__no, self.__ra, self.__ar, self.__vi, self.__da, self.__bo)

    def GetNombre(self):
        return self.__no
    def SetNomrbe(self, no):
        self.__no=no
    
    def GetRaza(self):
        return self.__ra
    def SetRaza(self, ra):
        self.__ra=ra

    def GetArma(self):
        return self.__ar
    def SetAr(self, ar):
        self.__ar=ar

    def GetVida(self):
        return self.__vi
    def SetVida(self, vi):
        self.__vi=vi
    
    def GetDaño(self):
        return self.__da
    def SetDaño(self, da):
        self.__da=da

    def GetBonificación(self):
        return self.__bo
    def SetBonificación(self, bo):
        self.__bo=bo
    
    def Victoria(self):
        print("Felicidades, has ganado la partida.")
    
    def Derrota(self):
        while self.GetRaza == "Elfo" or "Enano" or "Humano":
            if self.GetRaza == "Elfo":
                return self.Historia
            elif self.GetRaza == "Enano":
                return ("Vamos, vuelve a intentarlo, seguro ganas a la otra.")
            else:
                return ("Vamos, vuelve a intentar, pero selecciona un arma nueva.")
        
    
    def MsjInicial(self):
        print("La Batalla Ha Comenzado")
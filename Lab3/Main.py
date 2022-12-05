from Enano import Enano
from Elfo import Elfo
from Humano import Humano
from random import randint

Personajes=[]

def main():
    enano=Enano("Barbo", "Enano", "Cuchilla", 210, 18, "Aumenta Vida", "Kozuki")
    elfo=Elfo("Floki", "Elfo", "Bastón mágico", 80, 50, "Quita Vida", "Kattegat")
    humano=Humano("Edward", "Humano", "Murakumogiri", 340, 37, "Super Bono", "Newgate")
    Personajes.append(enano)
    Personajes.append(elfo)
    Personajes.append(humano)
    
    p1=randint(0,2)
    p2=randint(0,2)

    if p1 == 0:
        p1 == enano
    elif p1 == 1:
        p1 == elfo
    else:
        p1 == humano
    
    if p2 == 0:
        p2 == enano
    elif p2 == 1:
        p2 == elfo
    else:
        p2 == humano

    while p1 == p2:
            p2=randint(0,2)

    turno=1

    while turno <= 10:
    
        turno=turno+1
        print(Personajes[p1].GetVida())
        print(Personajes[p2].GetVida())
        if turno == 1:
            if p1 == enano:
                aumento=int(input("ingrese un valor entre 50 y 100 para sumar a su vida: "))
                enano.AumentaVida(aumento)
            elif p1 == elfo:
                elfo.QuitaVida()
            else:
                humano.SuperBono()
        
            if p2 == enano:
                enano.AumentaVida()
            elif p2 == elfo:
                elfo.QuitaVida()
            else:
                humano.SuperBono()
        
        Personajes[p1].SetVida(Personajes[p1].GetVida() - Personajes[p2].GetDaño())
        Personajes[p2].SetVida(Personajes[p2].GetVida() - Personajes[p1].GetDaño())

        if Personajes[p1].GetVida() < 0:
            p2.Victoria()
        elif Personajes[p2].GetVida() < 0:
            p1.Victoria()
        else:
            pass

        if turno == 10:
            if Personajes[p1].GetVida() < Personajes[p2].GetVida():
                p2.Victoria()
            elif Personajes[p1].GetVida() > Personajes[p2].GetVida():
                p1.Victoria()
            else:
                print("¡Es un empate!")

main()
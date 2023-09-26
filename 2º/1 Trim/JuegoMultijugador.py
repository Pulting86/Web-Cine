def juego(selA,selB):
    elementos=["Piedra","Papel","Tijera","Lagarto","Spock"]
    jugA=elementos[selA-1]
    jugB=elementos[selB-1]
    ##Piedra
    if jugA=="Piedra" and (jugB=="Tijera" or jugB=="Lagarto"):
        print("Gana el jugador 1")
        return
    elif jugB=="Piedra" and (jugA=="Tijera" or jugA=="Lagarto"):
        print("Gana el jugador 2")
        return

    ##Papel
    if jugA=="Papel" and (jugB=="Spock" or jugB=="Piedra"):
        print("Gana el jugador 1")
        return
    elif jugB=="Papel" and (jugA=="Spock" or jugA=="Piedra"):
        print("Gana el jugador 2")
        return

    ##Tijera
    if jugA=="Tijera" and (jugB=="Papel" or jugB=="Lagarto"):
        print("Gana el jugador 1")
        return
    elif jugB=="Tijera" and (jugA=="Papel" or jugA=="Lagarto"):
        print("Gana el jugador 2")
        return

    ##Lagarto
    if jugA=="Lagarto" and (jugB=="Spock" or jugB=="Papel"):
        print("Gana el jugador 1")
        return
    elif jugB=="Lagarto" and (jugA=="Spock" or jugA=="Papel"):
        print("Gana el jugador 2")
        return

    ##Spock
    if jugA=="Spock" and (jugB=="Tijera" or jugB=="Piedra"):
        print("Gana el jugador 1")
        return
    elif jugB=="Spock" and (jugA=="Tijera" or jugA=="Piedra"):
        print("Gana el jugador 2")
        return


jug1=0
jug2=0




while True:
    print("1.Piedra\n2.Papel\n3.Tijera\n4.Lagarto\n5.Spock")
    while jug1<1 or jug1>5:
        jug1=int(input(""))
    print("1.Piedra\n2.Papel\n3.Tijera\n4.Lagarto\n5.Spock")
    while jug2 < 1 or jug2 > 5:
        jug2 = int(input(""))

    juego(jug1,jug2)
    jug1 = 0
    jug2 = 0

import random

DICCIONARIO: dict = {3: 18, 6: 67, 57: 83, 72: 89, 85: 96, 86: 45, 88: 31, 98: 79, 63: 22, 58: 37, 48: 12, 36: 17}

def mostrar_menu() -> None:
    """POST-CONDICIÓN: imprime el menú para que el usuario pueda tener una visualización amplia y elegir una opción en base a él."""
    print(chr(27)+ "[0;37m" + """                                                          
                                                 ╔════════════════════════════════════════════╗
                                                 ║ ＳＥＲＰＩＥＮＴＥＳ Ｙ ＥＳＣＡＬＥＲＡＳ ║
                                                 ╚════════════════════════════════════════════╝
╔══════╗
║ MENÚ ║
╚══════╝

( 1 ) Iniciar partida

( 2 ) Mostrar estadísticas de casilleros

( 3 ) Resetear estadísticas de casilleros

( 4 ) Salir
""")

def generar_casillero_de_cascara_de_banana(casilleros_especiales: list) -> None:
    """POST-CONDICIÓN: genera los casilleros 'cáscara de banana' de manera aleatoria y los ubica en el tablero."""
    cantidad_de_casilleros_banana: int = 5
    for casillero_banana in range(cantidad_de_casilleros_banana):
        ubicacion: int = random.randint(21, 99)
        while ubicacion in casilleros_especiales[0]["ubicaciones"] or ubicacion in DICCIONARIO.keys() or ubicacion in DICCIONARIO.values():
            ubicacion = random.randint(21, 99)
        casilleros_especiales[0]["ubicaciones"].append(ubicacion)

def generar_casillero_magico(casilleros_especiales: list) -> None:
    """POST-CONDICIÓN: genera los casilleros 'mágicos' de manera aleatoria y los ubica en el tablero."""
    cantidad_de_casilleros_magico: int = 3
    casilleros_posicionados: list = []
    casilleros_posicionados = [ubicacion for casillero_especial in casilleros_especiales for ubicacion in casillero_especial["ubicaciones"]]
    for casillero_magico in range(cantidad_de_casilleros_magico):
        ubicacion: int = random.randint(2, 99)
        while ubicacion in casilleros_especiales[1]["ubicaciones"] or ubicacion in DICCIONARIO.keys() or ubicacion in DICCIONARIO.values() or ubicacion in casilleros_posicionados:
            ubicacion = random.randint(2, 99)
        casilleros_especiales[1]["ubicaciones"].append(ubicacion)

def generar_casillero_rushero(casilleros_especiales: list) -> None:
    """POST-CONDICIÓN: genera el casillero 'rushero' de manera aleatoria y los ubica en el tablero."""
    cantidad_de_casilleros_rushero: int = 1
    casilleros_posicionados: list = []
    casilleros_posicionados = [ubicacion for casillero_especial in casilleros_especiales for ubicacion in casillero_especial["ubicaciones"]]
    maximo_numero_cada_piso: list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for casillero_rushero in range(cantidad_de_casilleros_rushero):
        ubicacion: int = random.randint(2, 100)
        while ubicacion in maximo_numero_cada_piso or ubicacion in casilleros_especiales[2]["ubicaciones"] or ubicacion in DICCIONARIO.keys() or ubicacion in DICCIONARIO.values() or ubicacion in casilleros_posicionados:
            ubicacion = random.randint(2, 100)
        casilleros_especiales[2]["ubicaciones"].append(ubicacion)

def generar_casillero_hongos_locos(casilleros_especiales: list) -> None:
    """POST-CONDICIÓN: genera el casillero 'hongos locos' de manera aleatoria y los ubica en el tablero."""
    cantidad_de_casilleros_hongos_locos: int = 1
    casilleros_posicionados: list = []
    casilleros_posicionados = [ubicacion for casillero_especial in casilleros_especiales for ubicacion in casillero_especial["ubicaciones"]]
    minimo_numero_cada_piso: list = [1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
    for casillero_hongos_locos in range(cantidad_de_casilleros_hongos_locos):
        ubicacion: int = random.randint(1, 99)
        while ubicacion in minimo_numero_cada_piso or ubicacion in casilleros_especiales[3]["ubicaciones"] or ubicacion in DICCIONARIO.keys() or ubicacion in DICCIONARIO.values() or ubicacion in casilleros_posicionados:
            ubicacion = random.randint(1, 99)
        casilleros_especiales[3]["ubicaciones"].append(ubicacion)

def ubicar_casilleros_especiales(casilleros_especiales: list) -> None:
    """POST-CONDICIÓN: reúne todas las funciones que generan casilleros para poder utilizarlas al iniciar una partida."""
    generar_casillero_de_cascara_de_banana(casilleros_especiales)
    generar_casillero_magico(casilleros_especiales)
    generar_casillero_rushero(casilleros_especiales)
    generar_casillero_hongos_locos(casilleros_especiales)

def mostrar_tablero() -> None:
    """POST-CONDICIÓN: muestra el tablero."""
    print(chr(27) + "[2;31m" + """
    ╔═════╦════╦════╦════╦════╦════╦════╦════╦════╦════╗
    ║ 100 ║ 99 ║ 98 ║ 97 ║ 96 ║ 95 ║ 94 ║ 93 ║ 92 ║ 91 ║
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣        ESCALERAS:                                                  
    ║ 81  ║ 82 ║ 83 ║ 84 ║ 85 ║ 86 ║ 87 ║ 88 ║ 89 ║ 90 ║            Casillero 3 ➔  Avanza hasta Casillero 18                 
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 6 ➔  Avanza hasta Casillero 67                  
    ║ 80  ║ 79 ║ 78 ║ 77 ║ 76 ║ 75 ║ 74 ║ 73 ║ 72 ║ 71 ║            Casillero 57 ➔  Avanza hasta Casillero 83                  
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 72 ➔  Avanza hasta Casillero 89                  
    ║ 61  ║ 62 ║ 63 ║ 64 ║ 65 ║ 66 ║ 67 ║ 68 ║ 69 ║ 70 ║            Casillero 85 ➔  Avanza hasta Casillero 96                 
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣                        
    ║ 60  ║ 59 ║ 58 ║ 57 ║ 56 ║ 55 ║ 54 ║ 53 ║ 52 ║ 51 ║        SERPIENTES 🐍:                                              
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 86 ➔  Retrocede hasta Casillero 45              
    ║ 41  ║ 42 ║ 43 ║ 44 ║ 45 ║ 46 ║ 47 ║ 48 ║ 49 ║ 50 ║            Casillero 88 ➔  Retrocede hasta Casillero 31               
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 98 ➔  Retrocede hasta Casillero 79               
    ║ 40  ║ 39 ║ 38 ║ 37 ║ 36 ║ 35 ║ 34 ║ 33 ║ 32 ║ 31 ║            Casillero 63 ➔  Retrocede hasta Casillero 22
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 58 ➔  Retrocede hasta Casillero 37            
    ║ 21  ║ 22 ║ 23 ║ 24 ║ 25 ║ 26 ║ 27 ║ 28 ║ 29 ║ 30 ║            Casillero 48 ➔  Retrocede hasta Casillero 12               
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣            Casillero 36 ➔  Retrocede hasta Casillero 17
    ║ 20  ║ 19 ║ 18 ║ 17 ║ 16 ║ 15 ║ 14 ║ 13 ║ 12 ║ 11 ║                                                                     
    ╠═════╬════╬════╬════╬════╬════╬════╬════╬════╬════╣                                                                        
    ║  1  ║  2 ║  3 ║  4 ║  5 ║  6 ║  7 ║  8 ║  9 ║ 10 ║                                                                        
    ╚═════╩════╩════╩════╩════╩════╩════╩════╩════╩════╝""")

def caer_en_casillero_cascara_de_banana(casilleros_especiales: list, datos_jugador: dict, jugador: str) -> None:
    """POST-CONDICIÓN: chequea si el jugador cae en un casillero "cáscara de banana" y, en caso afirmativo, lo lleva al casillero que corresponda."""
    if datos_jugador["casillero"] in casilleros_especiales[0]["ubicaciones"]:
        datos_jugador["casillero"] -= 20
        casilleros_especiales[0]["contador"] += 1
        print(f"\nEL JUGADOR {jugador} HA CAÍDO EN EL CASILLERO 'CÁSCARA DE BANANA', CAE DOS PISOS Y AHORA ESTÁ EN EL CASILLERO {datos_jugador['casillero']}")
        
def caer_en_casillero_magico(casilleros_especiales: list, datos_jugador: dict, jugador: str) -> None:
    """POST-CONDICIÓN: chequea si el jugador cae en un casillero "mágico" y, en caso afirmativo, lo lleva al casillero que corresponda."""
    if datos_jugador["casillero"] in casilleros_especiales[1]["ubicaciones"]:
        datos_jugador["casillero"] = random.randint(2, 99)
        casilleros_especiales[1]["contador"] += 1
        print(f"\nEL JUGADOR {jugador} HA CAÍDO EN EL CASILLERO 'MÁGICO', SE TELETRANSPORTA AL CASILLERO {datos_jugador['casillero']}")

def caer_en_casillero_rushero(casilleros_especiales: list, datos_jugador: dict, jugador: str) -> None:
    """POST-CONDICIÓN: chequea si el jugador cae en un casillero "rushero" y, en caso afirmativo, lo lleva al casillero que corresponda."""
    if datos_jugador["casillero"] in casilleros_especiales[2]["ubicaciones"]:
        datos_jugador["casillero"] += (10 - (datos_jugador["casillero"] % 10))
        casilleros_especiales[2]["contador"] += 1
        print(f"\nEL JUGADOR {jugador} HA CAÍDO EN EL CASILLERO 'RUSHERO', AVANZA HASTA EL CASILLERO {datos_jugador['casillero']}")

def caer_en_casillero_hongos_locos(casilleros_especiales: list, datos_jugador: dict, jugador: str) -> None:
    """POST-CONDICIÓN: chequea si el jugador cae en un casillero "hongos locos" y, en caso afirmativo, lo lleva al casillero que corresponda."""
    if datos_jugador["casillero"] in casilleros_especiales[3]["ubicaciones"]:
        datos_jugador["casillero"] -= ((datos_jugador["casillero"] % 10) - 1)
        casilleros_especiales[3]["contador"] += 1
        print(f"\nEL JUGADOR {jugador} HA CAÍDO EN EL CASILLERO 'HONGOS LOCOS', RETROCEDE HASTA EL CASILLERO {datos_jugador['casillero']}")

def serpientes_y_escaleras(datos_jugador: dict, escaleras: dict, serpientes: dict, jugador: str) -> None:
    """POST-CONDICIÓN: chequea si el jugador cae en un casillero de escalera o serpiente y, en caso afirmativo, lo lleva al casillero que corresponda."""
    for key in DICCIONARIO:
        if datos_jugador['casillero'] == key:
            llave_casillero_jugador: int = key
            datos_jugador['casillero'] = DICCIONARIO.get(key)

            if datos_jugador['casillero'] > llave_casillero_jugador:
                escaleras["contador"] += 1
                print(f"\nEl jugador {jugador} se ha topado con una ESCALERA! Asciende hasta el casillero {datos_jugador['casillero']}")

            elif datos_jugador['casillero'] < llave_casillero_jugador:
                serpientes["contador"] += 1
                print(f"\nEl jugador {jugador} se ha topado con una SERPIENTE! Desciende hasta el casillero {datos_jugador['casillero']}")

def chequear_caida_en_casillero_especial(casilleros_especiales: list, datos_jugador: dict, escaleras: dict, serpientes: dict, jugador: str) -> None:
    """POST-CONDICIÓN: reúne todas las funciones de casilleros especiales para verificar si el jugador cae en alguno de éstos."""
    serpientes_y_escaleras(datos_jugador, escaleras, serpientes, jugador)
    caer_en_casillero_cascara_de_banana(casilleros_especiales, datos_jugador, jugador)
    caer_en_casillero_hongos_locos(casilleros_especiales, datos_jugador, jugador)
    caer_en_casillero_magico(casilleros_especiales, datos_jugador, jugador)
    caer_en_casillero_rushero(casilleros_especiales, datos_jugador, jugador)

def mostrar_estadisticas(casilleros_especiales: list, se_jugo_partida: bool, escaleras: dict, serpientes: dict) -> None:
    """POST-CONDICIÓN: muestra el contador de cada diccionario incluido en la lista de casilleros especiales y escaleras y serpientes."""
    if se_jugo_partida == False:
        print("\nNo se pueden mostrar las estadísticas porque todavía no se ha jugado una partida. \n")
    else:
        print("\nESTADÍSTICAS:\n")
        for diccionario_casillero in casilleros_especiales:
            print(f"{diccionario_casillero['tipo']}: Se ha caído {diccionario_casillero['contador']} veces en el casillero.\n")
        print(f"{escaleras['tipo']}: Se ha caído {escaleras['contador']} veces en el casillero.\n")
        print(f"{serpientes['tipo']}: Se ha caído {serpientes['contador']} veces en el casillero.")
        
def resetear_estadisticas(casilleros_especiales: list, se_jugo_partida: bool, escaleras: dict, serpientes: dict) -> None:
    """POST-CONDICIÓN: resetea el contador de cada diccionario incluido en la lista de casilleros especiales y escaleras y serpientes."""
    if se_jugo_partida == False:
        print("\nNo se pueden resetear las estadísticas porque todavía no se ha jugado una partida. \n")
    else:
        for diccionario_casillero in casilleros_especiales:
            diccionario_casillero["contador"] = 0
        escaleras["contador"] = 0
        serpientes["contador"] = 0
        print("\nSe han reseteado las estadísticas.\n")

def ronda_jugador(jugador: str, datos_jugador: dict) -> None:
    """POST-CONDICIÓN: tira los dados de forma aleatoria y asigna la nueva posición del jugador."""
    print(chr(27) + "[6;37m" + f"""
EL JUGADOR {jugador} TIRARÁ LOS DADOS 
""")
    texto_tirar_dados: str = input("Inserte cualquier tecla para tirar los dados.\n")
    turno: int = random.randrange(1,7)
    datos_jugador["casillero"] += turno
    print(chr(27) + "[6;37m" + f"El jugador {jugador} tiró los dados. Sacó {turno}, avanza hasta el casillero {datos_jugador['casillero']}")

def partida(casilleros_especiales: list, jugador: str, datos_jugador: dict, escaleras: dict, serpientes: dict, estar_en_partida: bool) -> bool:
    ronda_jugador(jugador, datos_jugador)
    chequear_caida_en_casillero_especial(casilleros_especiales, datos_jugador, escaleras, serpientes, jugador)
    if datos_jugador['casillero'] >= 100:
        datos_jugador['casillero'] = 100
        print(f"""
JUEGO FINALIZADO: Gana el Jugador {jugador} por llegar primero al casillero 100!
        """)
        estar_en_partida = False
    return estar_en_partida
    
def iniciar_partida(casilleros_especiales: list, jugador_1: str, jugador_2: str, primero_en_jugar: int, datos_jugador_1: dict, datos_jugador_2: dict, escaleras: dict, serpientes: dict) -> None:
    """POST-CONDICIÓN: inicia toda la lógica para iniciar una partida dependiendo a qué jugador le toque primero hasta que finalice la misma."""
    estar_en_partida: bool = True

    if 1 == primero_en_jugar:
        mostrar_tablero()
        while (datos_jugador_1['casillero'] < 100 or datos_jugador_2['casillero'] < 100) and estar_en_partida:
            estar_en_partida = partida(casilleros_especiales, jugador_1, datos_jugador_1, escaleras, serpientes, estar_en_partida)
            if estar_en_partida:
                estar_en_partida = partida(casilleros_especiales, jugador_2, datos_jugador_2, escaleras, serpientes, estar_en_partida)
            mostrar_tablero()

    else:
        mostrar_tablero()
        while (datos_jugador_1['casillero'] < 100 or datos_jugador_2['casillero'] < 100) and estar_en_partida:
            estar_en_partida = partida(casilleros_especiales, jugador_2, datos_jugador_2, escaleras, serpientes, estar_en_partida)
            if estar_en_partida:
                estar_en_partida = partida(casilleros_especiales, jugador_1, datos_jugador_1, escaleras, serpientes, estar_en_partida)
            mostrar_tablero()

def main() -> None:
    """POST-CONDICIÓN: principal función en la cual se ejecuta todo el programa."""
    iniciar: bool = True
    se_jugo_partida: bool = False
    casilleros_especiales: list = []
    casilleros_especiales = [
        {"tipo": "Cáscara de banana", "ubicaciones": [], "contador": 0},
        {"tipo": "Mágico", "ubicaciones": [], "contador": 0},
        {"tipo": "Rushero", "ubicaciones": [], "contador": 0},
        {"tipo": "Hongos locos", "ubicaciones": [], "contador": 0},
    ]
    escaleras: dict = {"tipo": "Escalera", "contador": 0}
    serpientes: dict = {"tipo": "Serpiente", "contador": 0}

    while iniciar:
        mostrar_menu()
        seleccionar = input("Ingrese una opción: ")

        while not seleccionar.isnumeric() or not (0 < int(seleccionar) < 5):
            seleccionar = input("\nIngrese una opción válida: \n")

        if seleccionar == "1":
            print("\nJUGADORES: \n")
            jugador_1: str = input("Nombre del jugador 1: \n")
            jugador_2: str = input("\nNombre del jugador 2: \n")
            datos_jugador_2: dict = {'casillero': 1}
            datos_jugador_1: dict = {'casillero': 1}
            primero_en_jugar: int = random.randint(1,2)
            ubicar_casilleros_especiales(casilleros_especiales)

            print(f"""1 PARA EL JUGADOR {jugador_1} Y 2 PARA EL JUGADOR {jugador_2}...\n
                     TOCÓ EL NÚMERO ' {primero_en_jugar} ' """)

            iniciar_partida(casilleros_especiales, jugador_1, jugador_2, primero_en_jugar, datos_jugador_1, datos_jugador_2, escaleras, serpientes)
            for casillero_especial in casilleros_especiales:
                casillero_especial["ubicaciones"] = []
            se_jugo_partida = True

        elif seleccionar == "2":
            mostrar_estadisticas(casilleros_especiales, se_jugo_partida, escaleras, serpientes)
    
        elif seleccionar == "3":
            resetear_estadisticas(casilleros_especiales, se_jugo_partida, escaleras, serpientes)
    
        elif seleccionar == "4":
            print("""
            
            ¡Nos vemos! Gracias por jugar Serpientes y Escaleras.
            
            ... SALIENDO DEL PROGRAMA ...
            
            """)
            iniciar = False

main()





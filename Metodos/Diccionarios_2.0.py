numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers[1])
print(numbers[2])
print(numbers[3])
information = {"nombre" :"Franklin",
               "apellidos": "Ramirez",
               "estatura": "1.75",
               "estado": "True"}
print(information)

#del information["apellidos"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)

pairs = information.items()
print(pairs)
contacts = {"Franklin":{"Apellido":"Ramirez",
                        "Altura":175,
                        "Edad": 30,
                        "Telefono":3162518115,
                        "Signo Zodiacal":"Geminis",
                        "Serie Favorita": "",
                        "Cancion Favorita":"Te Hare Feliz",
                        "Comida Favorita":"Camarones",
                        "Lugar Soñadp Vacaciones":"Paris",
                        "Habilidad Secreta":"Zurdo",
                        "Pasatiempo":"Estudiar",
                        "Heroe O Persona Que Admiras":"Papa",
                        "Libro Que Mas Te Ha Impactado":"",
                        "Cenar Con Alguien":"Mi Familia Completa",
                        "Superpoder":"Perseverancia",
                        "Logro Personal":"Titulo Profesional"
                        },
            "Papa":{"Nombre":"Luis",
                    "Apellido":"Ramirez",
                    "Celular":3162518115,
                    "Signo":"virgo",
                    "Fecha de cumpleaños":"11/sep"}}
print(contacts)
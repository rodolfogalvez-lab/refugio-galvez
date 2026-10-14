"""
Simulación de una día en el refugio
"""

from animal import Animal

Luna = Animal("Luna", "Gato", 3)
Rocky = Animal ("Rocky", "Perro", 5)
Kiwi = Animal("Kiwi", "Loro", 2)

print(Luna.nombre)

#Presentaciones

Luna.presentarse()
Rocky.presentarse()
Kiwi.presentarse()

#Actividad luna
Luna.jugar()
Luna.comer(150)
Luna.dormir()

#Activad Rocky
Rocky.jugar()
Rocky.jugar()
Rocky.jugar()
Rocky.comer(300)

#Actividad Kiwi
Kiwi.comer(100)
Kiwi.dormir()





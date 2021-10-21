from nodo import Nodo

class Pila:
    def __init__(self, max = -1):
        self.tope = None
        self.tamanio = 0
        self.maximo = max


    def ingresar_nuevo(self, id, nombre, apodo, nivel, xp, tipo, movimientos, hp, ataque, defensa, ata_especial, def_especial, velocidad):   
        if self.maximo == -1 or self.tamanio < self.maximo:
            #Crear el nuevo nodo
            nuevo = Nodo(id, nombre, apodo, nivel, xp, tipo, movimientos, hp, 
            ataque, defensa, ata_especial, def_especial, velocidad)
            #Enlazar al nodo viejo
            nuevo.siguiente = self.tope
            #Apunta al nodo nuevo
            self.tope = nuevo
            #Aumentar tama;o de la pila
            self.tamanio += 1
        else:
            #Lanzar error
            raise Exception('ERROR: Desbordamiento de pila')
    
    def recorrer(self):
        aux = self.tope
        contador = 1
        while True:
            if aux == None:
                break
            else:
                print(f"{contador} - {aux}")
                aux = aux.siguiente
                contador = contador + 1
    
    def __str__(self):
        return f"Tamanio: {self.tamanio}\n Max: {self.maximo}\n "
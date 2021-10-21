class Nodo:
  def __init__(self, id, nombre, apodo, nivel, xp, tipo, movimientos, hp, ataque, defensa, ata_especial, def_especial, velocidad):
    # Seccion de datos
    self.id = id
    self.nombre = nombre
    self.apodo = apodo
    self.nivel = nivel
    self.xp = xp
    self.tipo = tipo
    self.movimientos = movimientos
    #Datos de combate
    self.hp = hp
    self.ataque = ataque
    self.defensa = defensa
    self.ata_especial = ata_especial
    self.def_especial = def_especial
    self.velocidad = velocidad
    # Seccion de puntero
    self.siguiente = None
  
  def __str__(self):
        return f"Id {self.id} Nombre {self.nombre} "
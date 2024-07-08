from typing import Any
import pygame
import Recursos.colores as Color

# CLASE MOTO
class Moto(pygame.sprite.Sprite):
    
    def __init__(self,paramX,paramY):
        super().__init__()
        imagen_original = pygame.image.load(".\\sp\\Moto1.png")
        self.image = pygame.transform.scale(imagen_original, (100, 100))  # Escala la imagen a 40x83
        self.rect=self.image.get_rect()
        self.rect.x=paramX
        self.rect.y=paramY
        self.image.set_colorkey(Color.GRIS)
       
        self.carriles = [150, 250, 350]  # Define las posiciones de los carriles
        self.carril_actual = 1  # Comienza en el carril del medio

    def derecha(self):
        if self.carril_actual < 2:  # Si no está en el carril más a la derecha
            self.carril_actual += 1
            self.rect.x = self.carriles[self.carril_actual]  # Mueve la moto al carril de la derecha

    def izquierda(self):
        if self.carril_actual > 0:  # Si no está en el carril más a la izquierda
            self.carril_actual -= 1
            self.rect.x = self.carriles[self.carril_actual]  # Mueve la moto al carril de la izquierda
            
            
            
# CLASE CARRETERA      
class Carretera(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(".\\sp\\Carretera.png")  # Carga la imagen de la carretera
        self.rect = self.image.get_rect()
        self.rect.y = -self.rect.height / 2  
        self.velocidad = 10  # Define la velocidad de la carretera

    def update(self):
        self.rect.y += self.velocidad  # Mueve la carretera hacia abajo
        if self.rect.y > 0:  # Si la carretera ha llegado al borde de la pantalla
            self.rect.y = -self.rect.height / 2  # Vuelve a posicionar la carretera para que la mitad de ella esté por encima de la pantalla



# CLASE AUTO1          
class Auto1(pygame.sprite.Sprite):
    
    def __init__(self,paramX,paramY):
        super().__init__()
        imagen_original = pygame.image.load(".\\sp\\Auto1.png")  # Carga la imagen del auto
        self.image = pygame.transform.scale(imagen_original, (100, 100))  # Escala la imagen a 40x83
        self.rect = self.image.get_rect()
        self.rect.x = paramX
        self.rect.y = paramY
        self.image.set_colorkey(Color.BLANCO)
        self.velocidad = 5  # Define la velocidad del auto

    def mover(self):
        self.rect.y += self.velocidad  # Mueve el auto hacia abajo
    def update(self):
        self.mover()
        


# CLASE CAMION1     
class Camion1(pygame.sprite.Sprite):
    
    def __init__(self,paramX,paramY):
        super().__init__()
        imagen_original = pygame.image.load(".\\sp\\Camion1.png")  # Carga la imagen del Camion
        self.image = pygame.transform.scale(imagen_original, (100, 100))  # Escala la imagen 
        self.rect = self.image.get_rect()
        self.rect.x = paramX
        self.rect.y = paramY
        self.image.set_colorkey(Color.BLANCO)
        self.velocidad = 4  # Define la velocidad 

    def mover(self):
        self.rect.y += self.velocidad  # Mueve el objeto hacia abajo
    def update(self):
        self.mover()
    


# CLASE AUTO2
class Auto2(pygame.sprite.Sprite):
    
    def __init__(self,paramX,paramY):
        super().__init__()
        imagen_original = pygame.image.load(".\\sp\\Auto2.png")  # Carga la imagen del auto
        self.image = pygame.transform.scale(imagen_original, (70, 70))  # Escala la imagen a 40x83
        self.rect = self.image.get_rect()
        self.rect.x = paramX
        self.rect.y = paramY
        self.image.set_colorkey(Color.BLANCO)
        self.velocidad = 5  # Define la velocidad del auto

    def mover(self):
        self.rect.y += self.velocidad  # Mueve el auto hacia abajo
    def update(self):
        self.mover()
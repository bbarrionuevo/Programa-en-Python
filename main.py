import pygame
import sys
import random
import Recursos.constantes as con
import Recursos.colores as colores
import Recursos.clases as core

def main():
    pygame.init()  # inicio pygame
    pygame.mixer.init()  # inicio pygame mixer

    pygame.mixer.music.load('Audios/sonic-sth.mp3')  # Carga la canción
    pygame.mixer.music.play(-1)  # Reproduce la canción en bucle
    AUTO_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(AUTO_EVENT, 7000)  # Crea un auto cada 2000 milisegundos
    
    CAMION_EVENT = pygame.USEREVENT + 2
    pygame.time.set_timer(CAMION_EVENT, 10000)  # Crea un auto cada 2000 milisegundos
    
    #mis objetos
    moto=core.Moto(250,300)
    carretera = core.Carretera()  # Crea la carretera
    auto1 = core.Auto1(250, -100)  # Crea el auto 
    camion1 = core.Camion1(150, -100)  # Crea el auto 

    
    # lista de sprites
    objetos1 = pygame.sprite.Group()
    objetos2 = pygame.sprite.Group()
    carreteras = pygame.sprite.Group()  # Crea un grupo para la carretera
    
   
    # carga de listas
    objetos1.add(moto)
    carreteras.add(carretera)  # Añade la carretera al grupo de carreteras
    objetos2.add(auto1)  # Añade el auto a los objetos
    objetos2.add(camion1)  # Añade el camion a los objetos
    
    #pantalla
    pantalla=pygame.display.set_mode(con.DIM)
    pygame.display.set_caption("¡¡MotoGP!!")
    reloj=pygame.time.Clock()
    
    #loop
    repetir=True
    while repetir:
        for evento in pygame.event.get():
            if evento.type==pygame.QUIT:
                repetir=False
            elif evento.type == pygame.KEYDOWN:  # Detección de tecla presionada
                if evento.key == pygame.K_RIGHT:  # Flecha derecha
                    moto.derecha()
                elif evento.key == pygame.K_LEFT:  # Flecha izquierda
                    moto.izquierda()
            elif evento.type == AUTO_EVENT:  # Evento de aparición de auto
                x_pos = random.choice(con.CARRILES)  # Selecciona una posición aleatoria
                auto1 = core.Auto1(x_pos, -100)  # Crea un nuevo auto
                objetos2.add(auto1)  # Añade el auto a los objetos
                x_pos = random.choice(con.CARRILES)  # Selecciona una posición aleatoria
                auto2 = core.Auto2(x_pos, -100)  # Crea un nuevo auto
                objetos2.add(auto2)  # Añade el auto a los objetos
            elif evento.type == CAMION_EVENT:  # Evento de aparición de camión
                x_pos = random.choice(con.CARRILES)  # Selecciona una posición aleatoria
                camion = core.Camion1(x_pos, -100)  # Crea un nuevo camión
                objetos2.add(camion)  # Añade el camión a los objetos
                    
         # Actualiza los objetos y comprueba las colisiones
        objetos2.update()  # Actualiza los demás objetos
        objetos1.update()  # Actualiza los demás objetos
        if pygame.sprite.spritecollide(moto, objetos2, False):  # Comprueba si la moto ha chocado con algún objeto
            repetir = False  # Termina el juego  
              
        pantalla.fill(colores.BLANCO)
        reloj.tick(30)
        auto1.mover()  # Mueve el auto
        carreteras.update()  # Actualiza la carretera
        carreteras.draw(pantalla)  # Dibuja la carretera
        objetos1.draw(pantalla)  # Dibuja los demás objetos
        objetos2.draw(pantalla)  # Dibuja los demás objetos
        pygame.display.flip()
        
    
    pygame.quit()#salida pygame
    sys.exit()
    
if __name__=="__main__":
    main()
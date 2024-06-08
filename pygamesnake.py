
import pygame
import random




pygame.init()

WIN_SIZE = 800 #Fenster Pixel
SQUARE_COUNT = 20 #Anzahl der Raster
SQUARE_SIZE = WIN_SIZE / SQUARE_COUNT #Größe der Raster


screen= pygame.display.set_mode((WIN_SIZE, WIN_SIZE))#Fesnster größe

pygame.display.set_caption("Snake")#Name vom Fenster

#Zufällige position für snake Kopf
Randomsize = list(range(SQUARE_COUNT))
xSQUARE_SIZE = random.choice(Randomsize)
ySQUARE_SIZE = random.choice(Randomsize)
Randomapple_x = random.choice(Randomsize)
Randomapple_y = random.choice(Randomsize)


Randomsize2 = list(range(SQUARE_COUNT))
xRestart = random.choice(Randomsize2)
yRestart = random.choice(Randomsize2)

#ist eine Liste für körper
body_parts = []
snake_lenght = 10

# Schritte vom Snake
step_x = 0
step_y = 0
#Sound
apfel_collect = pygame.mixer.Sound("mario_coin_sound.mp3")
apfel_collect.set_volume(0.3)
uff_sound = pygame.mixer.Sound("falsche-antwort.mp3.")
uff_sound.set_volume(0.3)
jubel = pygame.mixer.Sound("hsv-torhymne.mp3")
jubel.set_volume(0.1)

#FPS
clock = pygame.time.Clock()

#Score
Score = 0
#Schriftart vom text
schriftart = pygame.font.SysFont("Arial", 45)
#level
level = 0

gruen = (0, 255, 0)
rot = (255, 0, 0)
blau = (0, 0, 255)





l = True

run=True
while run:
    # 100 ms verzögerung
    pygame.time.delay(100)
    clock.tick(60)



    for event in pygame.event.get():
        # Wenn "QUIT" ausgeführt wird dann geht man raus
        if event.type == pygame.QUIT:
            run = False











    # Schritte vom Snake, als erstes bewegt snake sich nicht, weil stepx_xy= 0 sind. Wenn ich eine Taste eingebe wird die Variable step_xy in der nächsten while schleife verändert.
    # Mit "if step_xy" wird verhindert, dass man sich um 180 Grad dreht
    # Erklärung: Wenn ich "Right" drücke UND er sich auf der x Achse nicht nach links bewegt nur dann wird er sich nach rechts bewegen!!

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if step_x != -1:
            step_x = 1
            step_y = 0
    elif keys[pygame.K_LEFT]:
        if step_x != 1:
            step_x = -1
            step_y = 0
    elif keys[pygame.K_UP]:
        if step_y != 1:
            step_x = 0
            step_y = -1
    elif keys[pygame.K_DOWN]:
        if step_y != -1:
            step_x = 0
            step_y = 1
    elif keys[pygame.K_ESCAPE]:
        run=False



    xSQUARE_SIZE += step_x
    ySQUARE_SIZE += step_y


    head_x = xSQUARE_SIZE * SQUARE_SIZE
    head_y = ySQUARE_SIZE * SQUARE_SIZE

    snake_head = pygame.draw.rect(screen, (0, 255, 0), (head_x, head_y, SQUARE_SIZE, SQUARE_SIZE))

    # Wenn der Kopf die selbe Position, wie ein Körperteil hat, dann wird alles zurück gesetzt.
    if (xSQUARE_SIZE, ySQUARE_SIZE) in body_parts:
        body_parts = []
        snake_lenght = 10
        step_x = 0
        step_y = 0
        Score = 0










    # mit append werden neue elemente hinten an der liste angehängt
    body_parts.append((xSQUARE_SIZE, ySQUARE_SIZE))
#Wenn die Länge der body_parts größer als die snake_lenght(10) ist, dann wird der 0. Index der body_parts liste gelöscht(mit befehl "pop"), also die elemente ganz vorne.
    if step_x !=0 or step_y !=0:
        if len(body_parts) >= snake_lenght:
            body_parts.pop(0)





    screen.fill((0, 0, 0))

#Die neue position des kopfes wird zur body_parts liste hinzugefügt
#Die for schleife durchläuft die liste und zeichnet immer die neue position des kopfes
    for part in body_parts:
        part_x = part[0] * SQUARE_SIZE
        part_y = part[1] * SQUARE_SIZE
        pygame.draw.rect(screen, (0, 255, 0), (part_x, part_y, SQUARE_SIZE, SQUARE_SIZE))  # screen= worauf es kommt, 2. Farbe, 3. Koordinate/maße(x,y pixel,)

    # i steht für die Variable in der range von SQUARE_COUNT (1-20), also wird bie line_position, die variable i für die werte 1-20 mit SQUARE_SIZE(40) multipliziert.
    #Dabei ist line_position in den durchläufen von i in der range Squarcount (1-20) immer unterschiedlich da 20 mal squaresize mit dem i (die range 1-20) multipliziert wird.
    for i in range(SQUARE_COUNT):
        line_position = SQUARE_SIZE * i
        pygame.draw.line(screen, (255, 255, 255), (line_position, 0), (line_position, WIN_SIZE), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, line_position), (WIN_SIZE, line_position), 2)







    if head_x < 0 or head_x > 800 or head_y < 0 or head_y > 800:
        uff_sound.play()
        play_sound = False
        body_parts = []
        snake_lenght = 10
        step_x = 0
        step_y = 0
        Score = 0
        level = 0





    #Apfel, eine zufällige Zahl von 1-20 (range(SQUARE_COUNT) wird mit der SQUARE_SIZE(40) multipliziert.
    Appel_x = Randomapple_x * SQUARE_SIZE
    Appel_y = Randomapple_y * SQUARE_SIZE

    Appel = pygame.draw.rect(screen, (255, 255, 0), (Appel_x, Appel_y, SQUARE_SIZE, SQUARE_SIZE))

    if snake_head.colliderect(Appel):
        snake_lenght +=1
        Randomapple_x = random.choice(Randomsize)
        Randomapple_y = random.choice(Randomsize)
        apfel_collect.play()
        Score += 1


    # Text wird gerendert und gezeichnet.
    text = schriftart.render(f"Score:{Score}", True, (0, 0, 255))
    screen.blit(text, (600, -1))

    text = schriftart.render(f"Level:{level}", True, (255, 0, 0))
    screen.blit(text, (400, -1))
    #Zufällige Farbe für snake head
    random_color = list(range(0, 256))
    random_color1 = random.choice(random_color)
    random_color2 = random.choice(random_color)
    random_color3 = random.choice(random_color)

    zufaellige_farbe = (random_color1, random_color2, random_color3)






#Level
    if Score == 10  or Score == 20 or Score == 30 or Score == 40 or Score == 50 or Score == 60 or Score == 70 or Score == 80 or Score == 90:
        snake_head = pygame.draw.rect(screen, (zufaellige_farbe), (head_x, head_y, SQUARE_SIZE, SQUARE_SIZE))
        if l:
            jubel.play()
            level += 1
            l = False

    if Score == 11 or Score == 21 or Score == 31 or Score == 41 or Score == 51 or Score == 61 or Score == 71 or Score == 81 or Score == 91:
        jubel.stop()
        l = True

























    pygame.display.update()

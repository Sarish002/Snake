import pygame
import time
import random
import sys
InterScore = 0
pygame.init()
screen = pygame.display.set_mode((600, 600))
Clock = pygame.time.Clock()
running = True
Score = 3
Color = "green"

music = pygame.mixer.music.load("game-music-loop-6-144641.mp3")
pygame.mixer.music.play(-1)

o = 0
Rect = []
Operation = "MainIndex -= 1"
MainIndex = 620
FruitOrNot = 615
if 170 < FruitOrNot < 1199:
    print("Nice")
for i in range(1200):
        Rect.append(pygame.Rect(((i % 30) * 20, (i // 30) * 20), (20, 20)))

RectIndexX = 300
RectIndexY = 300
Pool = [pygame.Rect((20, 20), (0, 0)) for i in range(Score)]

MainRect = pygame.Rect((RectIndexX, RectIndexY), (20, 20))
F1 = pygame.font.Font("MotleyForcesRegular-w1rZ3.ttf", 30)
Rect3 = pygame.Rect((20, 20), (200, 80))

while running:
    T1 = F1.render(f"Level: {InterScore}", True, "white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("#000000")
    for i in range(1200):
        if i == FruitOrNot:
            pygame.draw.rect(screen, "red", Rect[FruitOrNot])
        if i != MainIndex:
                pass
        else:
            o += 1
            for j in Pool:
                pygame.draw.rect(screen, Color, j, 5)
            pygame.draw.rect(screen, Color, Rect[i], 5)
            for j in range(len(Pool)):
                if j <= len(Pool) - 2:
                    Pool[j] = Pool[j + 1]
                else:
                    Pool[j] = Rect[i]

            if Rect[i].colliderect(Rect[FruitOrNot]):
                Pool.append(pygame.Rect((20, 20), (0, 0)))
                FruitOrNot = random.randint(300, 1157)
                InterScore += 1
                pygame.mixer.Sound("big-crunch-2-90138.mp3").play()

            if InterScore >= 5:
                Color = "purple"

            if InterScore >= 10:
                Color = "brown"

            if InterScore >= 15:
                Color = "pink"

            if InterScore >= 20:
                Color = "orange"

            if InterScore >= 25:
                Color = "yellow"

            if InterScore >= 37.5:
                Color = "blue"

            if InterScore >= 50:
                Color = "turquoise"

            if InterScore >= 60:
                Color = "blanchedalmond"

            if InterScore >= 70:
                Color = "chartreuse"

            if InterScore >= 80:
                Color = "chocolate1"

            if InterScore >= 90:
                Color = "crimson"

            if InterScore >= 100:
                Color = "darkmagenta"

            if InterScore >= 110:
                Color = "darkseagreen1"


            if InterScore >= 120:
                Color = "deeppink2"

            if InterScore >= 130:
                Color = "fuchsia"

            if InterScore >= 140:
                Color = "greenyellow"

            if InterScore >= 150:
                Color = "indianred1"

            if InterScore >= 160:
                Color = "lightcoral"

            if InterScore >= 170:
                Color = "lightsalmon"

            if InterScore >= 180:
                Color = "lightslateblue"

            if InterScore >= 190:
                Color = "mediumslateblue"

            if InterScore >= 200:
                Color = "orchid1"

            if InterScore >= 210:
                    Color = "palevioletred1"

            if InterScore >= 220:
                Color = "papayawhip"

            if InterScore >= 230:
                Color = "violetred3"

            if InterScore >= 240:
                Color = "springgreen"

            if InterScore >= 256:
                Color = "olivedrab1"
                time.sleep(2)
                running = False


            if FruitOrNot % 30 == 0 or FruitOrNot % 30 == 1:
               FruitOrNot = random.randint(300, 1157)

        if MainIndex < -5 or MainIndex > 1200 :
            time.sleep(0.2)
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        Operation = "MainIndex -= 30"
    if keys[pygame.K_DOWN]:
        Operation = "MainIndex += 30"
    if keys[pygame.K_RIGHT]:
        Operation = "MainIndex += 1"
    if keys[pygame.K_LEFT]:
        Operation = "MainIndex -= 1"
    if keys[pygame.K_RCTRL]:
        FruitOrNot = random.randint(300, 1157)
        if FruitOrNot % 30 == 0 or FruitOrNot % 30 == 1:
            FruitOrNot = random.randint(300, 1157)
    pygame.draw.rect(screen, "#000000", rect=Rect3, border_radius=8)
    screen.blit(T1, T1.get_rect(center = (120, 60)))
    exec(Operation)
    time.sleep(0.1)

    pygame.display.update()
    Clock.tick(100)

print(InterScore)
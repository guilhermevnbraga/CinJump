import pygame
import os
from random import randint, shuffle
from time import time


# Função para carregar e tocar uma playlist
def play_playlist(playlist, loop=True):
    # Carregar a primeira música
    pygame.mixer.music.load(playlist[0])
    pygame.mixer.music.play()
    
    current_track = 0
    
    while True:
        if not pygame.mixer.music.get_busy():
            # Se a música atual terminou, carregar a próxima
            current_track += 1
            if current_track >= len(playlist):
                if loop:
                    current_track = 0
                else:
                    break
            pygame.mixer.music.load(playlist[current_track])
            pygame.mixer.music.play()
        
        # Para evitar o uso excessivo da CPU, espere um pouco
        time.sleep(0.1)


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
objects = []
enemy = None
points = 0
running = True
lastTime = time()
dt = 0

# Inicializar o pygame mixer
pygame.mixer.init()

# Caminhos para suas músicas
playlist = [
    r"music\AtDoomsGate.mp3",
    r"music\BFGDivision.mp3",
    r"music\FleshnMetal.mp3",
    r"music\HarbingerDoom.mp3",
    r"music\Hellwalker.mp3",
    r"music\MastermindDoom.mp3",
    r"music\RipnTear.mp3",
    r"music\RustDustnGust.mp3",
    r"music\SkullHacker.mp3",
    r"music\TransistorFist.mp3"
]

shuffle(playlist)

pygame.mixer.music.load(playlist[0])
pygame.mixer.music.play()
current_track = 0

textColor = (250, 204, 21)
font = pygame.font.Font(None, 69)

# Carregar a imagem do player
player_image = pygame.image.load(r"imgs\playe.png").convert_alpha()

# Redimensionar a imagem do player mantendo a proporção
new_width = 222
aspect_ratio = player_image.get_height() / player_image.get_width()
new_height = int(new_width * aspect_ratio)
player_image = pygame.transform.scale(player_image, (new_width, new_height))

# Cria uma máscara para a imagem do player redimensionada
player_mask = pygame.mask.from_surface(player_image)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_rect = player_image.get_rect(center=player_pos)

# Carregar a imagem do inimigo
enemy_image = pygame.image.load(r"imgs\enemigo.png").convert_alpha()

# Redimensionar a imagem do inimigo mantendo a proporção
enemy_new_width = 40
enemy_aspect_ratio = enemy_image.get_height() / enemy_image.get_width()
enemy_new_height = int(enemy_new_width * enemy_aspect_ratio)
enemy_image = pygame.transform.scale(enemy_image, (enemy_new_width, enemy_new_height))

# Girar a imagem do inimigo em 180°
enemy_image = pygame.transform.rotate(enemy_image, 180)

# Cria uma máscara para a imagem do inimigo redimensionada e girada
enemy_mask = pygame.mask.from_surface(enemy_image)
enemy_rect = None

# Carregar a imagem do tiro
laser_image = pygame.image.load(r"imgs\laser.png").convert_alpha()

# Redimensionar a imagem do tiro mantendo a proporção
laser_new_width = 111
laser_aspect_ratio = laser_image.get_height() / laser_image.get_width()
laser_new_height = int(laser_new_width * laser_aspect_ratio)
laser_image = pygame.transform.scale(laser_image, (laser_new_width, laser_new_height))

# Girar a imagem do laser em 90°
laser_image = pygame.transform.rotate(laser_image, 270)

# Girar a imagem do tiro se necessário (por exemplo, 90°)
# laser_image = pygame.transform.rotate(laser_image, 90)

# Cria uma máscara para a imagem do tiro redimensionada
laser_mask = pygame.mask.from_surface(laser_image)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pygame.mixer.music.get_busy():
        # Se a música atual terminou, carregar a próxima
        current_track += 1
        if current_track >= len(playlist):
            if loop:
                shuffle_playlist()  # Embaralhar a playlist antes de repetir
                current_track = 0
            else:
                break
        pygame.mixer.music.load(playlist[current_track])
        pygame.mixer.music.play()

    screen.fill("black")

    screen.blit(player_image, player_rect.topleft)

    pygame.display.set_caption("Polygon Kill")

    text = font.render(f'Score: {points}', True, textColor)
    textPos = text.get_rect(left=20, top=20)
    screen.blit(text, textPos)

    keys = pygame.key.get_pressed()

    if not enemy_rect:
        enemy_pos = pygame.Vector2(randint(0, screen.get_width()), 0)
        enemy_rect = enemy_image.get_rect(topleft=enemy_pos)
    else:
        enemy_rect.y += 300 * dt 
        screen.blit(enemy_image, enemy_rect.topleft)

    if enemy_rect and enemy_rect.y > screen.get_height():
        enemy_rect = None

    # Movimento do player
    if keys[pygame.K_UP]:
        player_pos.y -= 600 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 600 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 600 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 600 * dt

    player_rect.center = player_pos

    if keys[pygame.K_SPACE] and lastTime - time() < -0.25:
        laser_pos = player_pos - pygame.Vector2(5, 60)
        laser_rect = laser_image.get_rect(topleft=laser_pos)
        objects.append(laser_rect)
        lastTime = time()

    # fazer o player sumir quando o inimigo colidir nele
    '''if enemy_rect and enemy_rect.colliderect(player_rect):
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        player_rect = player_image.get_rect(center=player_pos)
        points = 0'''

    if objects:
        for obj in objects:
            if obj.x < 0 or obj.x > screen.get_width() or obj.y < 0 or obj.y > screen.get_height():
                objects.remove(obj)

            if enemy_rect and enemy_rect.colliderect(obj):
                enemy_rect = None
                points += 1

            obj.y -= 1200 * dt
            screen.blit(laser_image, obj.topleft)

    # Limites da tela para o player
    if player_pos.x < 0:
        player_pos.x = 0

    if player_pos.x > screen.get_width():
        player_pos.x = screen.get_width()

    if player_pos.y < 0:
        player_pos.y = 0

    if player_pos.y > screen.get_height():
        player_pos.y = screen.get_height()

    # Verifica colisão usando a máscara
    if enemy_rect:
        offset = (enemy_rect.left - player_rect.left, enemy_rect.top - player_rect.top)
        if player_mask.overlap(enemy_mask, offset):
            print("Colisão detectada!")  # Aqui você pode adicionar lógica para o que acontece na colisão

    pygame.display.flip()

    dt = clock.tick(75) / 1000

pygame.quit()

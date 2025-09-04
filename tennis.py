import pygame, sys, random, os

# === Inisialisasi pygame ===
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tennis Game - Player vs Computer")
clock = pygame.time.Clock()

# === Warna ===
GREEN = (50, 205, 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# === Font ===
font = pygame.font.SysFont("Arial", 32, bold=True)

# === Player & Komputer (paddle) ===
player_width, player_height = 100, 15
player = pygame.Rect(WIDTH//2 - player_width//2, HEIGHT - 40, player_width, player_height)
computer = pygame.Rect(WIDTH//2 - player_width//2, 25, player_width, player_height)

# === Bola ===
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
ball_speed = [5 * random.choice((1, -1)), 5 * random.choice((1, -1))]

# === Skor ===
player_score = 0
computer_score = 0

# === Kecepatan ===
player_speed = 7
computer_speed = 6

# === Sound (opsional, skip kalau file tidak ada) ===
hit_sound = None
score_sound = None
if os.path.exists("assets/hit.wav"):
    hit_sound = pygame.mixer.Sound("assets/hit.wav")
if os.path.exists("assets/score.wav"):
    score_sound = pygame.mixer.Sound("assets/score.wav")

# === Fungsi untuk menggambar objek ===
def draw_objects():
    screen.fill(GREEN)

    # Lapangan (garis tengah = net)
    pygame.draw.line(screen, WHITE, (0, HEIGHT//2), (WIDTH, HEIGHT//2), 3)

    # Paddle & bola
    pygame.draw.rect(screen, WHITE, player)
    pygame.draw.rect(screen, WHITE, computer)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Skor
    score_text = font.render(f"{player_score} : {computer_score}", True, BLACK)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - 20))

# === Game loop ===
while True:
    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Kontrol Player (panah kiri/kanan)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Gerakan komputer (AI sederhana -> ikut bola)
    if computer.centerx < ball.centerx:
        computer.x += computer_speed
    elif computer.centerx > ball.centerx:
        computer.x -= computer_speed

    # Update bola
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Pantulan kiri/kanan
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed[0] = -ball_speed[0]

    # Pantulan player / komputer
    if ball.colliderect(player) or ball.colliderect(computer):
        ball_speed[1] = -ball_speed[1]
        if hit_sound:
            hit_sound.play()

    # Skor
    if ball.top <= 0:  # Player menang poin
        player_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed = [5 * random.choice((1, -1)), 5 * random.choice((1, -1))]
        if score_sound:
            score_sound.play()

    if ball.bottom >= HEIGHT:  # Komputer menang poin
        computer_score += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed = [5 * random.choice((1, -1)), 5 * random.choice((1, -1))]
        if score_sound:
            score_sound.play()

    # Gambar ulang
    draw_objects()
    pygame.display.flip()
    clock.tick(60)

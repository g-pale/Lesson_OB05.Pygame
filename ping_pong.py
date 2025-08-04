import pygame
import sys

# Инициализация
pygame.init()

# Параметры окна
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пинг-Понг")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры ракеток и мяча
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_RADIUS = 7
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Игровые объекты
left_paddle = pygame.Rect(30, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH//2, HEIGHT//2, BALL_RADIUS*2, BALL_RADIUS*2)

# Шрифт
font = pygame.font.SysFont("Arial", 36)

# Счёт
score_left = 0
score_right = 0

# Основной игровой цикл
clock = pygame.time.Clock()

def reset_ball():
    global BALL_SPEED_X, BALL_SPEED_Y
    ball.center = (WIDTH//2, HEIGHT//2)
    BALL_SPEED_X *= -1
    BALL_SPEED_Y *= -1

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Движение мяча
    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # Отскоки от верхнего и нижнего края
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        BALL_SPEED_Y *= -1

    # Отскоки от ракеток
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        BALL_SPEED_X *= -1

    # Проверка на гол
    if ball.left <= 0:
        score_right += 1
        reset_ball()
    if ball.right >= WIDTH:
        score_left += 1
        reset_ball()

    # Отрисовка
    WINDOW.fill(BLACK)
    pygame.draw.rect(WINDOW, WHITE, left_paddle)
    pygame.draw.rect(WINDOW, WHITE, right_paddle)
    pygame.draw.ellipse(WINDOW, WHITE, ball)
    pygame.draw.aaline(WINDOW, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Отображение счета
    left_text = font.render(str(score_left), True, WHITE)
    right_text = font.render(str(score_right), True, WHITE)
    WINDOW.blit(left_text, (WIDTH//4, 20))
    WINDOW.blit(right_text, (WIDTH*3//4, 20))

    pygame.display.flip()

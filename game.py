import pygame
import random
import sys

# --- Константы ---
WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 102, 204)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


# --- Классы ---

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 100
        self.height = 15
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.midbottom = (WIDTH // 2, HEIGHT - 30)
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.x += self.speed


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, RED, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 4 * random.choice((1, -1))
        self.speed_y = -4

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Стенки
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0:
            self.speed_y *= -1
        if self.rect.bottom >= HEIGHT:
            self.kill()  # мяч исчезает, можно добавить перезапуск


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color=GREEN):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


# --- Основная функция ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Арканоид")
    clock = pygame.time.Clock()

    # Спрайты
    all_sprites = pygame.sprite.Group()
    bricks = pygame.sprite.Group()

    paddle = Paddle()
    ball = Ball()
    all_sprites.add(paddle, ball)

    # Создание кирпичей
    for row in range(5):
        for col in range(12):
            brick = Brick(65 * col + 10, 30 * row + 40)
            all_sprites.add(brick)
            bricks.add(brick)

    running = True
    while running:
        clock.tick(FPS)

        # --- События ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- Обновление ---
        all_sprites.update()

        # Отскок мяча от платформы
        if pygame.sprite.collide_rect(ball, paddle):
            ball.speed_y *= -1
            ball.rect.bottom = paddle.rect.top

        # Проверка столкновений с кирпичами
        hit_brick = pygame.sprite.spritecollide(ball, bricks, True)
        if hit_brick:
            ball.speed_y *= -1

        # --- Отрисовка ---
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
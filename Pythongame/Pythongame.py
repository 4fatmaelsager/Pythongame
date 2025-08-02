import pygame
import random

# تهيئة Pygame
pygame.init()

# إعدادات النافذة
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("تحريك الكرة داخل الفريم")

# إعدادات الكرة
x = width // 2
y = height // 2
radius = 25
speed = 10

# الألوان
WHITE = (255, 255, 255)
blue = (0, 0, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# إعدادات الهدف
target_size = 50
target_x = random.randint(0, width - target_size)
target_y = random.randint(0, height - target_size)

# إعدادات العداد
score = 0
font = pygame.font.SysFont(None, 36)
start_ticks = pygame.time.get_ticks()
game_over = False
run = True

while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # حساب الوقت
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000
    if seconds >= 60:
        game_over = True

    screen.fill(black)

    if not game_over:
        # تحكم في الأسهم
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x - radius - speed >= 0:
            x -= speed
        if keys[pygame.K_RIGHT] and x + radius + speed <= width:
            x += speed
        if keys[pygame.K_UP] and y - radius - speed >= 0:
            y -= speed
        if keys[pygame.K_DOWN] and y + radius + speed <= height:
            y += speed

        # التحقق من التصادم
        if (target_x < x < target_x + target_size) and (target_y < y < target_y + target_size):
            score += 1
            target_x = random.randint(0, width - target_size)
            target_y = random.randint(0, height - target_size)

        # رسم الكرة والهدف
        pygame.draw.circle(screen, red, (x, y), radius)
        pygame.draw.rect(screen, blue, (target_x, target_y, target_size, target_size))

        # عرض العداد
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        time_text = font.render(f"Time: {seconds}s", True, WHITE)
        screen.blit(time_text, (10, 50))

    else:
        # شاشة انتهاء الوقت
        game_over_text = font.render("Time's up :(", True, WHITE)
        final_score_text = font.render(f"Your score: {score}", True, WHITE)
        screen.blit(game_over_text, (width // 2 - 80, height // 2 - 40))
        screen.blit(final_score_text, (width // 2 - 100, height // 2 + 10))

    pygame.display.update()

pygame.quit()
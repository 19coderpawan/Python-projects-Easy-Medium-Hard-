import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 600
FPS = 60
GRAVITY = 0.5
FLAP_STRENGTH = -10
PIPE_GAP = 150
PIPE_FREQUENCY = 1500  # milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load images (make sure to have these images in the same directory)
BIRD_IMG = pygame.Surface((34, 24))
BIRD_IMG.fill((255, 255, 0))  # Yellow bird for simplicity

PIPE_IMG = pygame.Surface((52, HEIGHT))
PIPE_IMG.fill((0, 255, 0))  # Green pipe for simplicity


# Game classes
class Bird:
    def __init__(self):
        self.image = BIRD_IMG
        self.rect = self.image.get_rect(center=(100, HEIGHT // 2))
        self.velocity = 0

    def flap(self):
        self.velocity += FLAP_STRENGTH

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity


class Pipe:
    def __init__(self):
        height = random.randint(100, HEIGHT - PIPE_GAP - 100)
        self.top_rect = PIPE_IMG.get_rect(topleft=(WIDTH, height))
        self.bottom_rect = PIPE_IMG.get_rect(topleft=(WIDTH, height + PIPE_GAP))

    def update(self):
        self.top_rect.x -= 5
        self.bottom_rect.x -= 5

    def off_screen(self):
        return self.top_rect.x < -self.top_rect.width


def display_message(screen, message):
    font = pygame.font.Font(None, 74)
    text = font.render(message, True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()


# Main game loop
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    bird = Bird()
    pipes = []
    score = 0

    # Create initial pipes
    pygame.time.set_timer(pygame.USEREVENT, PIPE_FREQUENCY)

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_over:
                    # Restart the game on any key press
                    main()
                    return
                else:
                    bird.flap()

            if event.type == pygame.USEREVENT:
                pipes.append(Pipe())

        if not game_over:
            # Update bird and pipes
            bird.update()

            for pipe in pipes:
                pipe.update()
                if pipe.off_screen():
                    pipes.remove(pipe)
                    score += 1

            # Check for collisions with pipes or ground
            for pipe in pipes:
                if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                    game_over = True

            if bird.rect.y > HEIGHT or bird.rect.y < 0:
                game_over = True

            # Draw everything
            screen.fill(BLACK)
            screen.blit(bird.image, bird.rect)

            for pipe in pipes:
                screen.blit(PIPE_IMG, pipe.top_rect)
                screen.blit(PIPE_IMG, pipe.bottom_rect)

            # Display score (optional)
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {score}', True, WHITE)
            screen.blit(score_text, (10, 10))

        else:
            display_message(screen, "You Lost")

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
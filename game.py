import pygame
import random
import time
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.snake_block = pygame.Surface((20, 20))
        self.snake_block.fill((50, 150, 50))
        self.snake_length = 1
        self.positions = [(100, 100)]
        self.direction = 'right'

    def draw(self):
        for pos in self.positions:
            self.parent_screen.blit(self.snake_block, pos)
    
    def move(self):
        head_x, head_y = self.positions[0]
        
        if self.direction == 'up':
            head_y -= 20
        if self.direction == 'down':
            head_y += 20
        if self.direction == 'left':
            head_x -= 20
        if self.direction == 'right':
            head_x += 20
            
        self.positions.insert(0, (head_x, head_y))
        if len(self.positions) > self.snake_length:
            self.positions.pop()

    def grow(self):
        self.snake_length += 1

    def change_direction(self, new_direction):
        opposite_dirs = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        if new_direction != opposite_dirs[self.direction]:
            self.direction = new_direction

class Food:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.food_block = pygame.Surface((20, 20))
        self.food_block.fill((200, 50, 50))
        self.position = (0, 0)
        self.place_random()
    
    def draw(self):
        self.parent_screen.blit(self.food_block, self.position)
    
    def place_random(self):
        self.position = random.randint(0, 49) * 20, random.randint(0, 49) * 20

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Snake Game")
        self.width, self.height = 1000, 1000
        self.surface = pygame.display.set_mode((self.width, self.height))
        self.snake = Snake(self.surface)
        self.food = Food(self.surface)
        self.score = 0
        self.font = pygame.font.SysFont('Arial', 35)
        self.game_speed = 0.1

    def check_collision(self):
        head_x, head_y = self.snake.positions[0]
        
        # Wall collision
        if head_x < 0 or head_x >= self.width or head_y < 0 or head_y >= self.height:
            return True
            
        # Self collision
        for pos in self.snake.positions[1:]:
            if pos == self.snake.positions[0]:
                return True
                
        return False

    def check_food_collision(self):
        if self.snake.positions[0] == self.food.position:
            self.snake.grow()
            self.food.place_random()
            self.score += 1
            if self.game_speed > 0.04:
                self.game_speed -= 0.005

    def display_score(self):
        score_text = self.font.render(f'Score: {self.score}', True, (0, 0, 0))
        self.surface.blit(score_text, (10, 10))

    def display_game_over(self):
        self.surface.fill((200, 200, 200))
        game_over = self.font.render('Game Over!', True, (200, 0, 0))
        final_score = self.font.render(f'Final Score: {self.score}', True, (0, 0, 0))
        restart = self.font.render('Press R to Restart', True, (0, 0, 0))
        quit_text = self.font.render('Press Q to Quit', True, (0, 0, 0))
        
        self.surface.blit(game_over, (self.width//2 - 80, self.height//2 - 60))
        self.surface.blit(final_score, (self.width//2 - 100, self.height//2 - 20))
        self.surface.blit(restart, (self.width//2 - 100, self.height//2 + 20))
        self.surface.blit(quit_text, (self.width//2 - 80, self.height//2 + 60))
        pygame.display.flip()

    def reset_game(self):
        self.snake = Snake(self.surface)
        self.food = Food(self.surface)
        self.score = 0
        self.game_speed = 0.1

    def run(self):
        running = True
        game_over = False
        
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        running = False
                    if event.key == K_r:
                        game_over = False
                        self.reset_game()
                    
                    if not game_over:
                        if event.key == K_UP:
                            self.snake.change_direction('up')
                        if event.key == K_DOWN:
                            self.snake.change_direction('down')
                        if event.key == K_LEFT:
                            self.snake.change_direction('left')
                        if event.key == K_RIGHT:
                            self.snake.change_direction('right')
            
            if not game_over:
                self.snake.move()
                self.check_food_collision()
                
                if self.check_collision():
                    game_over = True
                
                self.surface.fill((220, 220, 220))
                self.snake.draw()
                self.food.draw()
                self.display_score()
                pygame.display.flip()
                time.sleep(self.game_speed)
            else:
                self.display_game_over()

if __name__ == "__main__":
    game = Game()
    game.run()
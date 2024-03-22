import pygame,sys
from game.my_game import Game
from game.colors import Colors

pygame.init()

game_title_font = pygame.font.Font(None, 40)
game_score_surface = game_title_font.render("Score", True, Colors.black)
game_next_surface = game_title_font.render("Next", True, Colors.black)
game_over_surface = game_title_font.render("GAME OVER", True, Colors.black)

game_bg_image = pygame.image.load('./background.jpg')

game_score_rect = pygame.Rect(320, 55, 170, 60)
game_next_rect = pygame.Rect(320, 215, 170, 180)

game_screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Python Tetris")

game_clock = pygame.time.Clock()

tetris_game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if tetris_game.game_over == True:
				tetris_game.game_over = False
				tetris_game.reset()
			if event.key == pygame.K_LEFT and tetris_game.game_over == False:
				tetris_game.move_left()
			if event.key == pygame.K_RIGHT and tetris_game.game_over == False:
				tetris_game.move_right()
			if event.key == pygame.K_DOWN and tetris_game.game_over == False:
				tetris_game.move_down()
				tetris_game.update_score(0, 1)
			if event.key == pygame.K_SPACE and tetris_game.game_over == False:
				tetris_game.rotate()
		if event.type == GAME_UPDATE and tetris_game.game_over == False:
			tetris_game.move_down()

	#Drawing
	score_value_surface = game_title_font.render(str(tetris_game.score), True, Colors.black)

	game_screen.blit(game_bg_image, (0, 0))
	game_screen.blit(game_score_surface, (365, 20, 50, 50))
	game_screen.blit(game_next_surface, (375, 180, 50, 50))

	if tetris_game.game_over == True:
		game_screen.blit(game_over_surface, (320, 450, 50, 50))

	pygame.draw.rect(game_screen, Colors.light_blue, game_score_rect, 0, 10)
	game_screen.blit(score_value_surface, score_value_surface.get_rect(centerx = game_score_rect.centerx, 
		centery = game_score_rect.centery))
	pygame.draw.rect(game_screen, Colors.light_blue, game_next_rect, 0, 10)
	tetris_game.draw(game_screen)

	pygame.display.update()
	game_clock.tick(60)
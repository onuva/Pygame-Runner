import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		play_scale = 4.2;
		player_run1 = pygame.image.load('Graphics/players/play_run1.png').convert_alpha()
		player_run1 = pygame.transform.scale(player_run1, (player_run1.get_width() * play_scale, player_run1.get_height() * play_scale))
		player_run2 = pygame.image.load('Graphics/players/play_run2.png').convert_alpha()
		player_run2 = pygame.transform.scale(player_run2, (player_run2.get_width() * play_scale, player_run2.get_height() * play_scale))
		player_run3 = pygame.image.load('Graphics/players/play_run3.png').convert_alpha()
		player_run3 = pygame.transform.scale(player_run3, (player_run3.get_width() * play_scale, player_run3.get_height() * play_scale))
		player_run4 = pygame.image.load('Graphics/players/play_run4.png').convert_alpha()
		player_run4 = pygame.transform.scale(player_run4, (player_run4.get_width() * play_scale, player_run4.get_height() * play_scale))
		player_run5 = pygame.image.load('Graphics/players/play_run5.png').convert_alpha()
		player_run5 = pygame.transform.scale(player_run5, (player_run5.get_width() * play_scale, player_run5.get_height() * play_scale))
		player_run6 = pygame.image.load('Graphics/players/play_run6.png').convert_alpha()
		player_run6 = pygame.transform.scale(player_run6, (player_run6.get_width() * play_scale, player_run6.get_height() * play_scale))
		player_run7 = pygame.image.load('Graphics/players/play_run7.png').convert_alpha()
		player_run7 = pygame.transform.scale(player_run7, (player_run7.get_width() * play_scale, player_run7.get_height() * play_scale))
		player_run8 = pygame.image.load('Graphics/players/play_run8.png').convert_alpha()
		player_run8 = pygame.transform.scale(player_run8, (player_run8.get_width() * play_scale, player_run8.get_height() * play_scale))
		self.player_run = [player_run1, player_run2, player_run3, player_run4, player_run5, player_run6, player_run7, player_run8]
		self.player_index = 0

		player_jump1 = pygame.image.load('Graphics/players/play_jump1.png').convert_alpha()
		player_jump1 = pygame.transform.scale(player_jump1, (player_jump1.get_width() * play_scale, player_jump1.get_height() * play_scale))
		player_jump2 = pygame.image.load('Graphics/players/play_jump2.png').convert_alpha()
		player_jump2 = pygame.transform.scale(player_jump2, (player_jump2.get_width() * play_scale, player_jump2.get_height() * play_scale))
		player_jump3 = pygame.image.load('Graphics/players/play_jump3.png').convert_alpha()
		player_jump3 = pygame.transform.scale(player_jump3, (player_jump3.get_width() * play_scale, player_jump3.get_height() * play_scale))
		player_jump4 = pygame.image.load('Graphics/players/play_jump4.png').convert_alpha()
		player_jump4 = pygame.transform.scale(player_jump4, (player_jump4.get_width() * play_scale, player_jump4.get_height() * play_scale))
		self.player_jump = [player_jump1, player_jump2, player_jump3, player_jump4]

		self.image = self.player_run[self.player_index]
		self.rect = self.image.get_rect(bottomleft = (80, 330))
		self.grav = 0

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 330:
			self.grav = -18.5

	def apply_grav(self):
		self.grav += 1
		self.rect.y += self.grav
		if self.rect.bottom > 330: self.rect.bottom = 330

	def anim_state(self):
		if self.rect.bottom < 300: 
			if self.grav >= -20 and self.grav < -10: self.image = self.player_jump[0]
			elif self.grav >= -10 and self.grav < 0: self.image = self.player_jump[1]
			elif self.grav >= 0 and self.grav < 10: self.image = self.player_jump[2]
			else: self.image = self.player_jump[3]
		else:
			self.player_index += 0.35
			if self.player_index >= len(self.player_run): self.player_index = 0
			self.image = self.player_run[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_grav()
		self.anim_state()
		
class Obstacle(pygame.sprite.Sprite):
	def __init__(self, type):
		super().__init__()

		if type == 'fly':
			fly1 = pygame.image.load('Graphics/flies/fly1.png').convert_alpha()
			fly2 = pygame.image.load('Graphics/flies/fly2.png').convert_alpha()
			self.frames = [fly1, fly2]
			y_pos = 210
		else:
			cat_scale = 0.12;
			cat1 = pygame.image.load('Graphics/cats/cat1.png').convert_alpha()
			cat1 = pygame.transform.scale(cat1, (cat1.get_width() * cat_scale, cat1.get_height() * cat_scale))
			cat2 = pygame.image.load('Graphics/cats/cat2.png').convert_alpha()
			cat2 = pygame.transform.scale(cat2, (cat2.get_width() * cat_scale, cat2.get_height() * cat_scale))
			cat3 = pygame.image.load('Graphics/cats/cat3.png').convert_alpha()
			cat3 = pygame.transform.scale(cat3, (cat3.get_width() * cat_scale, cat3.get_height() * cat_scale))
			cat4 = pygame.image.load('Graphics/cats/cat4.png').convert_alpha()
			cat4 = pygame.transform.scale(cat4, (cat4.get_width() * cat_scale, cat4.get_height() * cat_scale))
			cat5 = pygame.image.load('Graphics/cats/cat5.png').convert_alpha()
			cat5 = pygame.transform.scale(cat5, (cat5.get_width() * cat_scale, cat5.get_height() * cat_scale))
			cat6 = pygame.image.load('Graphics/cats/cat6.png').convert_alpha()
			cat6 = pygame.transform.scale(cat6, (cat6.get_width() * cat_scale, cat6.get_height() * cat_scale))
			self.frames = [cat1, cat2, cat3, cat4, cat5, cat6]
			y_pos = 336

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1300), y_pos))

	def anim_state(self):
		self.animation_index += 0.2
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.anim_state()
		self.rect.x -= randint(4, 8)
		self.destroy()

	def destroy(self):
		if self.rect.x <= -70: 
			self.kill()

def display_score():
	curr_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = font.render(f'{curr_time}', False, 'Black')
	score_rect = score_surf.get_rect(center = (400, 50))
	screen.blit(score_surf, score_rect)
	return curr_time

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obst_group,False):
		obst_group.empty()
		return False
	else: return True

def title_anim():
	global play_stand, player_stand_index

	player_stand_index += 0.08
	if player_stand_index >= len(player_stands): player_stand_index = 0
	play_stand = player_stands[int(player_stand_index)]


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pygame Runner')
clock = pygame.time.Clock()
font = pygame.font.Font('Fonts/pixel.ttf', 30)
game_active = False
start_time = 0
score = 0

player = pygame.sprite.GroupSingle()
player.add(Player())

obst_group = pygame.sprite.Group()

sky = pygame.image.load('Graphics/sky.jpeg').convert()
sky = pygame.transform.scale(sky, (932.5, 337.5))
ground = pygame.image.load('Graphics/mground.png').convert()

#Intro screen
play_scale = 4.2;
play_stand1 = pygame.image.load('Graphics/players/play_stand1.png').convert_alpha()
play_stand1 = pygame.transform.scale(play_stand1, (play_stand1.get_width() * play_scale * 2, play_stand1.get_height() * play_scale * 2))
#play_stand = pygame.transform.rotozoom(play_stand, 0, play_scale * 2)
play_stand2 = pygame.image.load('Graphics/players/play_stand2.png').convert_alpha()
play_stand2 = pygame.transform.scale(play_stand2, (play_stand2.get_width() * play_scale * 2, play_stand2.get_height() * play_scale * 2))
play_stand3 = pygame.image.load('Graphics/players/play_stand3.png').convert_alpha()
play_stand3 = pygame.transform.scale(play_stand3, (play_stand3.get_width() * play_scale * 2, play_stand3.get_height() * play_scale * 2))
play_stand4 = pygame.image.load('Graphics/players/play_stand4.png').convert_alpha()
play_stand4 = pygame.transform.scale(play_stand4, (play_stand4.get_width() * play_scale * 2, play_stand4.get_height() * play_scale * 2))
player_stands = [play_stand1, play_stand2, play_stand3, play_stand4]
player_stand_index = 0

play_stand = player_stands[player_stand_index]
play_stand_rect = play_stand.get_rect(center = (400, 200))

title = font.render('Pygame Runner', False, (115, 215, 200))
title_rect = title.get_rect(center = (400, 80))
instruc = font.render('Press SPACE to start', False, (115, 215, 200))
instruc_rect = instruc.get_rect(center = (400, 300))

#Timer
obst_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obst_timer, 1300)



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obst_timer:
				obst_group.add(Obstacle(choice(['cat', 'fly', 'cat', 'cat'])))
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:
		screen.blit(sky, (0,0))
		screen.blit(ground, (0, 330))
		screen.blit(ground, (447, 330))
		score = display_score()

		player.draw(screen)
		player.update()

		obst_group.draw(screen)
		obst_group.update()

		#End game if collide
		game_active = collision_sprite()

	
	else:
		screen.fill((0, 60, 105))
		screen.blit(title, title_rect)
		title_anim()
		screen.blit(play_stand, play_stand_rect)

		score_message = font.render(f'Your score: {score}', False, (115, 215, 200))
		score_message_rect = score_message.get_rect(center = (400, 300))
		
		if score == 0: screen.blit(instruc, instruc_rect)
		else: screen.blit(score_message, score_message_rect)


	pygame.display.update()
	clock.tick(60)




#Credit for cat images:
#Image by <a href="https://www.freepik.com/free-vector/hand-drawn-animation-frames-element-collection_33591451.htm#query=animation%20sprite&position=10&from_view=keyword&track=ais">Freepik</a>
#Credit for bird images:
#Image by <a href="https://www.freepik.com/free-vector/hand-drawn-animation-frames-element-collection_33591451.htm#query=animation%20sprite&position=10&from_view=keyword&track=ais">Freepik</a>
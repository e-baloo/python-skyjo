# Example file showing a circle moving on screen
import pygame
from cards.card_value_enum import CardValueEnum

from cards.deck import Deck
from cards.discard import Discard
from cards.player_board import PlayerBoard


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

img_cards = pygame.image.load('assets/cards.png').convert()

card_width = 104
card_height = 170

sprite_card_back = img_cards.subsurface(
    (card_width * 0, card_height * 0, card_width, card_height))
sprite_card_back.set_alpha(178)
sprite_card_neg_2 = img_cards.subsurface(
    (card_width * 1, card_height * 0, card_width, card_height))
sprite_card_neg_1 = img_cards.subsurface(
    (card_width * 2, card_height * 0, card_width, card_height))
sprite_card_0 = img_cards.subsurface(
    (card_width * 3, card_height * 0, card_width, card_height))
sprite_card_1 = img_cards.subsurface(
    (card_width * 0, card_height * 1, card_width, card_height))
sprite_card_2 = img_cards.subsurface(
    (card_width * 1, card_height * 1, card_width, card_height))
sprite_card_3 = img_cards.subsurface(
    (card_width * 2, card_height * 1, card_width, card_height))
sprite_card_4 = img_cards.subsurface(
    (card_width * 3, card_height * 1, card_width, card_height))
sprite_card_5 = img_cards.subsurface(
    (card_width * 0, card_height * 2, card_width, card_height))
sprite_card_6 = img_cards.subsurface(
    (card_width * 1, card_height * 2, card_width, card_height))
sprite_card_7 = img_cards.subsurface(
    (card_width * 2, card_height * 2, card_width, card_height))
sprite_card_8 = img_cards.subsurface(
    (card_width * 3, card_height * 2, card_width, card_height))
sprite_card_9 = img_cards.subsurface(
    (card_width * 0, card_height * 3, card_width, card_height))
sprite_card_10 = img_cards.subsurface(
    (card_width * 1, card_height * 3, card_width, card_height))
sprite_card_11 = img_cards.subsurface(
    (card_width * 2, card_height * 3, card_width, card_height))
sprite_card_12 = img_cards.subsurface(
    (card_width * 3, card_height * 3, card_width, card_height))
sprite_cards = [sprite_card_neg_2, sprite_card_neg_1, sprite_card_0, sprite_card_1, sprite_card_2, sprite_card_3,
                sprite_card_4, sprite_card_5, sprite_card_6, sprite_card_7,
                sprite_card_8, sprite_card_9, sprite_card_10, sprite_card_11,
                sprite_card_12]

deck = Deck()
player_board = PlayerBoard()
deck.shuffle()
for _ in range(12):
    player_board.append(deck.draw())
player_board.reveal(3, 0)
player_board.reveal(2, 0)

discard = Discard()
discard.append(deck.draw())


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    # screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    for x in range(4):
        for y in range(3):
            card = player_board.get_card(x, y)
            coo = (x * (card_width + 10), y * (card_height + 10))

            if card is not None:
                screen.blit(sprite_cards[card.value], coo,)
                if not card.status.value:
                    screen.blit(sprite_card_back, coo,)

    discard_card = discard.last()
    if discard_card is not None:
        screen.blit(sprite_cards[discard_card.value], (600, 180),)

    draw_card = deck.get()
    if draw_card is not None:
        screen.blit(sprite_cards[draw_card.value], (730, 200),)
        if not draw_card.status.value:
            screen.blit(sprite_card_back, (730, 200),)

    # screen.blit(sprite_card_0, (50, 50),)
    # screen.blit(sprite_card_back, (0, 0),)
    # screen.blit(sprite_card_neg_2, (300, 300),)
    # screen.blit(sprite_card_12, (420, 400),)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()

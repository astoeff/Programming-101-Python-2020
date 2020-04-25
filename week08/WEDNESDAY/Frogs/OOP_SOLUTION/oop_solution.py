from pond import Pond
import constants
import subprocess
import time
import pygame


def print_pond_in_pygame(pond, dis):
    dis.fill((0, 100, 255))
    gray_wall = (0, 255, 100)
    left_frog_image = pygame.image.load('left.png')
    right_frog_image = pygame.image.load('right.jpg')
    position = (13 - len(pond.pond_string)) // 2
    for el in pond.pond_string:
        pygame.draw.rect(dis, gray_wall, [position * 100, 200, 80, 80])
        if el == constants.LEFT_FROG_SYMMBOL:
            dis.blit(left_frog_image, (position * 100, 200))
        elif el == constants.FREE_LILLY_SYMBOL:
            pass
        else:
            dis.blit(right_frog_image, (position * 100, 200))
        pygame.display.update()
        position += 1
    time.sleep(1.5)


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 0, 0))
    return textSurface, textSurface.get_rect()


def message_display(pond, text, dis, lenght = 650, width = 100):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (lenght, (width))
    dis.blit(TextSurf, TextRect)

    pygame.display.update()


if __name__ == '__main__':
    frogs_pers_side = int(input('Enter number of frogs per side: '))
    pond = Pond(frogs_pers_side)
    pond.set_pond_string()
    pygame.init()
    dis = pygame.display.set_mode((1500, 500))
    dis.fill((0, 100, 255))
    pygame.display.set_caption('Frogs Riddle')


    print_pond_in_pygame(pond, dis)
    while not pond.is_arranged():
        pond.move_frog()
        print_pond_in_pygame(pond, dis)

message_display(pond, 'SOLVED!', dis)
message_display(pond, f'In {pond.steps_count} steps', dis, 650, 400)
time.sleep(5)
pygame.quit()
print('\nResult:', pond.pond_string)
print('Solved in: ', pond.steps_count)

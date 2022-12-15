import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    """
    Запуск и инициализация pygame,
    создание отображаемой области в которой будут графические элементы игры:
    создает окно, в которой будет отображаться игра, прописывает название и цвет фона окна
    содержит цикл который обрабатывает действия пользователя игры
    :param screen: создаем дисплей
    :param set_caption: задаем имя дисплею
    :param bg_colour: задаем цвет дисплея
    """

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('SU-27SM')
    bg_colour = (4, 50, 70)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    scor = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_colour, screen, stats, scor, gun, inos, bullets)
            controls.update_bullets(screen,stats, scor, inos, bullets)
            controls.update_inos(stats, screen, scor, gun, inos, bullets)
run()


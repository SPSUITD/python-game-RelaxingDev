import os
from dialog import Dialog
import pygame
from pygame.locals import *
## Инициализация
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
## Цвета
red = (255, 0, 0)
green = (81,220, 55)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
white = (255, 255, 255)
## Экран
screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Sky Door')
## Фоны
mm = pygame.image.load(os.path.join("image\dg", "play1.png"))
mm = pygame.transform.scale(mm,(1000,800))
hl = pygame.image.load(os.path.join("image", "help.png"))

## Шрифт
menu_font = pygame.font.Font("font\gilroy-medium.ttf", 30)
novel_font = pygame.font.Font("font\gilroy-medium.ttf", 40)
## Музыка
pygame.mixer.music.load(os.path.join('audio', 'theme.mp3'))
click = pygame.mixer.Sound(os.path.join('audio','click.mp3'))
## Вывод текста справки и помощи
def printText(txtText, Textfont, Textsize , Textx, Texty, Textcolor):
	myfont = pygame.font.SysFont(Textfont, Textsize)
	label = myfont.render(txtText, 0, Textcolor)
	screen.blit(label, (Textx, Texty))
## Вывод спрайтов персонажей
class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(os.path.join("image\persons", filename))
    def pers(self):
        screen.blit(self.bitmap, (self.x, self.y))
class Fon:
    def __init__(self, xpos, ypos, filename,):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(os.path.join("image", "backgrounds", filename))
    def back(self):
        screen.blit(self.bitmap, (self.x, self.y, 1000, 800))
## Персонажи
gg1 = Sprite(50,240, "gg.png")
vv1 = Sprite(300, 150, "vv.png" )
## Фоны
bg1 = Fon(0,0, "bg1.png")
bg2 = Fon(0,0, "bg2.png")
bg3 = Fon(0,0, "bg3.png")
bg4 = Fon(0,0, "bg3.png")
bg5 = Fon(0,-90, "bg5.png")
bg6 = Fon(0,0, "bg6.png")
bg7 = Fon(0,0, "bg7.png")
glav11=Fon(0,0, "glav11.png")
glav22=Fon(0,0, "glav22.png")

## Создание меню
class Menu:
    ## Покрытие False по-умолчанию
    hovered = False
    ## Инициализация строк меню
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
    ## Рисование и рендер
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
    ## Сам рендер
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
    ## Указание цветов (Покрытый\Не покрытый)
    def get_color(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 105, 225)
    ## Рендер углов
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos
## Главное Меню
def mmenu():
    ## Пункты меню
    menus = [Menu("НОВАЯ ИГРА", (385, 560)),
             Menu("ПОМОЩЬ", (405, 620)),
             Menu("ВЫХОД", (420, 685))]
    begin = True
    screen.blit(mm, (0, 0))
    ## Рабочий цикл
    while begin:
        pygame.event.pump()
        ## Проверка пунктов меню
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "НОВАЯ ИГРА":
                        print("НОВАЯ ИГРА")
                        click.play()
                        glav1()
                    elif menu.hovered and menu.text == "ПОМОЩЬ":
                        print("ПОМОЩЬ")
                        click.play()
                        helps()
                    elif menu.hovered and menu.text == "ВЫХОД":
                        begin = False
                        click.play()
                        pygame.quit()

def helps():
    screen.blit(hl, (0, 0))
    hlp = True
    while hlp:
        printText("Управление Игрой", "gilroy-bold.ttf", 50, 350, 200, green)
        printText("Для продвижения вперед, нажмите пробел или клавишу \"Spacebar\".", "gilroy-bold.ttf", 36, 105, 270, white)
        printText("Для выбора, воспользуйтесь мышью.", "gilroy-bold.ttf", 36, 300, 315, white)
        ###
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                hlp = False
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                hlp = False
                mmenu()

## Новелла
def glav1():
    glav11.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("- Мысли в голове:   Не могу...  открыть глаза...",)
    unNoDialog.show = True
    unNoDialog.next()
    bg2.back()
    menus = [Menu("Как же больно, одни мерцания перед глазами...давай же... ", (30, 620)),
             Menu("Не хочу вставать, не хочу, хочу только спать дальше ", (30, 680))]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Как же больно, одни мерцания перед глазами...давай же... ":
                        print("Концовка-1")
                        click.play()
                        prod1()
                    elif menu.hovered and menu.text == "Не хочу вставать, не хочу, хочу только спать дальше ":
                        print("Продолжение...")
                        click.play()
                        end1()

## Первая концовка
def end1():
    bg2.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы засыпаете и умираете от холода ",)
    unNoDialog.show = True
    unNoDialog.next()
    screen.fill((0, 0, 0))
    while True:
        printText("Вы проиграли, начните игру заново", "gilroy-bold.ttf", 40, 230, 300, red)
        printText("Нажмите -SPACEBAR- для того чтобы выйти в меню ", "gilroy-medium.ttf", 35, 159, 360, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                mmenu()

## Идем дальше
def prod1():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы просыпаетесь в маленьком и очень тесном месте.",)
    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Вы чувствуете, что лежите на холодном  металлическом полу.",)
    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Глаза, будто заковали в цепи, вам с трудом.",
                          "удается открыть хотя бы один глаз.",)
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Чёрт! Где я?", (30, 640)),
             Menu("Чёрт, Кто я?", (30, 700)),]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Чёрт! Где я?":
                        print("Продолжение2")
                        click.play()
                        prod2()
                    elif menu.hovered and menu.text == "Чёрт, Кто я?":
                        print("Продолжение3")
                        click.play()
                        prod3()

# Продолжение2
def prod2():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Бортовой ИИ:  Ваши координаты, 59 382 9394 47372 0032 ",)
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Стой, стой, стой, а можно буквами? ", (30, 640)),
             Menu("И что мне делать? ", (30, 700)),]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Стой, стой, стой, а можно буквами? ":
                        print("Продолжение4")
                        click.play()
                        prod4()
                    elif menu.hovered and menu.text == "И что мне делать? ":
                        print("Продолжение5")
                        click.play()
                        prod5()

def prod3():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Проводится диагностика...20%...60%...100%...Диагностика закончена ",
                          "о вас известно только то, что вы как минимум из расы -человек- ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("А я думал я вареный арбуз, ладно, скажи мне где я ", (30, 640)),
             Menu("А что я тут делаю? ", (30, 700)),]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "А я думал я вареный арбуз, ладно, скажи мне где я ":
                        print("Продолжение4")
                        click.play()
                        prod4()
                    elif menu.hovered and menu.text == "А что я тут делаю? ":
                        print("Продолжение5")
                        click.play()
                        prod5()

def prod4():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Бортовой ИИ: Исходя из вашего прошлого местоположения, ",
                          "вы находитесь за солнечной системой ",)
    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Бортовой ИИ: Я думаю вам срочно нужно поднять уровень тепла в каюте.",)
    unNoDialog.show = True
    menus = [Menu("К-как, я же должен быть на луне... Скажи мне, как попасть обратно? ", (10, 640)),
            Menu("Впервые вижу такой корабль, ИИ, включи отопление за меня ", (10, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "К-как, я же должен быть на луне... Скажи мне, как попасть обратно? ":
                        print("Продолжение2")
                        click.play()
                        prod5()
                    elif menu.hovered and menu.text == "Впервые вижу такой корабль, ИИ, включи отопление за меня ":
                        print("Продолжение5")
                        click.play()
                        prod6()

def prod5():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Бортовой ИИ: В торговом порту, планеты Меркурий, сюда вас ",
                          "лично привел Герд-Маршал Руклер, вы сели и назвали точку полета ",)
    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Облачная зона добывающих станций ")
    unNoDialog.show = True
    unNoDialog.message = ("К сожалению для того чтобы вернуться назад, нужно 8 ",
                          "флашек кристалического топлива. Спешу дать вам совет, ",
                          "сейчас нам лучше долететь до ближайшей добывающей станции.",
                          "Возможно там мы сможем заправиться ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Э? ", (30, 620)),
            Menu("Тогда, кхм, О МОЙ БРАВЫЙ ВОИН, ЛЕТИМ К СТАНЦИИ! ", (30, 680)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Э? ":
                        print("Продолжение2")
                        click.play()
                        prod7()
                    elif menu.hovered and menu.text == "Тогда, кхм, О МОЙ БРАВЫЙ ВОИН, ЛЕТИМ К СТАНЦИИ! ":
                        print("Продолжение5")
                        click.play()
                        prod7()

def prod6():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Для спасения экипажа активирую элемент отопления ",)
    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Какой у вас будет приказ? ",)
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Расскажи мне про модель коробля ", (50, 640)),
            Menu("Расскажи что я тут делаю ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Расскажи мне про модель коробля ":
                        print("Продолжение2")
                        click.play()
                        prod8()
                    elif menu.hovered and menu.text == "Расскажи что я тут делаю ":
                        print("Продолжение5")
                        click.play()
                        prod5()

def prod8():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Это выпускной модуль коробля -NE6- ",
                          "Данный корабль обладает двумя отсеками еды ",
                          "на год и тремя ускорителями для маневров ",)
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Не густо, зато от голода не умру, но как мне попасть домой ", (50, 640)),
            Menu("... ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Не густо, зато от голода не умру, но как мне попасть домой ":
                        print("Продолжение2")
                        click.play()
                        prod5()
                    elif menu.hovered and menu.text == "... ":
                        print("Продолжение5")
                        click.play()
                        prod5()

def prod7():
    glav22.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Полет будет длиться 4 часа 19 минут ",
                          "Для комфортного проведения полета для вас ",
                          "будет подготовлен обед и новое белье ",)

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("*Нажмите два раза на Spacebar* ",)
    unNoDialog.show = True
    unNoDialog.next()
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                glav2()
            elif event.type == pygame.KEYDOWN:
                click.play()
                glav2()

def glav2():
    bg3.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("При приближении к станции вы стали видеть солнечную систему ",
                          "Её больше не покрывал туман, и вы увидели, что по строению ",
                          "Планет, система напоминала чем то солнечную, только тут ",
                          "Другие цвета ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("ИИ, расскажи про эту добывающую станцию ", (50, 640)),
             Menu("Ты был тут когда-нибудь? ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "ИИ, расскажи про эту добывающую станцию ":
                        print("Продолжение9")
                        click.play()
                        prod9()
                    elif menu.hovered and menu.text == "Ты был тут когда-нибудь? " :
                        print("Продолжение10")
                        click.play()
                        prod10()


def prod9():
    bg3.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Бортовой ИИ: Данная станция называется -Hibli3- ",
                          "На ней добывают кристаллы для переплавки в топливо ",
                          "На эту станцию ввозят людей раз в 20 лет ",
                          "Поэтому тут они живут и строят дома ",
                          "Советую вам быть осторожным, люди не любят новых ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Так понял, у нас есть на палубе оружее? ", (50, 640)),
             Menu("А нам уже нельзя развернуться и улететь? ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Так понял, у нас есть на палубе оружее? ":
                        print("Продолжение11")
                        click.play()
                        prod11()
                    elif menu.hovered and menu.text == "А нам уже нельзя развернуться и улететь? " :
                        print("Продолжение12")
                        click.play()
                        prod12()

def prod10():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Бортовой ИИ: Нет, я всю свою короткую жизнь ",
                          "существовал в солнечной системе и видел ",
                          "только луну, но у меня есть синхронизация ",
                          "с справочником по данной системе ",
                          "вам зачитать 15675 страниц? ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Прошу помилуй, не надо, у меня все еще голова болит ", (50, 640)),
             Menu("Ага, лучше скажи мне, скоро до станции? ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Прошу помилуй, не надо, у меня все еще голова болит ":
                        print("Продолжение9")
                        click.play()
                        prod12()
                    elif menu.hovered and menu.text == "Ага, лучше скажи мне, скоро до станции? " :
                        print("Продолжение10")
                        click.play()
                        prod12()

def prod11():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("К сожалению спасательный модуль не владеет ",
                          "Никаким вооружением, даже переносным ",
                          "Но я могу вам предложиь взять с собой перец ",
                          "О, неожиданность, мы подлетаем ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("О, кажется я вижу станцию! ", (50, 640)),
             Menu("... ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "О, кажется я вижу станцию! ":
                        print("Продолжение9")
                        click.play()
                        prod12()
                    elif menu.hovered and menu.text == "... " :
                        print("Продолжение10")
                        click.play()
                        prod12()

def prod12():
    bg5.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Подлетаем к станции, знаете, Герд-маршал ",
                          "Заложил в меня указания по тому, как заправляться ",
                          "В добывающих станциях ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Что за указания? ", (50, 640)),
             Menu("Сразу говори, что мне делать ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Что за указания? ":
                        print("Продолжение9")
                        click.play()
                        prod13()
                    elif menu.hovered and menu.text == "Сразу говори, что мне делать " :
                        print("Продолжение10")
                        click.play()
                        prod13()


def prod13():
    bg5.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("При состыковке к станции, я без специального разрешения ",
                          "буду одалживать немного топлива для себя ",
                          "Тем временем, вы будете должны отвлечь на себя внимание ",
                          "Жителей станции ",
                          "Заправка займет у меня 6 минут ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Я все понял, импровизируем ", (50, 640)),
             Menu("Расскажи побольше о жителях ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Я все понял, импровизируем ":
                        print("Продолжение9")
                        click.play()
                        prod14()
                    elif menu.hovered and menu.text == "Расскажи побольше о жителях " :
                        print("Продолжение10")
                        click.play()
                        prod15()

def prod14():
    bg6.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Тогда готовьтесь, пристыковываемся ",
                          "5....4....3....2....1 ")

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Нажмите два раза на spacebar ")
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                prod16()
            elif event.type == pygame.KEYDOWN:
                click.play()
                prod16()

def prod15():
    bg6.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Средний возраст жителей: 42+- ",
                          "Основное хобби: азартные игры ",
                          "Родная планета: Марс ",
                          "Музыкальные вкусы: Шансон, Рок ",
                          "Пристыковка через 5...4...3...2...1... ")

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("... ", (50, 640)),
             Menu("Я все понял, импровизируем ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "... ":
                        print("Продолжение1")
                        click.play()
                        prod16()
                    elif menu.hovered and menu.text == "Я все понял, импровизируем " :
                        print("Продолжение10")
                        click.play()
                        prod16()

def prod16():
    bg7.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: Назовите номер корабля! ",
                          "Назовите свое имя, вы у нас не записаны как ",
                          "прибывающий ",)

    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Здравствйте, у нас экстренная ситуация ", (50, 640)),
             Menu("Я должен быть в списке, меня отправили починить что-то ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Здравствйте, у нас экстренная ситуация ":
                        print("Продолжение1")
                        click.play()
                        prod17()
                    elif menu.hovered and menu.text == "Я должен быть в списке, меня отправили починить что-то " :
                        print("Продолжение10")
                        click.play()
                        prod18()

def prod17():
    bg7.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: И что? Мы тут причем? ",
                          "Улетайте отсюда, нас и так тут много ",
                          "ИИ: скажите им, что вы торговец ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Я...я торговец, мне нужно спасти свои товары, их очень много ", (50, 640)),
             Menu("А если я вам заплачу? ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Я...я торговец, мне нужно спасти свои товары, их очень много ":
                        print("Продолжение1")
                        click.play()
                        prod18()
                    elif menu.hovered and menu.text == "А если я вам заплачу? ":
                        print("Продолжение10")
                        click.play()
                        prod20()

def prod18():
    bg7.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: У нас и на борту достаточно ",
                          "персонала обслуживания так что проваливайте ")

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("ИИ: Осталось 3 минуты, тяните время ",)
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Хорошо, только дайте время отсоединиться от вас ", (50, 640)),
             Menu("Я отказываюсь... ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Хорошо, только дайте время отсоединиться от вас ":
                        print("Продолжение1")
                        click.play()
                        prod19()
                    elif menu.hovered and menu.text == "Я отказываюсь... ":
                        print("Продолжение10")
                        click.play()
                        prod19()

def prod19():
    bg7.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: Даю 30 секунд ",
                          "Иначе... ",
                          "Голос старика: ОНИ ОТКАЧИВАЮТ ТОПЛИВО!!! ")

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Неизвестный голос: Доставайте пушки мужики ",
                          "сейчас мы их оттуда выкурим ",
                          "и посмотрим кто там сидит ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("ИИ, дело очень плохо они с пушками сюда сейчас завалятся ", (50, 640)),
             Menu("А как вы этими пукалками пробьете обшивку? ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "ИИ, дело очень плохо они с пушками сюда сейчас завалятся ":
                        print("Продолжение1")
                        click.play()
                        prod21()
                    elif menu.hovered and menu.text == "А как вы этими пукалками пробьете обшивку? " :
                        print("Продолжение10")
                        click.play()
                        prod21()

def prod20():
    bg7.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: А зачем мне твои ",
                          "деньги, лучше плати проход коробкой пива ",
                          "Иначе... ",
                          "Голос старика: ОНИ ОТКАЧИВАЮТ ТОПЛИВО!!! ")

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("Неизвестный голос: Доставайте пушки мужики ",
                          "сейчас мы их оттуда выкурим ",
                          "и посмотрим кто там сидит ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("ИИ, дело очень плохо они с пушками сюда сейчас завалятся ", (50, 640)),
             Menu("Могу только вам мочу предложить ребята ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "ИИ, дело очень плохо они с пушками сюда сейчас завалятся ":
                        print("Продолжение1")
                        click.play()
                        prod21()
                    elif menu.hovered and menu.text == "Могу только вам мочу предложить ребята " :
                        print("Продолжение10")
                        click.play()
                        prod21()

def prod21():
    bg1.back()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Неизвестный голос: Вскрывайте эту консервную банку ",)

    unNoDialog.show = True
    unNoDialog.next()
    unNoDialog.message = ("ИИ: заправка закончена, можем улетать ",
                          "Вы отдаете приказ об отлете? ")
    unNoDialog.show = True
    unNoDialog.next()
    menus = [Menu("Конечно! Быстрее прошу тебя ", (50, 640)),
             Menu("Не, тут посидим ", (50, 700)), ]
    while True:
        pygame.event.pump()
        for menu in menus:
            if menu.rect.collidepoint(pygame.mouse.get_pos()):
                menu.hovered = True
            else:
                menu.hovered = False
            menu.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for menu in menus:
                    if menu.hovered and menu.text == "Конечно! Быстрее прошу тебя ":
                        print("Продолжение1")
                        click.play()
                        end3()
                    elif menu.hovered and menu.text == "Не, тут посидим " :
                        print("Продолжение10")
                        click.play()
                        end2()

def end2():
    bg7.back()
    vv1.pers()
    gg1.pers()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вам вскрывают модуль и захватывают в плен ",)
    unNoDialog.show = True
    unNoDialog.next()
    screen.fill((0, 0, 0))
    while True:
        printText("Вы проиграли, начните игру заново ", "gilroy-bold.ttf", 40, 230, 300, red)
        printText("Нажмите -SPACEBAR- для того чтобы выйти в меню ", "gilroy-medium.ttf", 35, 159, 360, red)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                mmenu()

def end3():
    bg2.back()
    unNoDialog = Dialog(screen)
    unNoDialog.message = ("Вы и ваш помошник смогли заправиться и успешно улететь ",
                          "обратно на вашу родную планету с полным баком ")
    unNoDialog.show = True
    unNoDialog.next()
    screen.fill((0, 0, 0))
    while True:
        printText("Спасибо за прохождение истории о путешествии космонавта!", "gilroy-bold.ttf", 40, 55, 300, green)
        printText("Нажмите -SPACEBAR- для того чтобы выйти в меню ", "gilroy-medium.ttf", 35, 159, 360, white)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                click.play()
                mmenu()
            elif event.type == pygame.KEYDOWN:
                click.play()
                mmenu()

def main():
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    mmenu()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


## Запуск программы
if __name__ == "__main__":
    main()

pygame.quit()
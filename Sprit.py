import pygame
win = pygame.display.set_mode((1600, 670))
#background

image_path = '/data/data/org.test.myapp/files/app/'


bg = [pygame.image.load(image_path + 'pic\\bg\\stom-land-0.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-1.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-2.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-3.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-4.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-6.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-7.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-8.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-9.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-10.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-11.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-12.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-13.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-14.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-15.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-16.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-17.png').convert(),pygame.image.load(image_path + 'pic\\bg\\stom-land-18.png').convert(),
      pygame.image.load(image_path + 'pic\\bg\\stom-land-19.png').convert()]

#stand l
#sl = [pygame.image.load("pic\\dr\\1.png"),pygame.image.load("pic\\dr\\2.png"),pygame.image.load("pic\\dr\\3.png"),
     # pygame.image.load("pic\\dr\\4.png"),pygame.image.load("pic\\dr\\5.png"),pygame.image.load("pic\\dr\\6.png"),
     # pygame.image.load("pic\\dr\\7.png"),pygame.image.load("pic\\dr\\8.png"),pygame.image.load("pic\\dr\\9.png"),
     # pygame.image.load("pic\\dr\\10.png"),pygame.image.load("pic\\dr\\11.png"),pygame.image.load("pic\\dr\\12.png"),
     # pygame.image.load("pic\\dr\\13.png"),pygame.image.load("pic\\dr\\14.png"),pygame.image.load("pic\\dr\\15.png"),
     # pygame.image.load("pic\\dr\\16.png"),pygame.image.load("pic\\dr\\17.png"),pygame.image.load("pic\\dr\\18.png"),
     # pygame.image.load("pic\\dr\\19.png"),pygame.image.load("pic\\dr\\20.png"),pygame.image.load("pic\\dr\\21.png"),
     # pygame.image.load("pic\\dr\\22.png"),pygame.image.load("pic\\dr\\23.png"),pygame.image.load("pic\\dr\\24.png"),
     # pygame.image.load("pic\\dr\\25.png"),pygame.image.load("pic\\dr\\26.png"),pygame.image.load("pic\\dr\\27.png"),
     # pygame.image.load("pic\\dr\\28.png"),pygame.image.load("pic\\dr\\29.png"),pygame.image.load("pic\\dr\\30.png")]

#stand r
sr = [pygame.image.load(image_path + "pic\\d\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\d\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\d\\30.png").convert_alpha()]

l = [pygame.image.load(image_path + "pic\\l\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\l\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\l\\19.png").convert_alpha(),pygame.image.load(image_path + image_path + "pic\\l\\20.png").convert_alpha()]

r = [pygame.image.load(image_path + "pic\\r\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\r\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\r\\20.png").convert_alpha()]

jl = [pygame.image.load(image_path + "pic\\jl\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jl\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\jl\\24.png").convert_alpha()]


jr = [pygame.image.load(image_path + "pic\\jr\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\jr\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\jr\\24.png").convert_alpha()]

item = [pygame.image.load(image_path + "pic\\item\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\3.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\6.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\9.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\item\\12.png").convert_alpha(),
        pygame.image.load(image_path + "pic\\item\\13.png").convert_alpha()]

rect1 = pygame.image.load(image_path + "pic\\rect1.png")
rect2 = pygame.image.load(image_path + "pic\\rect2.png")


start = [pygame.image.load(image_path + "pic\\start\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\start\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\start\\30.png").convert_alpha()]

over = [pygame.image.load(image_path + "pic\\over\\1.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\2.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\3.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\4.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\5.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\6.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\7.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\8.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\9.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\10.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\11.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\12.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\13.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\14.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\15.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\16.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\17.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\18.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\19.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\20.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\21.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\22.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\23.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\24.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\25.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\26.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\27.png").convert_alpha(),
      pygame.image.load(image_path + "pic\\over\\28.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\29.png").convert_alpha(),pygame.image.load(image_path + "pic\\over\\30.png").convert_alpha()]

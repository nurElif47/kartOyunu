import random
WIDTH=500
HEIGHT=500
odul=Actor("one")
odul.topleft=(WIDTH, HEIGHT)
oduller=[]
def on_mouse_down():
    for i in range(5):
        odul=Actor("one")
        x=random.randrange(odul.width,WIDTH-odul.width)
        odul.center=(x,0)
        oduller.append(odul)
def draw():
    screen.fill("gray")
    for odul in oduller:
        odul.draw()
def update():
    for odul in oduller:
        y_artis=random.randrange(1,20)
        odul.y+=y_artis

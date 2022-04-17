from pygame import* 
from time import clock


font.init()
font = font.SysFont('Arial', 40)


class GameSprite(sprite.Sprite):

    def __init__(self, sprite1_image, sprite1_x,  sprite1_y, sprite1_vesota, sprite1_dlinna):
        super().__init__()
        self.image = transform.scale(image.load(sprite1_image), (sprite1_dlinna, sprite1_vesota))
        self.vesota = sprite1_vesota
        self.dlinna = sprite1_dlinna
        self.rect = self.image.get_rect()
        self.rect.x = sprite1_x
        self.rect.y = sprite1_y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

O_x = 700
O_y = 500

window = display.set_mode((O_x, O_y))
display.set_caption('Platforma')

clock = time.Clock()
FPS = 60


back_g = transform.scale(image.load("Fon.jpg"), (700, 500))
stena1 = GameSprite(('steni 2.jpg'), 200, 200, 35, 100)
stena2 = GameSprite(('steni.jpg'), 350, 200, 35, 100)
stena3 = GameSprite(('steni.jpg'), 500, 200, 35, 100)
stena4 = GameSprite(('steni 2.jpg'), 100, 200, 35, 100)









game = True 

finish = False

while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False

        if finish != True:

            window.blit(back_g, (0, 0))
            stena1.reset()
            stena2.reset()
            stena3.reset()
            stena4.reset()






    display.update()
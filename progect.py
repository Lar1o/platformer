from pygame import* 
from time import clock


font.init()
font = font.SysFont('Arial', 40)


class GamePlatform(sprite.Sprite):

    def __init__(self, sprite1_image, sprite1_x,  sprite1_y, sprite1_vesota, sprite1_dlinna):
        super().__init__()
        self.image = transform.scale(image.load(sprite1_image), (sprite1_dlinna, sprite1_vesota))
        self.vesota = sprite1_vesota
        self.dlinna = sprite1_dlinna
        self.rect = self.image.get_rect()
        self.rect.x = sprite1_x*50
        self.rect.y = sprite1_y*35
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

O_x = 700
O_y = 500

window = display.set_mode((O_x, O_y))
display.set_caption('Platforma')

clock = time.Clock()
FPS = 60


steni = []


with open('Setka.txt', 'r') as file:
    data = file.readlines()
    print(data)
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == '1':
                steni.append(GameSprite(('steni 2.jpg'), j, i, 35, 50))

back_g = transform.scale(image.load("Fon.jpg"), (700, 500))

game = True 

finish = False

while game != False:

    for e in event.get():

        if e.type == QUIT:

            game = False

        if finish != True:

            window.blit(back_g, (0, 0))
            for stena in steni:
                stena.reset()
           


    display.update()
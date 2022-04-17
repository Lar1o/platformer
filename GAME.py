from pygame import *
font.init()
window = display.set_mode((500,500))
back = (0, 0, 0)
window.fill(back)
font1 = font.SysFont('Corbel',35)
class Button():
    def __init__(self,x,y,width,height,color,fill_color,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = font.SysFont('verdana', 35).render(text, True, color)
        self.image = Surface((width,height),SRCALPHA)
        # text1 = font1.render(text, True , (0,250,0))
        self.image.fill(fill_color)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

    def color(self,new_color):
        self.fill_color = new_color

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def reset(self):
        # draw.rect(window,self.image,self.rect)
        window.blit(self.label ,(self.x,self.y))
        window.blit(self.image , self.rect)



button_1 = Button(300,250,180,50,(250, 0, 0),(0, 250, 0, 0),'Уровень 2')
button_2 = Button(100,100,350,50,(250, 0 , 0),(0, 250, 0, 0),'Выберите уровень')
button_3 = Button(50,250,180,50,(250, 0 , 0),(0, 250, 0, 0),'Уровень 1')
button_4 = Button(170,350,180,50,(250, 0 , 0),(0, 250, 0, 0),'Уровень 3')
go = True

while go:
    display.update()
    button_1.reset()
    button_2.reset()
    button_3.reset()
    button_4.reset()

    for e in event.get():
        if e.type == QUIT:
            go = False

        if e.type == MOUSEBUTTONDOWN:
            x,y = e.pos

            if button_1.collidepoint(x,y):
                go = False

            if button_3.collidepoint(x,y):
                go = False

            if button_4.collidepoint(x,y):
                go = False

display.update()





from pygame import *
font.init()
window = display.set_mode((500,500))
back = (228, 122, 223)
window.fill(back)
font1 = font.SysFont('Corbel',35)
class Button():
    def __init__(self,x,y,width,height,color,fill_color,text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = font.SysFont('verdana', 35).render(text, True, color)
        self.rect = Rect(x,y,width,height)
        self.fill_color = fill_color
        # text1 = font1.render(text, True , (0,250,0))

    def color(self,new_color):
        self.fill_color = new_color

    def reset(self):
        draw.rect(window,self.fill_color,self.rect)
        window.blit(self.label ,(self.x,self.y))



button_1 = Button(300,200,20,40,(250,0,0),(0,250,0),'Go')



go = True
while go:
    display.update()
    button_1.reset()


    for e in event.get():
        if e.type == QUIT:
            go = False
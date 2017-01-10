import pygame as pg
import os

W = 800
H = 600


class Game(object):
    def __init__(self):
        self.screen = pg.display.set_mode((W,H))
        self.images = []
        self.num = 0
        for img in os.listdir('./img'):
            try:
                image = pg.image.load(os.path.join('./img', img))
                self.images.append(image)
            except:
                pass
        self.image = self.images[self.num]
        self.done = False
        self.fps = 60.0
        self.clock = pg.time.Clock()
        self.timer = 1000
        self.time = 0

    @staticmethod
    def image_fit_screen(img):
        image = img.copy()
        w, h = image.get_size()
        if w > W:
            h = h / w * W * 1.0
            w = W
            if h > H:
                w = w / h * H * 1.0
                h = H
        elif h > H:
            w = w / h * H * 1.0
            h = H
            if w > W:
                h = h / w * W * 1.0
                w = W
        img = pg.transform.scale(image, (int(w), int(h)))
        return img

    def draw(self):
        self.screen.fill((5,5,5))
        w,h = self.img.get_size()
        self.screen.blit(self.img,(W/2-w/2.0,H/2-h/2.0))

    def update(self,dt):
        self.time -= dt
        if self.time <= 0:
            self.frame = 0
            self.time = self.timer
            self.num = (self.num + 1) % len(self.images)
            self.image = self.images[self.num]
            self.show_image = self.image_fit_screen(self.image)
            self.w,self.h = self.show_image.get_size()
        self.frame += 1
        if self.frame <= 11:
            self.img = pg.transform.scale(self.show_image,(int(self.w*self.frame/10.0),int(self.h*self.frame/10.0)))
        elif self.frame > 11:
            self.img = self.image_fit_screen(self.image)

    def get_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.done = True
                if event.key == pg.K_DOWN:
                    self.timer += 200
                    if self.timer >= 2000:
                        self.timer = 2000
                if event.key == pg.K_UP:
                    self.timer -= 200
                    if self.timer <= 200:
                        self.timer = 200

    def run(self):
        pg.init()
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.get_event()
            self.update(dt)
            self.draw()
            pg.display.set_caption('switch time: {}'.format(self.timer/1000.0))
            pg.display.update()
        pg.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
        

import pygame

class Player:
    def __init__(self, x, y, w, h, speed):
        self.x = x-w/2
        self.y = y-h/2
        self.w = w
        self.h = h
        self.speed = speed
    def controls(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if(self.x < -self.w/2): self.x = -self.w/2
        if(self.x > 800-self.w/2): self.x = 800-self.w/2

class Brick:
    def __init__(self, x, y, w, h, color):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.on = True

class Ball:
    def __init__(self, x, y, w, h, vx, vy):
        self.x = x-w/2
        self.y = y-h/2
        self.w = w
        self.h = h
        self.vx = vx
        self.vy = vy
    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.y < 0: self.vy = -self.vy
        if self.x < 0: self.vx = -self.vx
        if self.x > 800-self.w: self.vx = -self.vx
    def collision(self, other):
        xcol = self.x+self.w>=other.x and self.x<=other.x+other.w
        ycol = self.y+self.h>=other.y and self.y<=other.y+other.h
        if(xcol and ycol):
            self.vy = -self.vy
            if type(other).__name__ == "Brick":
                other.on = False
            if type(other).__name__ == "Player":
                self.vx = (self.x+self.w/2-other.x-other.w/2)/10
                self.y = other.y-self.h
            return True
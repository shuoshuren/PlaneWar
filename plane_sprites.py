import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新频率
FPS = 60


class GameSpite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        # 在屏幕的垂直方向移动
        self.rect.y += self.speed


class BackGround(GameSpite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        super().__init__("./images/background.png")
        # 判断是否是交替图像,如果是,需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):

        # 1.调用父类方法实现
        super().update()
        # 2.判断是否移出屏幕,如果移出屏幕,则将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

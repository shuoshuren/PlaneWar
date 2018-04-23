import pygame

# 游戏的初始化
pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))

# 绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (150, 500))

# 可以在所有的绘制工作完成之后,统一调用update方法
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义Rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 500, 102, 126)
# 游戏循环->意味着游戏的正式开始
while True:
    clock.tick(60)
    # 2.修改飞机的位置
    hero_rect.y -= 1
    # 3.调用blit方法绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    # 4.调用update方法更新显示,在调用之前,需要把所有的游戏图像重新绘制一遍
    pygame.display.update()
    pass

pygame.quit()

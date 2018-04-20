# 1.使用pygame.image.load()加载图像的数据
# 2.使用游戏屏幕对象,调用bilt方法将图像绘制到指定位置
# 3.调用pygame.diaplay.update() 更新整个屏幕的显示


import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480,700))

# 绘制背景图像
# 1.加载图像数据
bg = pygame.image.load("./images/background.png")
# 2.blit绘制图像
screen.blit(bg,(0,0))
# 3.update 更新屏幕显示
pygame.display.update()


while True:
    pass


pygame.quit()
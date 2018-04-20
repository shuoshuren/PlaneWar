# pygame.display 用于创建和管理游戏窗口
# pygame.display.set_mode(resolution=(180,700),flags=0,depth=0) 初始化游戏显示窗口
# resolution:指定屏幕的宽和高,默认创建的窗口大小和屏幕的大小一致
# flags:参数指定屏幕的附加选项,例如是否全屏等,默认不传递
# depth:表示颜色的位数
# pygame.display.update() 刷新屏幕内容显示

import pygame

pygame.init()

# 创建游戏的窗口
screen = pygame.display.set_mode((480,700))
while True:
    pass


pygame.quit()
#  pip install -i https://pypi.tuna.tsinghua.edu.cn/simple/ pynput

from pynput import mouse
# 创建一个鼠标
m_mouse = mouse.Controller()
# 输出鼠标位置
print(m_mouse.position)

import time
from pynput import mouse, keyboard
time.sleep(5)

m_mouse = mouse.Controller()    # 创建一个鼠标
m_keyboard = keyboard.Controller()  # 创建一个键盘
m_mouse.position = (850, 670)       # 将鼠标移动到指定位置
m_mouse.click(mouse.Button.left) # 点击鼠标左键
while(True):
    m_keyboard.type('你好')        # 打字
    m_keyboard.press(keyboard.Key.enter)    # 按下enter
    m_keyboard.release(keyboard.Key.enter)    # 松开enter
    time.sleep(0.5)    # 等待 0.5秒
# encoding=gbk

import ctypes, sys

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# 字体颜色定义 text colors
FOREGROUND_BLUE = 0x09  # blue.
FOREGROUND_GREEN = 0x0a  # green.
FOREGROUND_RED = 0x0c  # red.
FOREGROUND_YELLOW = 0x0e  # yellow.

# 背景颜色定义 background colors
BACKGROUND_YELLOW = 0xe0  # yellow.

# get handle
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def set_cmd_text_color(color, handle=std_out_handle):
    Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return Bool

# reset white
def resetColor():
    set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)

def printGreen(mess):
    set_cmd_text_color(FOREGROUND_GREEN)
    sys.stdout.write(mess + '\n')
    resetColor()

def printRed(mess):
    set_cmd_text_color(FOREGROUND_RED)
    sys.stdout.write(mess + '\n')
    resetColor()

def printYellow(mess):
    set_cmd_text_color(FOREGROUND_YELLOW)
    sys.stdout.write(mess + '\n')
    resetColor()

# white bkground and black text
def printYellowRed(mess):
    set_cmd_text_color(BACKGROUND_YELLOW | FOREGROUND_RED)
    sys.stdout.write(mess + '\n')
    resetColor()


if __name__ == '__main__':
    printGreen('正在进行项目：构建管理员管理工具.......！')
    printRed('\033[1;33m正在进行项目：构建管理员管理工具.......！\033[1;31;40m')
    printYellow('printYellow:Yellow Color Text')

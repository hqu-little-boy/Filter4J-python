# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

from TextFilter import TextFilter


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
import sys
# from filter import TextFilter  # 假设TextFilter在filter模块中


def main():
    print("Filter4j 演示程序 已经启动!")
    textFilter = TextFilter()
    while True:
        try:
            # 在Python中，我们使用input函数来从控制台获取输入
            str = input()
            # str = '想cao你'
            # 在Python中，我们不需要使用三元运算符，可以直接使用if-else语句
            if textFilter.is_illegal(str):
                print("异常")
            else:
                print("正常")
        except KeyboardInterrupt:
            # 当用户按下Ctrl+C时，捕获KeyboardInterrupt异常并退出循环
            print("\n程序已退出。")
            break


if __name__ == "__main__":
    main()
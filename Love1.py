import time

# delay = 0.1 速度控制
def display_message(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def confession():
    display_message("亲爱的XXX，我有一件重要的事情想告诉你...")
    time.sleep(1) # 打印的间隔
    display_message("我喜欢你！")
    time.sleep(1)
    display_message("这不仅是程序的输出，而是我的真实感情。")
    time.sleep(1)
    display_message("愿意成为我的女朋友吗？")
    time.sleep(1)
    display_message("请慎重考虑，我会等待你的答案。")
    time.sleep(1)
    display_message("谢谢！")

if __name__ == "__main__":
    confession()

    # 等待用户输入或按下回车键
    input("按下回车键关闭程序...")

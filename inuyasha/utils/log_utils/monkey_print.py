import sys
import time

print_raw = print

WORD_COLOR = 37


def stdout_write(msg: str):
    sys.stdout.write(msg)
    sys.stdout.flush()


def stderr_write(msg: str):
    sys.stderr.write(msg)
    sys.stderr.flush()


# noinspection PyProtectedMember,PyUnresolvedReferences
def enhance_print(*args, sep=' ', end='\n', file=None):
    """
    print补丁
    """
    args = (str(arg) for arg in args)  # 防止是数字不能被join
    if file == sys.stderr:
        stderr_write(sep.join(args))  # 如 threading 模块第926行，打印线程错误，希望保持原始的红色错误方式，不希望转成蓝色。
    elif file in [sys.stdout, None]:
        # 获取被调用函数在被调用时所处代码行数
        # noinspection PyUnresolvedReferences
        line = sys._getframe().f_back.f_lineno
        # 获取被调用函数所在模块文件名
        file_name = sys._getframe(1).f_code.co_filename
        stdout_write(
            f'\033[0;{WORD_COLOR};34m{time.strftime("%H:%M:%S")}  "{file_name}:{line}"   {sep.join(args)} {end} \033[0m')
    else:
        print_raw(*args, sep=sep, end=end, file=file)


def patch_print():
    """
    Python有几个namespace，分别是locals,globals,builtin
    其中定义在函数内声明的变量属于locals，而模块内定义的函数属于globals。
    :return:
    """
    try:
        __builtins__.print = enhance_print
    except AttributeError:
        # noinspection PyUnresolvedReferences
        __builtins__['print'] = enhance_print


def common_print(*args, sep=' ', end='\n', file=None):
    args = (str(arg) for arg in args)
    args = (str(arg) for arg in args)  # 防止是数字不能被join
    if file == sys.stderr:
        stderr_write(sep.join(args) + end)  # 如 threading 模块第926行，打印线程错误，希望保持原始的红色错误方式，不希望转成蓝色。
    else:
        stdout_write(sep.join(args) + end)


def reverse_patch_print():
    """
    提供一个反猴子补丁，恢复print原状
    :return:
    """
    try:
        __builtins__.print = print_raw
    except AttributeError:
        # noinspection PyUnresolvedReferences
        __builtins__['print'] = print_raw

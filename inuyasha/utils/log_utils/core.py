import os
import sys
import threading

from loguru import logger

from inuyasha.utils.common_utils.get_project_path import get_project_path


class GetLogging:
    """
    日志配置，每天0点创建新文件，7天后清空
    """
    _instance_lock = threading.Lock()

    # 使用线程锁进行单例模式的锁定，防止创建多个实例
    def __new__(cls, *args, **kwargs):
        if not hasattr(GetLogging, "_instance"):
            with GetLogging._instance_lock:
                if not hasattr(GetLogging, "_instance"):
                    GetLogging._instance = object.__new__(cls)
        return GetLogging._instance

    # 初始化，会在 __new__ 方法后执行
    def __init__(self):
        self.BASE_DIR = get_project_path('inuyasha')
        self.error_log_file_path = os.path.join(self.BASE_DIR, 'outputs/logs/error_{time:YYYY-MM-DD}.log')
        self.debug_log_file_path = os.path.join(self.BASE_DIR, 'outputs/logs/debug_{time:YYYY-MM-DD}.log')
        self.info_log_file_path = os.path.join(self.BASE_DIR, 'outputs/logs/info_{time:YYYY-MM-DD}.log')
        self.all_log_file_path = os.path.join(self.BASE_DIR, 'outputs/logs/all_{time:YYYY-MM-DD}.log')
        # 移除默认控制台输出
        logger.remove()

        # 添加控制台输出的格式,sys.stdout为输出到屏幕
        logger.add(sys.stdout,
                   colorize=True,
                   format="<level>{time:YYYY-MM-DD HH:mm:ss}</level> - "  # 颜色>时间
                          "<level>{process.name} | </level>"  # 进程名
                          "<level>{thread.name} | </level>"  # 线程名
                          "<level>\"{file.path}:{line}\" - </level>"  # 文件名
                          "<level>{module}.{function}</level>"  # 模块名.方法名
                          ":<level>{line} | </level>"  # 行号
                          "<level>{level}: </level>"  # 等级
                          "<level>{message}</level>",  # 日志内容
                   )
        # 错误日志
        logger.add(
            self.error_log_file_path,
            format="{time:YYYY-MM-DD HH:mm:ss} - "  # 时间
                   "{process.name} | "  # 进程名
                   "{thread.name} | "  # 线程名
                   "\"{file.path}:{line}\" - "  # 文件名
                   "{module}.{function}:{line} - {level} -{message}",
            filter=lambda x: True if x["level"].name == "ERROR" else False,
            rotation="00:00", retention=7, level='ERROR', encoding='utf-8',
            enqueue=True
        )
        # DEBUG日志
        logger.add(
            self.debug_log_file_path,
            format="{time:YYYY-MM-DD HH:mm:ss} - "  # 时间
                   "{process.name} | "  # 进程名
                   "{thread.name} | "  # 线程名
                   "\"{file.path}:{line}\" - "  # 文件名
                   "{module}.{function}:{line} - {level} -{message}",
            filter=lambda x: True if x["level"].name == "DEBUG" else False,
            rotation="00:00", retention=7, level='DEBUG', encoding='utf-8',
            enqueue=True
        )
        # INFO日志
        logger.add(
            self.info_log_file_path,
            format="{time:YYYY-MM-DD HH:mm:ss} - "  # 时间
                   "{process.name} | "  # 进程名
                   "{thread.name} | "  # 线程名
                   "\"{file.path}:{line}\" - "  # 文件名
                   "{module}.{function}:{line} - {level} -{message}",
            filter=lambda x: True if x["level"].name == "INFO" else False,
            rotation="00:00", retention=7, level='INFO', encoding='utf-8',
            enqueue=True
        )
        # all日志
        logger.add(
            self.all_log_file_path,
            format="{time:YYYY-MM-DD HH:mm:ss} - "  # 时间
                   "{process.name} | "  # 进程名
                   "{thread.name} | "  # 线程名
                   "\"{file.path}:{line}\" - "  # 文件名
                   "{module}.{function}:{line} - {level} -{message}",
            rotation="00:00", retention=7, encoding='utf-8',
            enqueue=True
        )
        self.logger = logger

    def get_log(self):
        return self.logger


log = GetLogging().get_log()  # 获取日志实例

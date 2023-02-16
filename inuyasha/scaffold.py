import os
import sys


def create_folder(folder_name):
    if os.path.isdir(folder_name):
        print(f"{folder_name}文件夹已存在 ⚠️, 请重新创建一个新的项目名称")
    os.makedirs(folder_name)
    print(f"创建文件夹 📁: {folder_name} 成功 ✅")


def create_file(path, file_content=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(file_content)
    print(f"创建文件 📃: {path} 成功 ✅")


def create_scaffold():
    """ 创建项目脚手架"""
    # 创建项目名称
    project_name = input("请输入项目名称 🏭: 默认为test_project")
    project_name = project_name if project_name else "test_project"
    if os.path.isdir(project_name):
        print(f"{project_name}项目名称已存在 ⚠️, 请重新创建一个新的项目名称")
        return 1
    create_folder(project_name)
    print(f"您的项目创建成功 ✅，项目名称为: {project_name}")
    print(f"项目根目录为 🗂️: {os.path.join(os.getcwd(), project_name)}\n")
    # 创建项目类型
    test_type = input("请选择测试类型(api/ui/app) 🏭: 默认为api")
    test_type = test_type if test_type else "api"
    if test_type not in ['api', 'ui', 'app']:
        print(f"测试类型 {test_type} 不存在 ⚠️, 请重新选择测试类型")
        return 1
    create_folder(os.path.join(project_name, f'{test_type}_test'))
    # 创建应用名称
    application_name = input("请输入应用名称 🏭: 默认为test_application")
    application_name = application_name if application_name else "test_application"
    create_folder(os.path.join(project_name, f'{test_type}_test', application_name))
    create_file(os.path.join(project_name, f'{test_type}_test', '__init__.py'))  # 创建__init__.py文件

    # 创建项目结构
    project_path = os.path.join(project_name, f'{test_type}_test', application_name)
    application_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_project', f'{test_type}_test', 'test_application')

    for root, dirs, files in os.walk(application_path):
        relative_path = root.replace(application_path, "").lstrip("\\").lstrip("/")
        if dirs:
            for dir_ in dirs:
                create_folder(os.path.join(project_path, relative_path, dir_))
        if files:
            for file in files:
                with open(os.path.join(root, file), encoding="utf-8") as f:
                    create_file(os.path.join(project_path, relative_path, file), f.read())


def main_scaffold():
    # 项目脚手架处理程序入口
    sys.exit(create_scaffold())


if __name__ == '__main__':
    main_scaffold()
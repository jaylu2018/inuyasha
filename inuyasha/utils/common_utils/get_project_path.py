import os


def get_project_path(project_name=None):
    """
    获取当前项目根路径
    :param project_name:
    :return: 根路径
    """
    PROJECT_NAME = project_name if project_name else 'LianLianAuto'
    project_path = os.path.abspath(os.path.dirname(__file__))
    if "/" in project_path:
        path = os.sep.join(project_path.split("/"))
    if "\\" in project_path:
        path = os.sep.join(project_path.split("\\"))
    root_path = path[:path.find(f"{PROJECT_NAME}")] + f"{PROJECT_NAME}"
    # print(f'当前项目名称：{PROJECT_NAME}\r当前项目根路径：{root_path}')
    return root_path


if __name__ == '__main__':
    print(get_project_path('inuyasha'))

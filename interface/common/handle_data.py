import re
from common.handle_config import conf


class EnvData:
    pass


def replace_data(classname, confname, data):
    """
    把数据中的 #.*# 替换成配置文件中的数据或类属性中的数据
    :param classname: 存储数据的类名
    :param confname: 存储数据的配置文件模块名
    :param data: 需要替换的数据
    :type data: str
    :return: 替换后的数据
    """

    while re.search("#(.*?)#", data):
        res = re.search("#(.*?)#", data)
        key = res.group()
        key2 = res.group(1)
        try:
            value = conf.get(confname, key2)
        except:
            value = getattr(classname, key2)
        finally:
            data = data.replace(key, value)
    return data

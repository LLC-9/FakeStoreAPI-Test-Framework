import configparser   #导入专门读取ini的工具
import os    #导入os工具，才能去弄路径

def get_config():
    #实例化读取ini文件工具的机器人，命名为：config
    config = configparser.ConfigParser()
    #找根路径
    config_path1 = os.path.dirname(os.path.dirname(__file__))
    #拼接ini文件的绝对路径，方便后面读取
    config_path2 = os.path.join(config_path1, "config.ini")
    #调用config机器人读取ini文件，用uft-8防止文件中有中文乱码
    config.read(config_path2,encoding="utf-8")
    #分开取值，先取ini文件中开关的值（test,prod,dev三选一，由自己在config.ini配置中决定）
    config_current = config.get("env","current")
    #再取环境中的实际url
    base_url = config.get(config_current,"base_url")
    #返回取到的url
    return base_url
#本地测试，看看取对没有
if __name__ == "__main__":
    print(f"当前环境url为：{get_config()}")
'''
一个批量的自动化处理工具

使用click、ParallelSSHClient、Pyinstaller第三方库

账号和密码通过命令行传入

主机地址通过同级目录下host.txt获取
'''

import click
from pssh.clients import ParallelSSHClient

# 主机信息
HOSTS = []

# 从文件中获取获取IP
def getHostInfo():
    global HOSTS
    
    with open('host.txt') as fileInput:
        for host in fileInput:
            HOSTS.append(host.strip())

# 总处理逻辑
@click.command()
@click.option('--account', default='root', help='host account')
@click.option('--password', help='host password')
@click.option('--command', help='exec command')
def dealProcess(account, password, command):
    # 获取服务器客户端
    client = ParallelSSHClient(HOSTS, user=account, password=password)

    # 执行命令
    output = client.run_command(command)

    for host_out in output.values():
        # 打印命令的执行状态
        print('return code: ', host_out.exit_code)

        # 打印正常输出流
        print('正常输出流:')
        for stdout in host_out.stdout:
            print(stdout)

        # 打印异常输出流
        print('异常输出流:')
        for stderr in host_out.stderr:
            print(stderr)

        print('------------------------------------------')

if __name__ == '__main__':
    getHostInfo()
    dealProcess()
    


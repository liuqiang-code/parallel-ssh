'''
官方中文使用教程 https://parallel-ssh.readthedocs.io/en/latest/quickstart.html

本demo是一个简单的学习使用脚本
'''

from pssh.clients import ParallelSSHClient

# 服务器基本信息 主机地址、用户名、密码
HOSTS = ['192.168.1.183', '192.168.1.183', '192.168.1.183']
USERNAME = 'root'
PASSWD = 'lz673253'

# command
cmd = 'pwd'

# 获取服务器客户端
client = ParallelSSHClient(HOSTS, user=USERNAME, password=PASSWD) 

output = client.run_command(cmd)

for host_out in output.values():
    # 打印命令的执行状态
    print('running code: ', host_out.exit_code)
    for line in host_out.stdout:
        # 输出命令的执行结果
        print(line)
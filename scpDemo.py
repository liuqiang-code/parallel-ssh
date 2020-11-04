'''
并行将文件复制到远程主机

从远程主机并行复制文件

https://parallel-ssh.readthedocs.io/en/latest/advanced.html#sftp-and-scp
'''

from pssh.clients import ParallelSSHClient
from gevent import joinall

# 服务器基本信息 主机地址、用户名、密码
HOSTS = ['192.168.1.215']
USERNAME = 'root'
PASSWD = 'lz673253'

# 获取客户端
client = ParallelSSHClient(HOSTS, user=USERNAME, password=PASSWD)

# 上传文件
#greenlets = client.copy_file('readme.md', '/root/readme.md')
#joinall(greenlets, raise_error=True)

# 下载文件
greenlets = client.copy_remote_file('/root/readme.md', 'abc.md')
joinall(greenlets, raise_error=True)

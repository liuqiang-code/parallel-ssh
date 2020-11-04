#### parallel-ssh 学习使用demo

##### 简介
异步并行SSH客户端库。

在许多服务器上以异步方式运行SSH命令，而在客户端主机上的系统负载却最小，这可以使成百上千的服务器运行。

##### 安装
````
pip3 install parallel-ssh
````

##### pyinstaller 打包命令
````
pyinstaller autoTool.py -F --hidden-import=ssh2.agent --hidden-import=ssh2.pkey --hidden-import=ssh2.utils --hidden-import=ssh2.channel --hidden-import=ssh2.sftp_handle --hidden-import=ssh2.listener --hidden-import=ssh2.statinfo --hidden-import=ssh2.knownhost --hidden-import=ssh2.sftp --hidden-import=ssh2.sftp_handle --hidden-import=ssh2.session --hidden-import=ssh2.publickey --hidden-import=ssh2.fileinfo --hidden-import=ssh2.exceptions --hidden-import=ssh2.error_codes --hidden-import=ssh2.c_stat --hidden-import=ssh2.ssh2 --hidden-import=ssh2.c_sftp --hidden-import=ssh2.c_pkey --hidden-import=ssh2.agent --hidden-import=pkg_resources.py2_warn
````

[官方中文使用教程](https://parallel-ssh.readthedocs.io/en/latest/quickstart.html)
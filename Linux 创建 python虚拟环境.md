# Linux 创建 python虚拟环境

## 1.安装 virtualenv 和 virtualenvwrapper

`pip3 install virtualenv`

`pip3 install virtualenvwrapper`

## 2.创建一个存储虚拟环境的目录

`mkdir $HOME/.virtualenvs`

## 3.使用vim编辑器打开 ~/.bashrc 文件(命令:vim ~/.bashrc),向里添加以下内容(添加运行环境):

`export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh`

## 4.更新配置文件

`source ~/.bashrc`

## 5.创建虚拟环境

默认python版本创建：`mkvirtualenv 虚拟环境名`

指定python版本创建：`mkvirtualenv test1 -p /usr/local/bin/python3.8`

上述案例将指定虚拟环境的版本为:python3.8

## 6.退出虚拟环境

`deactivate`

## 7.启动(切换)虚拟环境

`workon 其它虚拟环境名`

## 8.删除虚拟环境

`rmvirtualenv 虚拟环境名`

## 9.查看虚拟环境使用的python版本

`python -V` 或者 `pip -V`

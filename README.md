# Flask
sth. about Flask


# Install Python3.6 on CentOS7
### 1. Pre-Build Configuration
Extract the downloaded Python3 source code and:
```JavaScript
$ cd Python-3.6.x/
$ ./configure --prefix=/usr/local/python3.6 --enable-optimizations

```
1. The **–prefix** option is used to set the local installation directory path. If this option is not configured, the executable files will be placed in /usr/local/bin by default after installation. The library files are placed by default in /usr/local/lib, The configuration file is placed by default in /usr/local/etc, other resource files are placed in /usr/local/share.
2. If configured –prefix, for example --prefix=/usr/local/python3.7, then all resource files can be placed in path /usr/local/python3.7 for easy administration.
3. **–enable-optimizations** is an optimization option (LTO, PGO, etc.). If add this flag for compilation, the compile performance will has about 10% optimization, but this will significantly increase the compile time.
4. When the **./configure** command is finished, it will create a file Makefile for the make command to use. After make install command execute, it will install the program into the folder you specified.

### 2. Perform Compile And Install
```JavaScript
$ sudo make
$ sudo make install

```

### 3. Add Soft Links
After above steps, you might not be able to run Python3 directly because your /usr/local/ path might not be in the system PATH environment variable value, but we can solve this by adding a soft link run below commands.
```JavaScript
$ ln -s /usr/local/python3.6/bin/python3.6 /usr/bin/python3
$ ln -s /usr/local/python3.6/bin/python3.6 /usr/bin/python3.6
$ ln -s /usr/local/python3.6/bin/pip3.6 /usr/bin/pip3

```

### 4. If faield, install the pre-requirements and retry
```JavaScript
$ yum -y install openssl-devel zlib-devel bzip2-devel sqlite-devel readline-devel libffi-devel systemtap-sdt-devel

```

# VSCode and Pipenv
Pipenv虚拟环境本质上其实就是一个安装了Python解释器以及Python Packages的目录，所谓的激活虚拟环境，本质上也就是将虚拟环境目录中的Python解释器作为当前shell的Python解释器。弄清楚了这一点后，就不难知道如何使用VSCode来调试Pipenv虚拟环境的Python项目了：就算要让VSCode将虚拟环境目录中的Python解释器作为当前shell的Python解释器。

Ctrl+Shift+P打开VSCode配置面板，找到python:Select Interpreter，可以看到当前可设置的Python解释器。VSCode Python extension 不仅能自动检测到安装在标准目录中的Python解释器，还能检测到虚拟环境下的Python解释器。

可是初始时，我们在python:Select Interpreter提供的选项列表中并不能看到项目虚拟环境的Python解释器。原因是VSCode（确切地说应该是Python extension）并不知道我们的虚拟环境目录在哪儿。因此我们需要做的就是给VSCode设置一下Python虚拟环境目录：
```javascript
// settings.json
{
    ...
    ...
    "python.venvPath": "/home/XXXX/.local/share/virtualenvs"
}
```

重启VSCode之后，就能python:Select Interpreter提供的解释器列表中看到我们虚拟环境下的Python解释器。选择项目对应的虚拟环境Python解释器后，就能开始调试任务了。


# Pip install 速度慢的处理办法
可以用以下方式指定其他安装包源：
```javascript

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pipenv

```
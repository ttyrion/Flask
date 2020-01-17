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

```

### 4. If faield, install the pre-requirements and retry
```JavaScript
$ yum -y install openssl-devel zlib-devel bzip2-devel sqlite-devel readline-devel libffi-devel systemtap-sdt-devel

```
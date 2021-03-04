## 安装
1. 安装Python3.6、pipenv
```shell
pip install -i https://mirrors.aliyun.com/pypi/simple pipenv
```
2. 初始化
```shell
pipenv run pipenv install
```
3. 添加依赖
```shell
pipenv shell
pipenv install pandas
pipenv install --verbose pandas
```
4. 启动
```shell
pipenv run python main.py
```
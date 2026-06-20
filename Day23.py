# -*- coding: utf-8 -*-
# 1. 导入 os 模块
import os

# 2. 获取当前工作目录
current_dir = os.getcwd()
print("当前工作目录: ", current_dir)

# 3.列出当前目录下的所有内容
print("当前目录下的内容: ", os.listdir(current_dir))

# 4. 创建一个新目录 （如果不存在）
new_dir = "test_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print(f"目录 {new_dir} 创建成功! ")
else:
    print(f"目录 {new_dir} 已经存在! ")

# 5. 在新目录中创建一个文本文件
file_path = os.path.join(new_dir, "hello.txt")
with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hello, Python! 学习ing ")
print(f"文件 {file_path} 创建成功! ")

# 6. 读取文件内容
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()
    print("文件内容: ", content)

# 7. 删除文件
os.remove(file_path)
print(f"文件: {file_path} 已删除! ")

# 8. 删除空目录
os.rmdir(new_dir)
print(f"目录:{new_dir} 已删除! ")

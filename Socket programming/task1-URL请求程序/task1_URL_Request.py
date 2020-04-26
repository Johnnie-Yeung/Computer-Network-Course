import requests
import codecs
import os
url = input('Please input a URL:')
r = requests.get(url)   # 请求网页
file_path = 'E:\software\PYTHON_work\html_file.html'  # 输入保存文件的目录
with codecs.open('html_file.html', 'w', r.encoding) as file_object:
    file_object.write(r.text)    # 把请求的网页内容写入html文件中
size = os.path.getsize(file_path)  # 计算文件大小
print('The requested url: ' + url)    # 打印请求的url
print('The saved file: html_file.html')  # 打印文件名称
print('The requested file size: ', size, 'bytes')   # 打印文件大小

import re


# 打开文件并读取内容
def open_file_read(path):
    text = ''
    file = open(path, 'r', encoding='UTF-8')
    each_line = file.readline()
    while each_line:
        text += each_line
        each_line = file.readline()
    # 使用re模块的sub()实现正则匹配，替换标点符号为空
    # \W匹配除了字母,数字，下划线之外的字符
    final_text = re.sub('\W+', '', text).replace("_", '')
    file.close()
    return final_text

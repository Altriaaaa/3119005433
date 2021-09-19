import re
import gensim
import jieba
import os

# 打开文件并读取内容
import jieba


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

def cut(final_text):
    res = jieba.lcut(final_text)
    return res

# def caculate_similarity(final_first_text, final_second_text):


def main_test():
    first_path = input("输入原文文件的绝对路径")
    second_path = input("输入抄袭版论文的绝对路径")

    if not os.path.exists(path1):
        print("原文文件找不到")
        exit()
    if not os.path.exists(path2):
        print("抄袭版论文找不到")
        exit()

    first_text = open_file_read(first_path)
    second_text = open_file_read(second_path)

    final_first_text = cut(first_text)
    final_second_text = cut(second_text)

    similarity = caculate_similarity(final_first_text,final_second_text)

    print("两篇文章相似度为%.2f"%similarity)
    save_file = open(save_path, 'w', encoding="utf-8")
    save_file.write("这两篇文章的相似度： %.2f"%similarity)
    save_file.close()

if __name__ == '__main__':
    main_test()
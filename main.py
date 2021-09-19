import re
import gensim
import jieba
import sys


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


def cut(final_text):
    res = jieba.lcut(final_text)
    return res


def caculate_similarity(cut_first_text, cut_second_text):
    texts = [cut_first_text, cut_second_text]
    # 创建语料库
    repository = gensim.corpora.Dictionary(texts)
    # doc2bow
    corpus = [repository.doc2bow(text) for text in texts]
    # num_features代表生成的向量的维数（根据词袋的大小来定）
    cosine_similarity = gensim.similarities.Similarity('-Similarity-index', corpus, num_features=len(repository))
    # 获取句子相似度
    testing_corpus = repository.doc2bow(cut_first_text)
    cosine_similarity = cosine_similarity[testing_corpus][1]
    return cosine_similarity


def main():
    try:
        first_path = sys.argv[1]
        second_path = sys.argv[2]
        answer = sys.argv[3]

        first_text = open_file_read(first_path)
        second_text = open_file_read(second_path)

        cut_first_text = cut(first_text)
        cut_second_text = cut(second_text)

        cosine_similarity = caculate_similarity(cut_first_text, cut_second_text)

        print("cosine_similarity is %.2f" % cosine_similarity)
        answer_file = open(answer, 'w', encoding="utf-8")
        answer_file.write("cosine_similarity is %.2f" % cosine_similarity)
        answer_file.close()
    except Exception as e:
        print(e)
        exit("请使用命令行传参，格式如python main.py [原文文件] [抄袭版论文的文件] [答案文件]")

def test_main():
    first_path='C:\\Users\\84330\\Desktop\\3119005433-main\\测试文本2\\orig.txt'
    second_path='C:\\Users\\84330\\Desktop\\3119005433-main\\测试文本2\\orig_0.8_add.txt'
    first_text = open_file_read(first_path)
    second_text = open_file_read(second_path)
    cut_first_text = cut(first_text)
    cut_second_text = cut(second_text)
    cosine_similarity = caculate_similarity(cut_first_text, cut_second_text)
    cosine_similarity = round(cosine_similarity.item(), 2)
    return cosine_similarity

if __name__ == '__main__':
    main()
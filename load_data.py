# coding: utf-8

from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os
import unicodedata
import string

all_letters = string.ascii_letters + " .,;'"   # 所有的有效字符
n_letters = len(all_letters)  # 字符数量


def find_files(path):
    return glob.glob(path)


def unicode_to_ascii(string_):
    return ''.join(c for c in unicodedata.normalize("NFD", string_) if
                   unicodedata.category(c) != "Mn" and c in all_letters)


def read_lines(file_name):
    lines = open(file_name, encoding="utf-8").read().strip().split("\n")  # read() 参数为空表示读取全部
    return [unicode_to_ascii(line) for line in lines]


def get_category(data_path):
    category_lines = {}
    all_category = []
    for file_name in find_files(data_path):
        category = os.path.splitext(os.path.basename(file_name))[0]
        all_category.append(category)
        lines = read_lines(file_name)
        category_lines[category] = lines
    return all_category, category_lines


if __name__ == '__main__':
    print(all_letters)
    print(unicode_to_ascii("Ślusàrski"))
    date_path = "./data/names/*.txt"
    categories, category_dict = get_category(date_path)
    print(categories)
    print(category_dict["Chinese"][:10])




import numpy as np
from PIL import Image
from os import path
from scipy.misc import imread
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import random
import os

if __name__ == "__main__":
    d = path.dirname(__file__)
    mask = imread(path.join(d, "template.png"))
    font = os.path.join(d, "simhei.ttf")
    text = open("人民的名义.txt").read()

    # preprocessing the text a little bit
    text = text.replace("侯亮平", u"亮平")
    text = text.replace("说", "")
    text = text.replace("啊", "")

    # adding specific stopwords
    stopwords = set(STOPWORDS)
    with open('stopwords.txt', encoding='utf-8') as f:
        words = f.readlines()
        for x in words:
            stopwords.add(x.rstrip())

    wc = WordCloud(font_path=font, background_color="black", max_words=2000, mask=mask, stopwords=stopwords, margin=10,
                   random_state=42).generate(text)
    # recolor wordcloud and show
    plt.title("Custom colors")
    plt.imshow(wc.recolor(color_func=ImageColorGenerator(mask), random_state=3))
    wc.to_file("wordcloud.png")
    plt.axis("off")
    plt.show()
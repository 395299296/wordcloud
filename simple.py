import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
import os

from wordcloud import WordCloud, STOPWORDS


font=os.path.join(os.path.dirname(__file__), "DroidSansFallbackFull.ttf")

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(80, 100)

if __name__ == "__main__":
    d = path.dirname(__file__)
    mask = np.array(Image.open(path.join(d, "template.png")))
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

    wc = WordCloud(font_path=font,max_words=1000, mask=mask, stopwords=stopwords, margin=10,
                   random_state=1).generate(text)
    # store default colored image
    default_colors = wc.to_array()
    plt.title("Custom colors")
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
    wc.to_file("a_new_hope.png")
    plt.axis("off")
    plt.figure()
    plt.title(u"人民的名义")
    plt.imshow(default_colors)
    plt.axis("off")
    plt.show()
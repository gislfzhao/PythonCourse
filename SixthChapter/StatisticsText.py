# Statistics Text
import jieba


def get_text(path, filename):
    txt = open(path + filename, "r", encoding="utf-8").read()
    return txt


def output_words_info(words, path, filename):
    output_name = path + filename.split(".")[0] + "_statistics.txt"
    txt = open(output_name, "w", encoding="utf-8")
    for word in words:
        txt.write("{:<}:{:>5}\n".format(word[0], word[1]))
    txt.close()


def stat_words(txt):
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    # lambda标注的为匿名函数，
    # key指定的是排序方式的函数，x为参数,:后面为表达式
    return items


def top_words(words, num):
    for i in range(num):
        word, count = words[i]
        print("{:<10}:{:>5}".format(word, count))


if __name__ == "__main__":
    u_path = r"C:\Users\GISzhao\Desktop\\"
    u_filename = "十九大.txt"
    text = get_text(u_path, u_filename)
    txt_words = stat_words(text)
    top_words(txt_words, 10)
    output_words_info(txt_words, u_path, u_filename)

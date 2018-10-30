# Calculate Hamlet V1


def get_text():
    txt = open("hamlet.txt", "r").read()
    txt = txt.lower()
    for ch in "^&!#$%*()@+-,./;:<>=_|\\~{}[]'?\"‘’·":
        txt = txt.replace(ch, " ")
    return txt


def output_words_info(words):
    output_name = "hamlet_words_info.txt"
    txt = open(output_name, "w")
    for word in words:
        txt.write("{:<15}:{:>5}\n".format(word[0], word[1]))
    txt.close()


def stat_words(txt):
    words = txt.split()
    counts = {}
    for word in words:
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
    text = get_text()
    txt_words = stat_words(text)
    top_words(txt_words, 10)
    output_words_info(txt_words)

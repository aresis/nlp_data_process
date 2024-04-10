import nltk
import pandas as pd

path = 'careerguidance_remove_10_20_topicwords.txt'

DF = pd.read_csv(path, header=None, encoding='utf-8')

tweets = DF[0].tolist()

words = []
for tweet in tweets:
    words.extend(nltk.word_tokenize(tweet))  # 把每个tweet分成词语，并加入words

word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(f"the len of vocab is{len(word_freq)}")

# 输出词频最高的10个词
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_words = sorted_word_freq[:10]
print("Top 10 words by frequency:")
for word, freq in top_words:
    print(f"{word}: {freq}", end=' ')
print()
# 设置词频阈值
threshold = 5  # 你可以根据需要调整这个值

# 输出词频低于阈值的词
low_freq_words = [word for word, freq in word_freq.items() if freq < threshold]
print(f"Words with frequency less than {threshold}:{len(low_freq_words)}")
for word in low_freq_words:
    print(word, end=' ')

# 按照词频大小排序
sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

file_name = path.split('.')[0]
# 输出词汇表到文件
with open(file_name + "_vocab.txt", "w", encoding='utf-8') as f:
    for item in sorted_word_freq:
        f.write(f"{item[0]}: {item[1]}\n")

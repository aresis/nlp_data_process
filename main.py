import re

import enchant
import nltk
import preprocessor as pre
import spacy
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from twitter_preprocessor import TwitterPreprocessor


def lemma(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    word_tokens = nltk.word_tokenize(text)
    text_lemma = " ".join([wordnet_lemmatizer.lemmatize(word) for word in word_tokens])
    return ' '.join(text_lemma)


def stem(text):
    stemmer = nltk.stem.snowball.SnowballStemmer('english')
    text_stemmed = [stemmer.stem(token) for token in word_tokenize(text)]
    return ' '.join(text_stemmed)


def remove_special_characters(text):
    text = re.sub('[^a-zA-Z0-9\s]', '', text)  # ^表示非
    return text


def lowercase(text):
    text_low = [token.lower() for token in word_tokenize(text)]
    return ' '.join(text_low)


def remove_one_character_words(text):
    '''Remove words from dataset that contain only 1 character'''
    text_high_use = [token for token in word_tokenize(text) if len(token) > 1]
    return ' '.join(text_high_use)


def remove_numbers(text):
    no_nums = re.sub(r'\d+', '', text)
    return ''.join(no_nums)


def remove_stopwords(text):
    stop = set(stopwords.words('english'))
    word_tokens = nltk.word_tokenize(text)
    text = " ".join([word for word in word_tokens if word not in stop])
    return text


stop = set({})
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        stop.add(line)


def remove_stopword(text):
    word_tokens = nltk.word_tokenize(text)
    text = " ".join([word for word in word_tokens if word not in stop])
    return text


dic = enchant.Dict("en_US")
nlp = spacy.load("en_core_web_lg", enable=["lemmatizer", "tagger", "attribute_ruler", "tok2vec"])
pre.set_options(pre.OPT.URL, pre.OPT.NUMBER)


def process(text):
    # if fastlid(text)[0] != "en":  #判断文本是否是纯英文文本
    #     return ''
    p = TwitterPreprocessor(text).fully_preprocess()
    sentence = remove_stopwords(remove_stopword(p.text))
    sen = nlp(pre.clean(sentence))
    line = []
    for token in sen:
        if dic.check(token.lemma_) == True and not nlp.vocab[token.lemma_].is_stop and len(
                list(token.lemma_)) > 3:  # dic.check(token.lemma_)判断单词的拼写是否正确
            line.append(token.lemma_.lower())
    # if len(line) >= 10:
    sen = ' '.join([word for word in line])
    sen = remove_stopwords(remove_stopword(sen))
    return sen
    # return ''

# text = "But other businessmen said such a short-term commercial advantage would be outweighed by further U.S.In Malaysia, trade officers and businessmen said tough curbs against Japan might allow hard-hit producers of"
# print(process(text))

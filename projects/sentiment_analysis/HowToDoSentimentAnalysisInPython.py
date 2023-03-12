# how to do sentiment analysis in python

import os
import nltk
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk.stem import WordNetLemmatizer



if __name__ == '__main__':
    nltk.download('sentiwordnet', './nltk_data')
    nltk.download('wordnet', './nltk_data')
    nltk.data.path.append('./nltk_data')

    lemmatizer = WordNetLemmatizer()

    words = []
    with open('./test_words.txt', 'r') as stream:
        words = stream.read().split('\n')

    positive_words = []
    negitive_words = []
    neutral_words = []
    for word in words:
        print(f'{word}: ')

        lem = lemmatizer.lemmatize(word)
        print(f'    {lem = }')
        synsets = list(wn.synsets(lem, lang='eng'))
        # print(f'    {synsets = }')
        synset = synsets[0]
        print(f'    {synset.name() = }')
        print(f'    {synset.pos() = }')
        # Analyzed our word
        swn_synset = swn.senti_synset(synset.name(), synset.pos())
        print(f'    {vars(swn_synset) }')
        score = swn_synset.pos_score() - swn_synset.neg_score()
        print(f'    Sentiment = {score}')

        if score > 0:
            positive_words.append(word)
        elif score < 0:
            negitive_words.append(word)
        else:
            neutral_words.append(word)

    print('-' *80)
    print(f"Positive Words: {positive_words}")
    print(f"Bad Words: {negitive_words}")
    print(f"Neutral Words: {neutral_words}")

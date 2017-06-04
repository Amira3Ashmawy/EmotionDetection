# import nltk
# import random
# from nltk.corpus import movie_reviews
#
# documents =[(list (movie_reviews.words(fileid)),category)
#             for category in movie_reviews.categories()
#             for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)
# all_words = []
# for w in movie_reviews.words():
#     all_words.append(w.lower)
# all_words=nltk.FreqDist(all_words)
# print(all_words.most_common(15))
import csv
from keras.models import Sequential
from keras.layers import Dense
from keras.utils.np_utils import to_categorical
from keras.layers import Dropout
import numpy
import h5py
from keras.models import model_from_json

class tstsent():
    def __init__(self):
        dataset = numpy.loadtxt("o.csv", delimiter=",")
        print "here"
        xtest = dataset[:12,0:21]
        ytest = dataset[:12,21:24]

        json_file = open("model.json", 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        loaded_model.load_weights("model.h5")
        print("Loaded model from disk")

        loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        scores = loaded_model.evaluate(xtest, ytest)
        print("\n%s: %.2f%%" % (loaded_model.metrics_names[1], scores[1]*100))
        predictions = loaded_model.predict(xtest)
        print(predictions)
        rounded= numpy.around(predictions, decimals=0)
        print "rounded"
        print(rounded)
        self.write(rounded)



    def write(self,rounded):
        f = open('res.txt','w')
        for round in rounded:
            #for i in range(len(round)):
            if round[0]==1:
                f.write("angry\n")
            elif round[1]==1:
                f.write("disgust\n")
            elif round[2]==1:
                f.write("joy\n")
        f.close()








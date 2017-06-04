import csv
from tstsentenses import tstsent
class Extraction():
    def __init__(self,allSentences):

        ls = self.read()
        EmoVec = []
        Words = []
        for word in ls:
            w = word.split(" ")
            Words.append(w[0])
            temp = []
            for j in range(1, len(w)):
                temp.append(int(w[j]))
            EmoVec.append(temp)
        sentences = allSentences.split('.')

        allFeatures = []
        for sent in sentences:
            sent = sent.lower()
            words = sent.split(' ')
            count = 0
            featureVec = []
            features = []
            for k in range(0, 20):
                features.append(0)
            for word in words:
                feature = self.get(word, Words, EmoVec)
                if feature != []:
                    for i in range(0, 10):
                        features[i] = feature[i]
                    for sub in range(count + 1, len(words)):
                        if words[sub] == "?":
                            features[18] = 1
                            break
                        elif words[sub] == "!":
                            features[19] = 1
                            break
                    featureVec.append(features)
                    features = []
                    for i in range(0, 20):
                        features.append(0)
                elif word == "not" or word == "no":
                    features[10] = 1

                elif word == "was":
                    features[11] = 1
                elif word == "before":
                    features[12] = 1
                elif word == "after":
                    features[13] = 1
                elif word == "always" or word == "every":
                    features[14] = 1
                elif word == "never" or word == "ever":
                    features[15] = 1
                elif word == "then" or word == "so" or word == "because":
                    features[16] = 1
                elif word == "when":
                    features[17] = 1
                count += 1

            allFeatures.append(featureVec)
        print "Features"
        print allFeatures
        print len(allFeatures)
        res = self.setMax(allFeatures)
        print res
        row = len(res[0])
        for i in range(row):
            for k in range(len(res)):
                res[k][i] = float(res[k][i] / 20.0)
        self.write(res)
        res = tstsent()
        '''print res
        self.getEmotions(res)'''
    def getEmotions(self,res):
        print "getted res"
        print res
        return res
    def read(self):
        f = open('lexicon.txt','r')
        s = f.read().replace('\r', '')
        ls = s.split('\n')
        f.close()
        return ls

    def  get (self,word , words , EmoVec):
        for i in range(0,len(words)):
            if word == words[i]:
                return EmoVec[i]

        return []
    def setMax(self,allFeatures):
        c = 20
        addVec = []
        for i in range(0,20):
            addVec.append(0)
        for features in allFeatures:
            if len(features)<c:
                for j in range(0,c-len(features)):
                    features.append(addVec)
        new = []

        for features in allFeatures:
            for i in range(1,len(features)):
                for j in range(0,len(features[i])):
                    features[0][j]+= features[i][j]
            new.append(features[0])
        return new

    def write(self,res):
        c = 0
        f = open('o.csv','w')
        for sent in res:
            print len(sent)
            check = True
            for word in sent:
                #for bit in word:
                if check == True:
                    f.write("%.5f" % word)
                    check = False
                else:
                    f.write(",")
                    f.write("%.5f" % word)
            if c < 4:
                f.write(",")
                f.write("0")
                f.write(",")
                f.write('1')
                f.write(",")
                f.write('0')
                f.write(",")
                f.write('0')
                c+=1
            elif c < 8:
                f.write(",")
                f.write("0")
                f.write(",")
                f.write('0')
                f.write(",")
                f.write('1')
                f.write(",")
                f.write('0')
                c+=1
            else:
                f.write(",")
                f.write("1")
                f.write(",")
                f.write('0')
                f.write(",")
                f.write('0')
                f.write(",")
                f.write('1')
                c+=1
            f.write("\n")
        f.close()

















import sys
import json


def loadSentFile(fp):
    sentMap = {}
    while 1:
        line = fp.readline()
        if not line:
            break;
        loadSent(sentMap, line)
    return sentMap

def loadSent(sentMap,line):
    sent = line.split('\t')
    sentMap[sent[0]] = float(sent[1])

def processTweets(fp, sentMap):
    while 1:
        line = fp.readline()
        if not line:
            break;
        tweet = readTweet(line)
        if tweet:
            computeSentiment(tweet, sentMap)
     

def computeSentiment(tweet, sentMap ):       
    sentIndex = 0.0
    text = tweet['text']
    tokens = text.split(' ')
    for t in tokens:
        if t in sentMap:
            sentIndex += sentMap[t]
    print sentIndex



def readTweet(line):        
    tweet = json.loads(line)
    if 'lang' in tweet and tweet['lang'] == 'en' and'created_at' in tweet:
        return tweet  
            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentMap = loadSentFile(sent_file)
    processTweets(tweet_file,sentMap)

if __name__ == '__main__':
    main()

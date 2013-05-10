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

def processTweets(fp, sentMap, termMap):
    while 1:
        line = fp.readline()
        if not line:
            break;
        tweet = readTweet(line)
        if tweet:
            computeSentiment(tweet, sentMap, termMap)
            
def computeSentiment(tweet, sentMap, termMap ):       
    sentIndex = 0.0
    text = tweet['text']
    tokens = text.split()
    for t in tokens:
        if t in sentMap:
            sentIndex += sentMap[t]    
    for t in tokens:
        if t not in sentMap:
            if t not in termMap:
                termMap[t] = {'P':0.0, 'N': 0.0 }
            if sentIndex > 0:
                termMap[t]['P'] += (1.0/len(tokens))
            elif sentIndex < 0: 
                termMap[t]['N'] += (1.0/len(tokens))
  

def printTermSentiment(termMap):
    for i in termMap: 
        try:
            token = i.encode('utf-8') 
            p = termMap[i]['P']
            n = termMap[i]['N']
            if n <1:
                n = 1         
            print token, ' ', p/n 
        except UnicodeEncodeError:
            pass


def readTweet(line):        
    tweet = json.loads(line)
    if 'lang' in tweet and tweet['lang'] == 'en' and'created_at' in tweet:
        return tweet  
        

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentMap = loadSentFile(sent_file)
    termMap = {}
    processTweets(tweet_file,sentMap, termMap)
    printTermSentiment(termMap)        


if __name__ == '__main__':
    main()

import sys
import json

ALL_TOKENS = ' '

def processTweets(fp):
    freqMap = { ALL_TOKENS :0.0 }
    while 1:
        line = fp.readline()
        if not line:
            break;
        tweet = readTweet(line)
        if tweet:
            countTokens(tweet, freqMap)
    return freqMap
     

def countTokens(tweet, freqMap ):       
    text = tweet['text']
    tokens = text.split()    
    for t in tokens:
        if len(t) > 0:
            freqMap[ALL_TOKENS] +=1.0
            if t in freqMap:
                freqMap[t] += 1.0
            else:
                freqMap[t] = 1.0
         

def readTweet(line):        
    tweet = json.loads(line)
    if 'created_at' in tweet:
        return tweet  
            

def computeFrequency(freqMap):
    allTokens = freqMap.pop(ALL_TOKENS)
    for i in freqMap.keys():
        try:
            token = i.encode('utf-8')
            print token, ' ', freqMap[i]/allTokens
        except UnicodeEncodeError:
            pass


def main():
    tweet_file = open(sys.argv[1])
    frequencyMap = processTweets(tweet_file)
    computeFrequency(frequencyMap)


if __name__ == '__main__':
    main()

import sys
import json

def processTweets(fp):
    tagsMap = {  }
    while 1:
        line = fp.readline()
        if not line:
            break;
        tweet = readTweet(line)
        if tweet:
            countTags(tweet, tagsMap)
    return tagsMap
     

def countTags(tweet, tagsMap ):       
    tags = tweet['entities']['hashtags']
    for t in tags:
        tag = t['text']
        if tag in tagsMap:
            tagsMap[tag] += 1.0
        else:
            tagsMap[tag] = 1.0
     

def readTweet(line):        
    tweet = json.loads(line)
    if 'created_at' in tweet and tweet['entities'] and tweet['entities']['hashtags']:
        return tweet  
            

def selectTopTenTags(tMap):
    cnt = 0
    for i in sorted(tMap, key=tMap.get, reverse=True):
        try:
            token = i.encode('utf-8')            
            print token, ' ', tMap[i]
            cnt += 1
            if cnt > 9:
                break
        except UnicodeEncodeError:
            pass


def main():
    tweet_file = open(sys.argv[1])
    tagsMap = processTweets(tweet_file)
    #print frequencyMap    
    selectTopTenTags(tagsMap)


if __name__ == '__main__':
    main()

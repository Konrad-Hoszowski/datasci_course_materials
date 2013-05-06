import sys
import json


US_STATES = {
'AL': 'Alabama',
'AK': 'Alaska',
'AS': 'American Samoa',
'AZ': 'Arizona',
'AR': 'Arkansas',
'CA': 'California',
'CO': 'Colorado',
'CT': 'Connecticut',
'DE': 'Delaware',
'DC': 'District Of Columbia',
'FM': 'Federated States Of Micronesia',
'FL': 'Florida',
'GA': 'Georgia',
'GU': 'Guam',
'HI': 'Hawaii',
'ID': 'Idaho',
'IL': 'Illinois',
'IN': 'Indiana',
'IA': 'Iowa',
'KS': 'Kansas',
'KY': 'Kentucky',
'LA': 'Louisiana',
'ME': 'Maine',
'MH': 'Marshall Islands',
'MD': 'Maryland',
'MA': 'Massachusetts',
'MI': 'Michigan',
'MN': 'Minnesota',
'MS': 'Mississippi',
'MO': 'Missouri',
'MT': 'Montana',
'NE': 'Nebraska',
'NV': 'Nevada',
'NH': 'New Hampshire',
'NJ': 'New Jersey',
'NM': 'New Mexico',
'NY': 'New York',
'NC': 'North Carolina',
'ND': 'North Dakota',
'MP': 'Northern Mariana Islands',
'OH': 'Ohio',
'OK': 'Oklahoma',
'OR': 'Oregon',
'PW': 'Palau',
'PA': 'Pennsylvania',
'PR': 'Puerto Rico',
'RI': 'Rhode Island',
'SC': 'South Carolina',
'SD': 'South Dakota',
'TN': 'Tennessee',
'TX': 'Texas',
'UT': 'Utah',
'VT': 'Vermont',
'VI': 'Virgin Islands',
'VA': 'Virginia',
'WA': 'Washington',
'WV': 'West Virginia',
'WI': 'Wisconsin',
'WY': 'Wyoming'
}

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
    happy_states = initHappyStates()
    while 1:
        line = fp.readline()
        if not line:
            break;
        tweet = readTweet(line)
        if tweet:
            sentIndex = computeSentiment(tweet, sentMap)        
            state = extractState(tweet)
            if state:
                happy_states[state] += sentIndex 
    print selectHappiesState(happy_states)


def selectHappiesState(happy_states):
    happiest_state_name = 'CA'
    for i in happy_states.keys():
        if happy_states[i] > happy_states[happiest_state_name]:
            happiest_state_name = i
    return happiest_state_name
             
def initHappyStates():
    happy_states = {}
    for i in US_STATES.keys():
        happy_states[i] = 0.0
    return happy_states


def extractState(tweet):       
    address = tweet['place']['full_name']
    tokens = address.split(',')
    us_state = tokens[len(tokens)-1].upper().strip()
    if us_state in US_STATES:
        return us_state     


def computeSentiment(tweet, sentMap ):       
    sentIndex = 0.0
    text = tweet['text']
    tokens = text.split(' ')
    for t in tokens:
        if t in sentMap:
            sentIndex += sentMap[t]
    return sentIndex


def readTweet(line):        
    tweet = json.loads(line)
    if 'created_at' in tweet and tweet['place'] and tweet['place']['country_code'] == 'US':
        return tweet  
            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sentMap = loadSentFile(sent_file)
    processTweets(tweet_file,sentMap)

if __name__ == '__main__':
    main()

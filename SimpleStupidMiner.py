
# coding: utf-8

# In[17]:


import hashlib
import requests
import sys
import time
from threading import Timer

#Node url is passed as command line parameter
if len(sys.argv) < 2:
    print("\033[91mWarning !!! No URL for the node is supplied. Using dummy URL!\033[0m")
    nodeURL = "http://IamAdummyURL.com"
else:
    nodeURL = sys.argv[1]     
    
getTask = "/mineBlock"
givePoW = "/mining/submit-block/"
global timestamp 
timestamp = time.time()
nonce = 0

def checkForUpdates():   
    #Go to the Node each 3 seconds and check for new hash/difficulty
    t = Timer(3,checkForUpdates)
    t.start()
    
    global blockHash
    global difficulty
    
    #Get the previous hash and the difficulty form the Node
    try:    
        response = requests.get(nodeURL+getTask)
        node_data = response.json()
    except:
        print("\033[91mWarning! Failed to obtain data from the Node for blockHash and difficutly! Using old values!\033[0m")
        #Start with dummy data
        node_data = {
            'blockDataHash': 'Default hash before data fetch',
            'difficulty' : 5,
        }
        
    blockHash = node_data["blockDataHash"]
    difficulty = node_data["difficulty"]
    
    print(f'Running for block hash:\033[92m {blockHash}\033[0m on difficulty\033[91m {difficulty}\033[0m on stamp \033[92m{timestamp}\033[0m at cumulative iteration \033[4m{nonce}\033[0m')
    return

def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def solutionFound(nonce,result, timestamp):
    #Push the solution to the Node
    print(f'\033[94mSolution found for\033[1m nonce = {nonce} hash = {result}\033[91m ')
    data = {'nounce':nonce,'dateCreated':timestamp  , "blockHash":result}
    try:    
        requests.post(nodeURL+givePoW, data=data)
    except:
        print("\033[91mWarning! Failed to connect to Node in order to submit found block! \033[0m")
    return

checkForUpdates()


for nonce in range(2**1000):
    timestamp = time.time()
    result = hash_256(blockHash+str(timestamp)+str(nonce))
    if result[:difficulty] == '0'*difficulty:
        solutionFound(nonce, result, timestamp)
  



# coding: utf-8

# In[7]:


import hashlib
import requests
from threading import Timer

nonce = 0
nodeURL = "3333333"
getTask = "bbbb"
givePoW = "cccc"

#Dummy data for now
node_data = {
    'blockHash': 'Default hash before data fetch',
    'difficulty' : 6,
}


def checkForUpdates():   
    #Go to the Node each 3 seconds and check for new hash/difficulty
    t = Timer(3,checkForUpdates)
    t.start()
    
    global blockHash
    global difficulty
    
    #Get the previous hash and the difficulty form the Node
    #response = requests.get(nodeURL+getTask)
    #node_data = response.json()
    blockHash = node_data["blockHash"]
    difficulty = node_data["difficulty"]
    
    print(f'Running for block hash:\033[92m {blockHash}\033[0m on difficulty\033[91m {difficulty}\033[0m at cumulative iteration \033[4m{nonce}\033[0m')
    return

def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def solutionFound(result):
    #Push the solution to the Node
    print(f'\033[94mSolution found for\033[1m nonce = {nonce} hash = {result}\033[91m ')
    
    data = {'nonce':nonce,'Proof-of-work':result}
    #requests.put(nodeURL+givePoW, data=data)
    return

checkForUpdates()


for nonce in range(2**1000):
    result = hash_256(blockHash+str(nonce))
    if result[:difficulty] == '0'*difficulty:
        solutionFound(result)
  


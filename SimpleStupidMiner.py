
# coding: utf-8

# In[43]:


import hashlib
from threading import Timer

nonce = 0
prevHash = "bbbbb"
difficulty = 5


def checkForUpdates():   
    #Go to the Node each 3 seconds and check for new hash/difficulty
    t = Timer(3,checkForUpdates)
    t.start()
    global prevHash
    global difficulty
    
    #Get the previous hash and the difficulty form the Node
    prevHash = "aaaaaa"
    #Higher number = lower difficulty
    difficulty = 71
    print(f'Running for previous hash: {prevHash} on difficulty {difficulty} at cumulative iteration {nonce}')
    return

def hash_256(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def solutionFound():
    #Push the solution to the Node
    print(f'Solution found for nonce {nonce}')
    return

checkForUpdates()


for nonce in range(2**256):
    result = hash_256(prevHash+str(nonce))
    if int(result,16) < 10**difficulty:
        solutionFound()
  


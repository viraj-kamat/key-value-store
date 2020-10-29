"""
Key value store using python
@author : virajk /viraj.kmt@gmail.com

Description :
A version keyvalue store that stores a key/value and fetches the value of the key based on a version specified or the last version present

"""
import random
import bisect

class KeyValueStore() :
    def __init__(self) :
        self.keystore = {}
        
    
    def put(self,key,value) :
        """
        @input 
        key : str
        value : int
        """
        #create key if it does not exist
        if key not in self.keystore :
            self.keystore[key] = [[],[]] #value/version
            
        version = 0
        if self.keystore[key][0] :
            version = self.keystore[key][1][-1]
        
        #Append new value to keystore
        self.keystore[key][0].append(value)
        self.keystore[key][1].append(version+1)
 
        return version+1
        
    
    
    def get(self,key,version=False) :
        """
        @Input
        key : str
        version : int (Optional)
        """
        if not version :
            if key in self.keystore and self.keystore[key][0] :
                print("Key {0} has value {1} at version {2}".format(key,self.keystore[key][0][-1],self.keystore[key][1][-1]))
                return self.keystore[key][0][-1]
            else :
                return None
        else :
            
            if key in self.keystore and self.keystore[key][0] :
                index = bisect.bisect_left(self.keystore[key][1], version)
                
                if index == 0 :
                    if self.keystore[key][1][0] > version :
                        return None
                    else :
                        print("Key {0} has value {1} at version {2}".format(key,self.keystore[key][0][-1],self.keystore[key][1][-1]))
                        return self.keystore[key][0][0]
                else :
                    
                    try :
                        if self.keystore[key][1][index] == version :
                            print("Key {0} has value {1} at version {2}".format(key,self.keystore[key][0][index],self.keystore[key][1][index]))
                            return self.keystore[key][0][index]
                            
                        print("Key {0} has value {1} at version {2}".format(key,self.keystore[key][0][index-1],self.keystore[key][1][index-1]))
                        return self.keystore[key][0][index-1]
                    except Exception as e :
                        print("Invalid version number")
                        return None
                    
            else :
                return None
                


if __name__ == "__main__" :
    pass
    
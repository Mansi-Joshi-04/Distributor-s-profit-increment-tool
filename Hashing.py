class Hash_Map:
    def __init__(self):
        self.Max=9
        self.arr=[None for i in range(self.Max)]
    def hash_key(self,key,value):
        hash=0
        for i in range(len(key)):
            for j in key[i][0]:
                hash+=ord(j)
                for k in key[i][1]:
                    hash+=ord(k)
            z=hash%9
            key_hash=z
            key_value=[key[i],value[i]]
            if self.arr[key_hash]is None:
                self.arr[key_hash]=[key_value]
            else:
                for pair in self.arr[key_hash]:
                    if pair[0]==key[i]:
                        pair[1]=value[i]
                self.arr[key_hash].append(key_value)
         
        return self.arr                    
                      
        
    def print(self):
        Ck=[]
        count=0
        for item in self.arr:
            #print(item)
            #print(len(item))
            if item is not None:
                for i in range(len(item)):
                    if len(item)>=5:
                        Ck.append(item[i][0])
        return Ck


        
                



class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data
        else:
          nextslot = self.rehash(hashvalue,len(self.slots))
          while self.slots[nextslot] != None and self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot]=key
            self.data[nextslot]=data
          else:
            self.data[nextslot] = data

    def hashfunction(self,key,size):
         return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get(self,key):
      startslot = self.hashfunction(key, len(self.slots))

      data = None
      position = startslot
      while self.slots[position] != None:
         if self.slots[position] == key:
           data = self.data[position]
           return data
         else:
           position = self.rehash(position, len(self.slots))
           if position == startslot:
               return None

    def __getitem__(self,key):
        return self.get(key)

    def __setitem__(self,key,data):
        self.put(key,data)

    def __delitem__(self,key):
        startslot = self.hashfunction(key, len(self.slots))

        position = startslot
        while self.slots[position] != None:
            if self.slots[position] == key:
                self.slots[position] = None
                self.data[position] = None
                return None
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    return None


    def __contains__(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        position = startslot
        while self.slots[position] != None:
            if self.slots[position] == key:
                return True
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    return False

    def __len__(self):
        return len([k for k in self.slots if k])


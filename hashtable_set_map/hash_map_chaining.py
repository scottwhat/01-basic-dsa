class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    def __init__(self):
        self.capacity = 2
        self.map = [[] for _ in range(self.capacity)]

    def hash(self, key):
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        index = self.hash(key)
        for pair in self.map[index]:
            if pair.key == key:
                return pair.val
        return None

    def put(self, key, val):
        index = self.hash(key)
        for pair in self.map[index]:
            if pair.key == key:
                pair.val = val
                return
        self.map[index].append(Pair(key, val))

    def remove(self, key):
        index = self.hash(key)
        for i, pair in enumerate(self.map[index]):
            if pair.key == key:
                del self.map[index][i]
                return

    def rehash(self):
        oldMap = self.map
        self.capacity *= 2
        self.map = [[] for _ in range(self.capacity)]
        for bucket in oldMap:
            for pair in bucket:
                self.put(pair.key, pair.val)

    def print(self):
        for bucket in self.map:
            for pair in bucket:
                print(pair.key, pair.val)


# Example usage
my_hash_map = HashMap()
my_hash_map.put('butts', 500)
my_hash_map.put('butts', 32)
my_hash_map.put('tits', 6)
my_hash_map.print()

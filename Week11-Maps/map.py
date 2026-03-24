class Map:

    LOAD_FACTOR = .75

    def __init__(self):
        self._buckets = []
        for bucket in range(11):
            self._buckets.append([])
        self._number_of_items = 0

    # O(n) - copies from old buckets to new buckets
    def _resize(self):
        new_buckets = []
        # double + next prime is best or something
        for bucket in range(len(self._buckets) * 2):
            new_buckets.append([])

        old_buckets = self._buckets

        self._buckets = new_buckets

        for bucket_index in range(len(old_buckets)):
            for pair in old_buckets[bucket_index]:
                self._buckets[self._get_bucket_index(pair[0])].append(pair)



    def _get_bucket_index(self, key):
        return hash(key) % len(self._buckets)

    # O(1) average
    def __setitem__(self, key, value):
        if self._number_of_items / len(self._buckets) >= self.LOAD_FACTOR:
            self._resize()

        bucket_index = self._get_bucket_index(key)
        for pairs in self._buckets[bucket_index]:
            # did find the key, updated the value
            if pairs[0] == key:
                pairs[1] = value
                return
        # didn't find the key
        self._buckets[bucket_index].append([key, value])
        self._number_of_items += 1

    # O(1)
    def __getitem__(self, key):
        bucket_index = self._get_bucket_index(key)
        for pairs in self._buckets[bucket_index]:
            if pairs[0] == key:
                return pairs[1]
        raise KeyError("not found")
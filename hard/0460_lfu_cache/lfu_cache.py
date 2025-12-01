from typing import Dict, Tuple
from collections import OrderedDict


class LFUCache:
    def __init__(self, capacity: int):
        """
        Initializes an LFU Cache with a fixed capacity.

        Using:
        - key_to_val_freq: {key: (value, frequency)}
        - freq_to_keys: {frequency: OrderedDict(key: None)}
        - min_freq: tracks the current minimum frequency in the cache.

        Args:
            capacity (int): Maximum number of items the cache can hold.
        """
        self.capacity = capacity
        self.size = 0

        self.key_to_val_freq: Dict[int, Tuple[int, int]] = {}
        self.freq_to_keys: Dict[int, OrderedDict] = {}

        self.min_freq = 0

    def get(self, key: int) -> int:
        """
        Retrieves the value of the given key if present in the cache.
        Updates the key's frequency.

        Time Complexity: O(1)  
        Space Complexity: O(capacity)
        """
        if key not in self.key_to_val_freq:
            return -1

        value, freq = self.key_to_val_freq[key]

        # remove from current freq bucket
        self.freq_to_keys[freq].pop(key)

        # if empty and freq == min_freq → update min_freq
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # add to new freq bucket
        new_freq = freq + 1
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = OrderedDict()

        self.freq_to_keys[new_freq][key] = None
        self.key_to_val_freq[key] = (value, new_freq)

        return value

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair.
        If capacity is full, evicts the Least Frequently Used key.
        Ties are broken by LRU inside each frequency bucket.

        Time Complexity: O(1)  
        Space Complexity: O(capacity)
        """
        if self.capacity == 0:
            return

        if key in self.key_to_val_freq:
            # update value + increase frequency (via get)
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self.get(key)
            return

        # Evict if needed
        if self.size == self.capacity:
            # evict LRU key in min_freq bucket
            freq_bucket = self.freq_to_keys[self.min_freq]
            evict_key, _ = freq_bucket.popitem(last=False)

            if not freq_bucket:
                del self.freq_to_keys[self.min_freq]

            del self.key_to_val_freq[evict_key]
            self.size -= 1

        # Insert new key with freq = 1
        self.key_to_val_freq[key] = (value, 1)
        if 1 not in self.freq_to_keys:
            self.freq_to_keys[1] = OrderedDict()
        self.freq_to_keys[1][key] = None

        self.min_freq = 1
        self.size += 1

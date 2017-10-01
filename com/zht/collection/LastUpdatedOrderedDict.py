from collections import OrderedDict


class LastUpdatedOrderedDict(OrderedDict):
    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value, **kwargs):
        containsKey = 1 if key in self else 0
        if containsKey:
            del self[key]
            print 'Remove exsiting key ', key
        elif len(self) >= self._capacity:
            # last=False, the first added entry
            # last=True, the last added entry
            first_added_entry = self.popitem(last=False)
            print 'Remove ', first_added_entry

        print 'Add ', (key, value)
        OrderedDict.__setitem__(self, key, value)


if __name__ == '__main__':
    last_updated_ordered_dict = LastUpdatedOrderedDict(5)
    for i in range(10):
        last_updated_ordered_dict[i] = i

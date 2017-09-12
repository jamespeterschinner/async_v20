class IndexDict(dict):
    """A dictionary that can be indexed via its position or key"""
    copy_slice = slice(None, None, None)

    def __getitem__(self, item):
        #  return a copy of self if a blank slice is passed
        if item == self.copy_slice:
            result = IndexDict(self.copy())
        else:
            try:
                # Try to access value like a normal dict
                result = super().__getitem__(item)
            except (KeyError, TypeError):
                # if it failed Create a list of values to use as a look up
                lookup = tuple(self.items())
                try:
                    result = IndexDict(lookup[item])
                except TypeError:
                    # if that failed there might be a mix between key & int in the slices
                    # resolve key's to int's and then try and take the slice
                    slice_item = item.start, item.stop, item.step
                    item = slice(*[self.index_lookup(key)
                                   if not isinstance(key, (int, type(None)))
                                   else key
                                   for key in slice_item])
                    result = IndexDict(lookup[item])
        return result

    def key_lookup(self, index):
        """return the key from a numeric index"""
        result = None
        try:
            result = list(self.keys())[index]
        except TypeError:
            if index in self.keys():
                result = index
        return result

    def index_lookup(self, key):
        """return the index from a key"""
        result = None
        lookup = dict([(key, index) for index, key in enumerate(self.keys())])
        try:
            result = lookup[key]
        except KeyError:
            result = list(lookup.values())[key]
        return result

    def reverse_lookup(self, value):
        """return index and key from corresponding value"""
        result = None
        reversed = dict([(self[key], (index, key)) for index, key in enumerate(self.keys())])
        try:
            result = reversed[value]
        except KeyError:
            result = list(reversed.values())[value]
        return result

    def __repr__(self):
        return self.__class__.__name__ + str(dict([((index, key), self[key])
                                                   for index, key in enumerate(self.keys())]))

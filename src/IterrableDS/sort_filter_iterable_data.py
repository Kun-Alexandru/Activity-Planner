class ItterableDataStructure:
    def __init__(self, new_itterable=None):
        if new_itterable == None:
            new_itterable = {}
        self._data = new_itterable
        self._itteration_index = 0

    def __setitem__(self, key, value):
        self._data[key] = value

    def __getitem__(self, key):
        return self._data[key]

    def __delitem__(self, key):
        del self._data[key]

    def __iter__(self):
        self._itteration_index = 0
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def values(self):
        return self._data.values()

    def pop(self, *arguments):
        return self._data.pop(*arguments)

    def append(self, item):
        if type(self._data) == type(list()):
            self._data.append(item)
            return True
        else:
            return False

    def next(self):
        index = self._itteration_index
        if index is None or index >= len(self._data):
            self._itteration_index = None
            raise StopIteration()
        value = list(self._data)[index]
        self._itteration_index = index + 1
        return value

def standard_compare(item1, item2):
    # ascending order
    if item1 > item2:
        return False
    else:
        return True

def standard_function_filter(element):
    if element < 0:
        return True
    else:
        return False

class ArrayOperations(object):

    def gnomeSort(givenArray, function = None):

        if function is None:
            function = standard_compare

        index = 0

        while index < len(givenArray):
            if index == 0:
                index = index + 1
            if function(givenArray[index], givenArray[index - 1]) == False:
                index = index + 1
            else:
                givenArray[index], givenArray[index - 1] = givenArray[index - 1], givenArray[index]
                index = index - 1

        return givenArray

    def selfFilter(givenArray, acceptance = None):

        if acceptance is None:
            acceptance = standard_function_filter
        copyArray = givenArray[:]
        i = 0
        while i < len(copyArray):
            if (acceptance(copyArray[i]) == False and i != 0):
                del copyArray[i]
                i = i - 1
            elif acceptance(copyArray[i]) == False and i == 0:
                del copyArray[i]
            else:
                i = i + 1

        return copyArray


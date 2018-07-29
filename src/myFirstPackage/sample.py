# A very simple class to be called for testing
class Sample:

    def __init__(self):
        pass

    def func(self, x):
        return x + 1


# trivial call
if __name__ == '__main__':

    sample = Sample()

    inputValues = range(0, 10)
    outputArray = []
    sampleDict = dict()

    for i in inputValues:
        output = sample.func(i)
        outputArray.append(output)
        sampleDict[i] = output

    print('Sample value: ', sample.func(2))

    print('Input array: ', inputValues)
    print('Output array: ', outputArray)
    print('Sample dict: ', sampleDict)
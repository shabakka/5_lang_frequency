import codecs
import re
import operator

def load_data(filepath):
    result = []
    with codecs.open(filepath) as file:
        asdf = file.readlines()
        for i in asdf:
            result.append(i)
    return result
    pass


def get_most_frequent_words(text):
    slov = {}
    list = load_data(text)
    for line in list:
        matches = re.findall(r'(\w+)\b', line)
        for match in matches:
            if match not in slov:
                slov[match] = 1
            else:
                slov[match] = slov.get(match) + 1
    valuest = []
    for x,y in slov.items():
        valuest.append(y)
        valuest.sort(reverse=True)
    sorted_slov = sorted(slov.items(),key=operator.itemgetter(1),reverse=True)
    for i in sorted_slov[:10]:
        print(i[0])

#sorting only words with length > 4
#filtredItems = filter(lambda x : len(x[0]) > 4, slov.items())
#sorted_slov = sorted(filtredItems, key=operator.itemgetter(1), reverse=True)

if __name__ == '__main__':
    path = 'D:/test/voynaimirtom1,2.txt'
    get_most_frequent_words(path)
    pass

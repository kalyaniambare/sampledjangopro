def solution(param):
    param = "".join([str(i) for i in param])

    list = []
    string_name = ""

    for i in str(param):
        list.append(i)

    if "-" in list:
        dash = list.pop(0)
        string_name += str(dash)

    for i in range(len(list)):
        for j in range(len(list) - 1):

            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            else:
                list[j], list[j + 1] = list[j], list[j + 1]
    return string_name + "".join(list)


LIST = ['-', 3, 2, 1]
s = solution(LIST)

sentence1 = "Hi all, my name is Tom...I am originally from Australia."
sentence2 = "I need to work very hard to learn more about algorithms in Python!"


def solution1(sentence):
    for p in "!?',;.":
        sentence = sentence.replace(p, '')
    data = sentence.split()
    sum1 = sum([len(i) for i in data])
    return sum1/len(data)

s1 = solution1(sentence1)
print(s1)
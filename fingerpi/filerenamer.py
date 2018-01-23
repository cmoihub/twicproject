import os
def check(filename):
    first = -1
    list_ = []
    for file in os.listdir("."):
        if file.endswith(".pickle"):
            list_.append(str(file[:1]))
    for i in range(len(list_)):
        list_[i] = int(i)
    if first is not list_[-1]:
        first = int(list_[-1]) + 1
        print (first)
    return first
'''str(check(filename))'''
for filename in os.listdir("."):
    if filename.endswith("0raw_img.pickle"):
        check(filename)
        os.rename(filename, str(check(filename)) + "raw_img.pickle")
'''
@File      :   censorDFA.py
@Author    :   lunzhiPenxil仑质
@Contact   :   lunzhipenxil@gmail.com
@License   :   AGPL3
@Copyright :   (C) 2022-2023, lunzhiPenxil
@Desc      :   一个基于DFA算法实现的高性能敏感词解析库
'''

import censorDFA

import time

if __name__ == '__main__':
    print('load file ...', end = '')
    t1 = time.perf_counter()
    textList = censorDFA.loadListFromFile('./input.txt')
    t2 = time.perf_counter()
    print(' done in : ' + str(t2 - t1))
    print('iter test ...', end = '')
    t1 = time.perf_counter()
    for textList_this in textList:
        pass
    t2 = time.perf_counter()
    print(' done in : ' + str(t2 - t1))
    print('load DFA  ...', end = '')
    t1 = time.perf_counter()
    DFAObj = censorDFA.DFA(textList)
    t2 = time.perf_counter()
    print(' done in : ' + str(t2 - t1))
    #DFAObj.dumpf('./output.json')
    while True:
        print('=' * 25)
        msg = input('input msg    >> ')
        if msg in ['.exit', '.quit']:
            break
        else:
            print('long match   >> ' + str(DFAObj.find(msg, mode = censorDFA.maxMatchType)))
            print('long output  >> ' + DFAObj.doReplace(msg, replaceMark='█', mode = censorDFA.maxMatchType))
            print('short match  >> ' + str(DFAObj.find(msg, mode = censorDFA.minMatchType)))
            print('short output >> ' + DFAObj.doReplace(msg, replaceMark='█', mode = censorDFA.minMatchType))

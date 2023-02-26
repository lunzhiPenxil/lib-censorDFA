import random
import time

import censorDFA

testSize = 100000

testTimes = 10000
testTargetSize = 1000
testTargetOffset = 900

# 来自真实案例的平均长度大致为 7.73
lenTarget = 7
lenOffset = 6

baseStr ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'

if __name__ == '__main__':
    wordList = []
    for i in range(testSize):
        wordLen = random.randint(lenTarget - lenOffset, lenTarget + lenOffset)
        str_this = ''
        for j in range(wordLen):
            str_this += random.choice(baseStr)
        wordList.append(str_this)

    print('iter test ...', end = '')
    t1 = time.perf_counter()
    for textList_this in wordList:
        pass
    t2 = time.perf_counter()
    print(' done in : ' + str(t2 - t1))
    
    print('=' * 25)

    print('load DFA  ...', end = '')
    t1 = time.perf_counter()
    DFAObj = censorDFA.DFA(wordList)
    t2 = time.perf_counter()
    print(' done in : ' + str(t2 - t1))

    print('=' * 25)

    print('run  test ... ')
    print('  0%', end = '')
    t_flash = int(time.perf_counter())
    total_time = 0
    for i in range(testTimes):
        msgLen = random.randint(testTargetSize - testTargetOffset, testTargetSize + testTargetOffset)
        msg_this = ''
        for j in range(msgLen):
            msg_this += random.choice(baseStr)
        t1 = time.perf_counter()
        DFAObj.find(msg_this)
        t2 = time.perf_counter()
        total_time += t2 - t1
        t_flash_now = int(time.perf_counter())
        if t_flash_now != t_flash:
            t_flash = t_flash_now
            print('\r  %d%% (%d/%d)' % (int((i + 1) * 100 / testTimes), i + 1, testTimes), end = '')
        elif i + 1 == testTimes:
            print('\r  100%% (%d/%d)' % (i + 1, testTimes))
    print('Done')
    print('')
    print('total count   : ' + str(testTimes))
    print('total time    : ' + str(total_time))
    print('average time  : ' + str(total_time / testTimes))
    print('=' * 25)

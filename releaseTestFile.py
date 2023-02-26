import random

testSize = 100000

# 来自真实案例的平均长度大致为 7.73
lenTarget = 7
lenOffset = 6

baseStr ='ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'

if __name__ == '__main__':
    res = []
    for i in range(testSize):
        wordLen = random.randint(lenTarget - lenOffset, lenTarget + lenOffset)
        str_this = ''
        for j in range(wordLen):
            str_this += random.choice(baseStr)
        res.append(str_this)
    with open('input.txt', 'w', encoding = 'utf-8') as f:
        f.write('\n'.join(res))

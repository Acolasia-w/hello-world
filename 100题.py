"""
题目022：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""


def t22():
    for a in ['x', 'y', 'z']:
        for b in ['x', 'y', 'z']:
            for c in ['x', 'y', 'z']:
                if a != b and b != c and c != a:
                    if a != 'x' and c != 'x' and c != 'z':
                        print('a' + a, 'b' + b, 'c' + c)


"""
题目023：
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""


def t23():
    num = 7
    for i in range(num):
        blank = abs(num // 2 - i)
        print(' ' * blank + '*' * (num - 2 * blank))


"""
题目026：利用递归方法求5!。
"""


def fac(x):
    if x > 1:
        return x * fac(x - 1)
    else:
        return x


def t26():
    print(fac(5))


"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""


def output(s, length):
    if length == 0:
        return
    print(s[length - 1])
    output(s, length - 1)


def t27():
    s = input('please input a string:')
    length = len(s)
    output(s, length)


"""
题目029：给一个不多于5位的正整数，
要求：一、求它是几位数，二、逆序打印出各位数字。
"""


def t29():
    s = str(input('please input a number:'))
    print(len(s))
    print(s[::-1])


"""
题目030：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同
"""


def t30():
    s = str(input('please input a number:'))
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[- i - 1]:
            print('false')
            break
    else:
        print('true')


"""
题目031：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""


def t31():
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    inp = input('please input a alf:')
    arr = []
    for day in week:
        if inp == day[:len(inp)]:
            arr.append(day)
    if len(arr) > 0:
        print(arr[:len(arr)])
    elif len(arr) == 0:
        print('none')


"""
32.按相反的顺序输出列表的值
"""


def t32():
    # 方法一
    a = [1, 2, 3, 4, 5]
    print(a[::-1])
    # 方法二
    a = [1, 2, 3, 4, 5]
    a.reverse()
    print(a)
    # 方法三
    a = [1, 2, 3, 4, 5]
    a.sort(reverse=True)
    print(a)


"""
题目036：求100之内的素数
"""


def t36():
    arr = [2]
    for i in range(3, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)

    print(arr)


"""
题目037：对10个数进行排序
"""


def t37():
    a = [1, 4, 7, 3, 9, 0, 5, 2, 1, 6]
    a.sort()
    print(a)


"""
题目038：求一个3*3矩阵主对角线元素之和。
"""


def t38():
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s = 0
    n = len(a)
    for i in range(n):
        s += a[i][i]
    print(s)


"""
题目039：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""


def t39():
    aaa = [1, 5, 8, 14, 28, 39, 60, 89, 134, 324, 612, 900]
    b = 555
    for a in aaa:
        if b > a:
            aaa.insert(aaa.index(a), b)
            break
    else:
        aaa.append(b)
    print(aaa)


"""
题目044：两个3*3的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
"""


def t40():
    import numpy as np
    x = np.array([[12, 7, 3], [4, 5, 6], [7, 8, 9]])
    y = np.array([[5, 8, 1], [6, 7, 3], [4, 5, 9]])
    z = x + y
    print(z)


"""
题目045：统计 1 到 100 之和。
"""


def t45():
    s = 0
    for i in range(101):
        s += i
    print(s)
    print(sum(range(1, 101)))
    # 666


"""
题目046：求输入数字的平方，如果平方运算后小于 50 则退出。
"""


def t46():
    while 1:
        x = int(input('please input a number:'))
        print(x * x)
        if x * x < 50:
            break


"""
题目047：两个变量值互换
"""


def t47():
    a, b = 50, 60
    a, b = b, a
    print(a, b)


"""
题目062：查找字符串。
"""


def t62():
    s = 'abcdefg'
    print(s.find('c'))


"""
题目066：输入3个数a,b,c，按大小顺序输出。
"""


def t66():
    arr = []
    for i in range(3):
        a = int(input('please input a num:'))
        arr.append(a)
    arr.sort(reverse=True)
    print(arr)


"""
题目067：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组
"""


def t67():
    a = [6, 3, 10, 2, 5, 1, 4, 7, 9, 8]
    i = a.index(max(a))
    a[0], a[i] = a[i], a[0]
    i = a.index(min(a))
    a[-1], a[i] = a[i], a[-1]
    print(a)


"""
题目068：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
"""


def t68():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = 3
    b = a[-m:] + a[:-m]
    print(b)
    # 666


"""
题目070：写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度
"""


def t70():
    def geylength(string):
        return len(string)

    if __name__ == '__main__':
        x = 'abcde'
        print(geylength(x))


"""
题目076：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
"""


def t76():
    n = int(input('please input a num:'))
    s = sum(1 / i for i in range(n, 0, -2))
    print(s)
    # 666


"""
题目078：找到年龄最大的人，并输出
"""


def t78():
    person = {"li": 18, "wang": 50, "zhang": 20, "sun": 22}
    name, age = '', 0
    for p in person.keys():
        if person.get(p) > age:
            name, age = p, person.get(p)
    print(name, age)


"""
题目080：海滩上有一堆桃子，五只猴子来分。
第一只猴子把这堆桃子平均分为五份，多了一个，
这只猴子把多的一个扔入海中，拿走了一份。
第二只猴子把剩下的桃子又平均分成五份，又多了一个，
它同样把多的一个扔入海中，拿走了一份，
第三、第四、第五只猴子都是这样做的，
问海滩上原来最少有多少个桃子？
"""


def t80():
    for total in range(2, 10000):
        t = total
        remain = lambda t: (t - 1) / 5 * 4
        for i in range(5):
            t = remain(t)
            if t % 1 != 0:
                break
        else:
            print(total, t)
            break


"""
题目082：八进制转换为十进制
"""


def t82():
    print(bin(10))  # 十转二
    print(oct(10))  # 十转八
    print(hex(10))  # 十转16
    print(int('10', 8))  # 八转十
    print(int('10', 2))  # 二转十
    print(int('10', 16))  # 16转十


"""
题目083：求0—7所能组成的奇数个数。
"""


def t83():
    s = [i for i in '01234567']
    import itertools
    arr = []
    for i in range(1, 9):
        a = list(itertools.permutations(s, i))
        l = list(map(lambda x: int(''.join(x)), a))
        arr += l
        print(i, len(l))
    arr1 = set(arr)
    arr2 = list(filter(lambda x: x % 2 == 1, arr1))
    print(len(arr), len(arr1), len(arr2))


"""
题目085：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。
"""


def t85():
    x = int(input('please input a number:'))
    for i in range(1, 600):
        if int('9' * i) % x == 0:
            print(i)
            break
    else:
        print('hehe')


"""
题目096：计算字符串中子串出现的次数
"""


def t96():
    x = 'ababaabbaaa'
    print(x.count('ab'))


"""
题目100：列表转换为字典。
"""


def t100():
    l = ['ak17', 'b51', 'b52', '#64']
    d = {}
    for i in range(len(l)):
        d[i] = l[i]
    print(d)



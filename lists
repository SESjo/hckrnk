if __name__ == '__main__':
    N = int(input())

l = []
for _ in range(N):
    s = input().split()
    cmd = s[0]
    arg = s[1:]
    if s[0] != "print":
        eval("l.{0}{1}".format(cmd, tuple(map(int, arg))))
    else:
        print(l)

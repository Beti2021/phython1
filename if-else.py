  n = int(input().strip())
if n % 2 != 0:
    print('Weird')
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
elif n % 2 == 0 and 6 <= n <= 20: //hackerrank
    print('Weird')
else:
    print('Not Weird')

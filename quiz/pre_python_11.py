"""11. 최대공약수를 구하는 함수를 구현하시오

예시
<입력>
print(gcd(12,6))

<출력>
6
"""

def gcd(x, y):
    while y:
        x, y = y, x % y

    return x

print(gcd(12,6))
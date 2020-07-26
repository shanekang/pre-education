"""
문제
[9, 4, 3, 1, 12]을 오름차순으로 정렬하시오. 

---------------------------- 주어진 위치 = 0번 인덱스 ------------------------------

1. 최소값 찾기
- 0번 인덱스의 값은 9입니다. 현재까지는 9가 최소값입니다. 
- 1번 인덱스의 값 4와 최소값을 비교합니다. 4는 9보다 작으므로 4가 최소값입니다. 
- 2번 인덱스의 값 3과 최소값을 비교합니다. 3은 4보다 작으므로 3이 최소값입니다. 
- 3번 인덱스의 값 1과 최소값을 비교합니다. 1은 3보다 작으므로 1이 최소값입니다. 
- 4번 인덱스의 값 12와 최소값을 비교합니다. 1은 12보다 작으므로 1이 최소값입니다. 
- 최소값은 3번 인덱스의 1입니다. 

2. 최소값을 0번 인덱스에 배치하기 
- 3번 인덱스의 1을 0번 인덱스로 옮기고, 
  0번 인덱스의 9를 3번 인덱스로 옮깁니다. 

3. 결과
[1, 4, 3, 9, 12]
0번 인덱스까지 정렬되었습니다.

--------------------------- 주어진 위치 = 1번 인덱스 -----------------------------

1. 최소값 찾기 
- 1번 인덱스의 값은 4입니다. 현재까지는 4가 최소값입니다. 
- 2번 인덱스의 값은 3입니다. 3은 4보다 작으므로 3이 최소값입니다. 
- 3번 인덱스의 값은 9입니다. 3은 9보다 작으므로 3이 최소값입니다. 
- 4번 인덱스의 값은 12입니다. 3은 12보다 작으므로 3이 최소값입니다. 
- 최소값은 2번 인덱스의 3입니다. 

2. 최소값을 1번 인덱스에 배치하기 
- 2번 인덱스의 3을 1번 인덱스로 옮기고, 
  1번 인덱스의 4를 2번 인덱스로 옮깁니다. 

3. 결과
[1, 3, 4, 9, 12]
1번 인덱스까지 정렬되었습니다. 

--------------------------- 주어진 위치 = 2번 인덱스 -----------------------------
반복

--------------------------- 주어진 위치 = 3번 인덱스 -----------------------------
반복

--------------------------- 주어진 위치 = 4번 인덱스 -----------------------------
반복

결과
[1, 3, 4, 9, 12]

"""

def selection_sort(list):
  for i in range(len(list)-1):
    min_index = i
    for j in range(i+1, len(list)):
      if list[j] < list[min_index]:
        min_index = j
    list[i], list[min_index] = list[min_index], list[i]
  return list


list_1 = [3,2,1,6,8,7,4,5]
print(selection_sort(list_1))

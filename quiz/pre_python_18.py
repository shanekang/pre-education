"""18. 확장자가 포함된 파일 이름이 담긴 리스트에서 확장자를 제거하고
파일 이름만 추가 리스트에 저장하시오.

file = ['exit.py',hi.py','playdata.hwp',intro.jpg']

결과:
file = ['exit',hi','playdata',intro']

예시
<입력>
print(new_list)

<출력>
['exit', 'hi', 'playdata', 'intro']

"""

file = ['exit.py','hi.py','playdata.hwp','intro.jpg']
new_list = file[0][0:4], file[1][0:2], file[2][0:8], file[3][0:5]
print(new_list)

# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

c=input().lower()
a=[0 for _ in range(26)]
for i in c:
    a[ord(i)-ord('a')]+=1
m=max(a)
cnt=0
for i in a:
    if i==m:
        cnt+=1
if(cnt>1):
    print("?")
else:
    print(chr(a.index(max(a))+ord('a')).upper())

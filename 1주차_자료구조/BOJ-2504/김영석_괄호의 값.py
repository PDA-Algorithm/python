"""
1. 입력을 받는다
2. 입력을 스택에 하나씩 넣으면서, (, [는 그냥 넣고 ),]는 해당 짝을 만날때까지
    중간에 있는 모든 숫자들의 합을 기억해두고 있다가, 짝을 만나면 (는 2점, [는 3점을 곱해 스택에 넣어준다.
3. 만약 2단계에서 짝을 못만나거나, 모든 입력을 넣었는데 스택이 남아있다면 짝이 안맞으므로 0을 출력한다.
4. 마지막 입력을 처리한 후 스택이 비어있다면 점수를 출력 후 종료   
"""

brackets = input()
s = []
for bracket in brackets:
    if bracket in ( '(', '[' ):
        s.append(bracket)
        continue
    
    elif bracket == ')':
        try:
            # 점수 기록용
            temp = 0
            
            # 짝을 만날때까지 pop
            while True:
                
                item = s.pop()
                
                # 찾은경우
                if item == '(':
                    if temp:
                        s.append(2*temp)
                    else:
                        s.append(2)
                    break
                
                # 짝이 안맞는경우
                elif item == '[':
                    raise ValueError()
                
                # 점수를 만난 경우
                else:
                    temp += item
        
        # 스택에 아이템이 없는경우 or 불가능한 경우
        except:
            print(0)
            exit()
            
            
    elif bracket == ']':
        try:
            # 점수 기록용
            temp = 0
            
            # 짝을 만날때까지 pop
            while True:
                
                item = s.pop()
                
                # 찾은경우
                if item == '[':
                    if temp:
                        s.append(3*temp)
                    else:
                        s.append(3)
                    break
                
                # 짝이 안맞는경우
                elif item == '(':
                    raise ValueError()
                
                # 점수를 만난 경우
                else:
                    temp += item
        
        # 스택에 아이템이 없는경우 or 불가능한 경우
        except:
            print(0)
            exit()
    
try:
    print(sum(s))
except:
    print(0)
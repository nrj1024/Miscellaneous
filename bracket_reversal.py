from math import ceil

brackets=input('Enter the bracket string : ')
n=len(brackets)

if n%2!=0:
    print('Not possible')
else:
    stack=[]

    for i in range(n):
        if stack==[]:
            stack.append(brackets[i])
        elif brackets[i]=='{':
            stack.append('{')
        else:
            if stack[-1]=='{':
                stack.pop(-1)
            else:
                stack.append('{')

    open_b=0
    close_b=0

    for i in stack:
        if i=='{':
            open_b+=1
        else:
            close_b+=1

    no_of_reversals=ceil(open_b/2)+ceil(close_b/2)

    print(no_of_reversals)
    

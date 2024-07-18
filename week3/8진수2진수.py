num = input()
dict = {'0':'000', '1':'001', '2':'010', '3':'011', '4':'100', '5':'101', '6':'110', '7':'111'}

answer = []
for i in range(len(num)):
    answer.append(dict[num[i]])
if(num == '0'):
    print('0')
else:
    print(''.join(answer).lstrip('0'))


import re
N, Q = input().split(' ') #N is the number of lines of JSON object, Q is the number of lines of JSON query in the format of key1.key2.key3
lst = []
for i in range(int(N)):
    temp = re.sub(r'\s{2,}','',input()) #
    lst.append(temp)
string = ''.join(lst) #EXAMPLE:'[{"$schema": "http://json-schema.org/draft-03/schema#","name": "Product","type": "object","properties": {"id": {"type": "number","description": "Product identifier","required": true},"name": {"type": "string","description": "Name of the product","required":true},"price": {"type": "number","minimum": 0,"required": true},"tags": {"type": "array","items": {"type": "string"}},"stock": {"type": "object","properties": {"warehouse": {"type": "number"},"retail": {"type": "number"}}}}}' It is not well formatted JSON.
for j in range(int(Q)):
    temp = re.sub('\$','\$',input()) #If there is $ in keys, replace it with \$.
    ss = string #A copy of JSON.
    keys = temp.split('.') #Sperate keys by '.'
    for k in range(len(keys)):
        if k != len(keys)-1: #If key is not the last key
            s = '"' + keys[k] + '"\:\s*(\{.*\})'
            if re.findall(s,ss):
                ss= re.findall(s,ss)[0] #Extract the first level embedded JSON.
            else:
                print('null')
        else:
            ss = re.sub('"[^"]+"\:\s*(\{.*\})','',ss) #Make embedded JSON disappear.
            s = '"' + keys[k] + '"\:\s*((?:"[^"]+")|[^\{\},]+)[,\}]'
            if re.findall(s,ss):
                print(re.findall(s,ss)[0]) #Extract the value of the final key.
            else:
                print('null')

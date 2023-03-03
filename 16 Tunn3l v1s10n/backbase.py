import base64

with open('base.txt', 'r', encoding='utf8') as f:
    lines = f.readlines()
    
for line in lines:
    try:
        print(base64.b64decode(line))
    except:
        pass
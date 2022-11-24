'''
DATE=24th NOV 2022
DAY= thursday
TOPIC= strings
AUTHOR= pooja
'''
a='god bless you'
print(a.find('b')) #4
print(a.find('o')) #1
print(a.rfind('o')) #11 
print(a.count('s')) #2
print(a.count('l')) #1
print(a.replace('bless','loves')) #god loves you
print(a.replace('s','7')) #god ble77 you
print(a.replace('b','y')) #god yless you
b='        god loves you      '
print(b.strip()) #god loves you
print(b.lstrip()) #god bless you
print(b.rstrip()) #        god bless you
c='god','bless','you'
d='loves'.join(c)
print(d) #godlovesblesslovesyou
e='love you dad'
print(e.removeprefix('l')) #ove you dad
print(e.removesuffix('d')) #love you da
f='love you mom'
print(f.isalnum()) #false
f='loveyoumom'
print(f.isalnum()) #true
f='loveyou.mom'
print(f.isalnum()) #false
g='8'
print(g.isalpha()) #false
print(g.isalnum()) #true
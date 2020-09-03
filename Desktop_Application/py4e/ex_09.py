fname=input('Enter file: ')

if len(fname) < 1:fname='clown.txt'
hand=open(fname)

for lin in hand:
    lin=lin.rstrip()
    print(lin)
    wds=lin.split()
    print(wds)
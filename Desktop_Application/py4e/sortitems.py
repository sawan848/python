fname = input('enter file:')
if len(fname) < 1:
    fname = 'clown.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        #idiom:retrieve/create/update counter
        di[w] = di.get(w, 0)+1

# print(di)

# x=sorted(di.items())
# print(x[:5])

temp=list()
for k,v in di.items():
    # print(k,v)
    newtuple=(v,k)
    temp.append(newtuple)

# print('flipped: ',temp)
temp=sorted(temp,reverse=True)
# print('sorted ',temp[:5])

for v,k in temp[:10]:
    print(k,v)
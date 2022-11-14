aaa = list()
c = input('enter first MACD value: ')
c = int(c)
d = input('enter second MACD value: ')
d = int(d)
e = input('enter third MACD value: ')
e = int(e)
f = input('enther smoothing value for EMAs: ')
f = float(f)
b = input('enter first close price: ')
b = float(b)
aaa.append(b)
while len(aaa) < d:
    print('not enough close price for ema',d)
    b = input('enter next close price: ')
    b = float(b)
    aaa.append(b)
bbb = list()
countd = len(aaa)
bbb = aaa[(countd - d):]
x = 0
for i in bbb:
    x =x+i
emad = x / d
print('first ema', d , 'number is sma' , d ,' and equals to: ' , emad )
ccc = list()
ccc.append(emad)
x = 0
while len(aaa) < c:
    print('not enough close price for ema',c)
    b = input('enter next close price: ')
    b = float(b)
    aaa.append(b)
    g = ccc[x] + ((aaa[x+d] - ccc[x])*(f / (d + 1)))
    x = x+1
    ccc.append(g)
    print('next ema', d , ' equals to: ',ccc[x])
ddd = list()
countc =len(aaa)
ddd = aaa[(countc - c):]
y = 0
for i in ddd:
    y = y+i
emac = y / c
eee = list()
eee.append(emac)
print('first ema', c , 'number is sma' , c ,' and equals to: ' , emac )
print('first MACD line value is: ',ccc[c-d]-eee[0])
x = 0
fff = list()
while len(aaa) < c+e :
    print('not enough close price for MACD signal')
    b = input('enter next close price: ')
    b = float(b)
    aaa.append(b)
    g = ccc[x+c-d] + ((aaa[x+c] - ccc[x+c-d])*(f / (d + 1)))
    h = eee[x] + ((aaa[x+c] - eee[x])*(f / (c + 1)))
    ccc.append(g)
    eee.append(h)
    x=x+1
    print('next ema', d , ' equals to: ',ccc[x+c-d])
    print('next ema', c , ' equals to: ',eee[x])
    macdline = ccc[x+c-d] - eee[x]
    print('next MACD line equals to: ',macdline)
    fff.append(macdline)
y = 0
for i in fff:
    y = y+1
siglin1 = y / e
print
ggg = list()
ggg.append(siglin1)
print('first signal line value is: ', siglin1)
z = 0
x = 0
hhh = list()
while z == 0:
    b = input('enter next close price: ')
    if b == 'done':
        z = 1
    b = float(b)
    aaa.append(b)
    g = ccc[x+c+e-d] + ((aaa[x+c+e] - ccc[x+c+e-d])*(f / (d + 1)))
    ccc.append(g)
    h = eee[x+e] + ((aaa[x+c+e] - eee[x+e])*(f / (c + 1)))
    eee.append(h)
    macdline = ccc[x+c-d] - eee[x]
    fff.append(macdline)
    j = ggg[x] +((fff[x+e] - ggg[x])*(f / (e + 1)))
    ggg.append(j)
    x=x+1
    print('next ema', d , ' equals to: ',ccc[x+c+e-d])
    print('next ema', c , ' equals to: ',eee[x+e])
    print('next MACD line value equals to: ',fff[x+e-1])
    print('next signal line value equals to: ',ggg[x])
    k = fff[x+e-1] - ggg[x]
    hhh.append(k)
    print('MACD signal is:',hhh[x-1])
    if len(hhh) >1:
        if hhh[x-2]>0:
            if (hhh[x-1]-hhh[x-2])>(hhh[x-1]+hhh[x-2]):
                print('its a sell signal')
            else:
                print('no signal')
        else:
            if (hhh[x-1]-hhh[x-2])<(hhh[x-1]+hhh[x-2]):
                print('its a buy signal')
            else:
                print('no signal')

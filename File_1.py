import random as rn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('Pokemon.csv')

x = rn.randint(0,721)
y = rn.randint(0,721)

print(x,'vs',y)

datx = data.loc[x]
daty = data.loc[y]

namex = datx['Name']
namey = daty['Name']

hpx = datx['HP']
hpy = daty['HP']

attx = datx['Attack']
atty = daty['Attack']

defx = datx['Defense']
defy= daty['Defense']

spattx = datx['Sp. Atk']
spatty = daty['Sp. Atk']

spdefx = datx['Sp. Def']
spdefy = daty['Sp. Def']

speedx = datx['Speed']
speedy = daty['Speed']

print(namex,'vs',namey)

print('HP',hpx,hpy)
print('att',attx,atty)
print('def',defx,defy)
print('spatt',spattx,spatty)
print('spdef',spdefx,speedy)
print('speed',speedx,speedy)

if speedx > speedy:
    hit = attx - defy
    if hit<0:
        hpx = hpx+hit
    else:
        hpy = hpy-hit
else:
    hit = atty - defx
    if hit < 0:
        hpy = hpy+hit
    else:
        hpx = hpx-hit

if hpx<0 or hpy<0:

    print('\nOverall Score after a fight')
    print(namex,hpx)
    print(namey,hpy)

    if(hpy<0):
        print(namex,'WON')
    else:
        print(namey,'WON')
else:
    while(not(hpx<0 or hpy<0)):
        if(hpx>hpy):
            hitagain = spattx -spdefy
            if hitagain < 0:
                hpx = hpx + hitagain
            else:
                hpy = hpy - hitagain
        else:
            hitagain = spatty -spdefx
            if hitagain < 0:
                hpy = hpy + hitagain
            else:
                hpx = hpx - hitagain

    print('\nOverall Score after a fight')
    print(namex,hpx)
    print(namey,hpy)

    if (hpy < 0):
        print(namex, 'WON')
    else:
        print(namey, 'WON')


---
title: lesvoorbereiding topic 8 numpy-plotlib
---

Numpy
=====

Kenmerken
---------

* Vergelijkbaar met list (array).
* Homogeen (lists niet)
* Mutable zoals list
* Geordend zoals list

Aanmaken
--------

```python
import numpy as np
eendimensionele_lijst = np.array[1, 2, 3]
tweedimensionel_lijst = np.array[[1,2,3], [4,5,6]]
```

Type van de elementen
---------------------

type van de array
    
```python
    type(lijst)
    numpy.ndarray
```

type van de elementen: homogeen, dus één waarde.

```python
    lijst.dtype
    dtype('int64')
```

Eigenschappen
-------------
```python
lijst = np.array([1, 2, 3], [4, 5, 6])

    lijst.ndim # dimensie: 2
    lijst.size # aantal elementen: 6
    lijst.shape # aantal rijen en kolommen (tuple): (2,3)
```

Een getal: scalar
Eendimensionele rij: vector
Tweedimensionele tabel: matrix (bijv. zwart-wit-afbeelding als een matrix van pixels)
Meerdimensioneel: tensor (bijv. een gekleurde afbeelding, een matrix van pixels, met voor elke pixel een vector met de kleurwaarde voor rood, groen en blauw (RGB)))

Functies om snel matrices te creëren
------------------------------------

```python
np.ones(shape=(4,5) # matrix 4 x 5 met eentjes
np.zeros((2, 3, 4)) # tensor 2 x 3 x 4 met nullen
np.identity(10) # matrix 10 x 10 met nullen en eentjes in de diagoneel
np.arange(0, 21, 2) # vector met even getallen tot en met 20 arrange(start, stop, step)
np.random.rand(3, 4) # matrix 3 x 4 met random getallen tussen 0 en 1
np.random.randint(low=1, hight=100, size=(2,3)) # matrix 2 x 3 met willekeurige gehele getallen tussen 1 en 100
```


Elementen uit een array selecteren
----------------------------------

### Scalar

```python
n = np.array(np.pi)
n.tile()
```

### Vector

```python
v = np.array([1, 2, 3, 4, 5])
v = [0] # eerste element
v = [-1] # laatste element
v = [1:] # alle elementen uitgezonderd eerste
```

### Matrices

```python
m = np.array([[1,2,3,4,5], [6,7,8,9,10]])
m[1][3] # de tweede rij, vierde kolom
m[1,3] # idem
m[1,:] # 2de rij, alle kolommen
m[:,3] # alle rijen, vierde kolom
m[1:,2:] # alles vanaf tweede rij en derde kolom
m[1:,:3] # alles vanaf tweede rij en tot en zonder vierde kolom
m[:, ::2] # alle rijen, kolommen met telkens één overslaan, dus 1ste, derde en vijfde.
```

Selecteren met een booleaanse expressie
---------------------------------------

```python
m = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(m[[True, True, False, False, True], [True, False, True, False, True]])
print(m[m > 5])
print(m[~(m % 2 == 0)])
print(m[~(m % 2 == 0) | (m > 5)])
print(m[~(m % 2 == 0) & (m > 5)])
```

Overlopen van de elementen
--------------------------

Optie 1: for-lus --> te vermijden, is te langzaam

```python
m = np.array([[1,2,3,4,5], [6,7,8,9,10]])
for row in m:
    for element in row:
        print(element * 5)
```
    
Optie 2: vectoriseren

```python
print(m * 5)
n = np.ones((2,3))
print(m + n) # telt de elementen van m op bij overeenkomstige elementen van n en creëert zo nieuwe matrix
```

### Broadcasting

Een matrix vermenigvuldigen met een matrix van een kleinere dimensie, met vergelijkbare maten.

Een matrix vermenigvuldigen met een vector (zelfde rijlengte)

```python
p = np.array([5, 2, 6, 10, 3])
print(m * p)
```

### Functies

```python
print(m.log10(x)
print(m.min())
print(m.max())
print(m.sum())
print(m.sum(axis=0)) # som van alle kolommen
print(m.sum(axis=1)) # som van alle rijen
```

Arrays herschikken
------------------

```python
np.reshape(m, (5,2)) # herschikken, maakt een copy. Wijzigt matrix niet.
m.shape(5,2) # wijzigt
np.reshape(m, (5,2)), order='C' # rijgewijs, verwijst naar programmeertaal C
np.reshape(m, (5,2)), order='F' # kolomgewijs, verwijst naar programmeer Fortran

a.flatten()
a.flatten(order='C')
a.flatten(order='F')

rij = np.random.randint(0,100,21)
rij[:, np.newaxis] # matrix 20 x 1
np.expand_dims(rij, axis=0) # matrix 1 x 20
```

Arrays samenvoegen en splitsen
--------------------------------

```python
nullen = np.zeros(4,4)
eentjes = np.ones(4,4)
np.concatenate((nullen, eentjes), axis=1) # naast elkaar zetten
np.concatenate((nullen, eentjes), axis=0) # onder elkaar zetten
np.tile(nullen, (2,3) # rijen twee keer herhalen, kolommen drie keer.
np.array_split(nullen, 2) # lijst van twee arrays
```

Matploblib: plotten
===================

Eenvoudige lijn
---------------

```python
# simpele lijn op basis van array

import matplotlib.pyplot as plt
import numpy as np

y = np.arange(1,100)
plt.plot(y)
plt.show()
```

Met x-as, y-as
--------------

```python
x = np.linspace(-1,1,100)
y = np.sin(x)
plt.plot(x,y,) 
plt.xlabel("x")
plt.ylabel("y = sin(x)")
plt.title("Sinus")
plt.show()
```
Met opmaak
----------

```python
x = np.random.randint(1,10,10)
plt.plot(x,'ro:') # r=red, o=cirkel, := stippellijn
plt.show()
```

```python
x = np.random.randint(1,10,10)
plt.plot(x, color="red", marker="s", linestyle='dotted')
plt.show()
```



Balkgrafiek met opmaak
---------------------

```python
cat = ["vogels", "vissen", "huisdieren"]
aantallen = [200, 500, 350]
plt.bar(cat,aantallen, color=["cyan", "red", "blue"])
plt.title("Aantallen per diersoort")
plt.show()
```

Pillow: werken met afbeeldingen
===============================

Pillow installeren
------------------

    pip intall pillow

Pillow gebruiken
-----------------

```python
from PIL import Image
im = image.open("cijfer.png")
im.show()
im.save("cijfer.jpg", "JPEG")
im.size # aantal kolommen (pixel width) en aantal rijen (pixel height)
im2 = im.resize((128,128)) # aspect ratio wordt niet behouden
im3 = im.resize((128,128)) # aspect ratio zal wel behouden worden
im2 = im.resize((128,128), resample=Image.NEAREST) # je geeft nu expliciet de methode nearest neighbour op voor resampelen
im = im.rotate(90,expland=1)
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im = im.transpose(Image.FLIP_LEFT_RIGHT)
```

Afbeeldingen en numpy-arrays
-----------------------------

```python
from PIL import Image
im = Image.open("download.png")
imbl = im.convert('L') # omzetten naar zwart-wit (L = luminance)
imarr = np.array(im) # image imzetten naar numpy array
print(imarr.shape) # (128, 256, 3), driedimensionele tensor met waarden voor de drie kleuren van rbg
imblarr = np.array(imbl)
print(imarr.shape) # (128,256), matrix met grijswaarden
imblarr = 255 - imlbarr # wit wordt zwart en zwart wordt wit
plt.imshow(imblarr, cmap="gray")
```


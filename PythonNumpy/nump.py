import numpy as np

x = np.array([1, 2, 3, 4])
x = np.array(["a", "b", "c"])

# ZERO ARRAYS
a = np.zeros(10)
a = np.zeros(10, dtype=int)
a = np.zeros((3, 4), dtype=int)
a = np.zeros([3, 4])
a = np.zeros([4, 8, 8])
# 4 adet 8e 8 array oluşturur
a = np.zeros([3, 8, 8, 5])

# SPECIFIC ELEMENT ARRAY
b = np.full((4, 5), 2)
# 2lerden oluşan 4e5 array
b = np.full(4, 5)
# 5lerden oluşan 4 elemanlı  array
b = np.full((4, 5), "a")
b = np.full((4, 5), 2.3)

# CONSECUTİVE NUMBERS ARRAY
c = np.arange(0, 10)
# c = np.arange(2,10)
# c = np.arange(2,20,4)
# 2den 20ye kadar +4 ekleyerek array oluşturur
# c = np.arange(35,6, -6)
# 35den 6ya +6 ekleyerek array oluşturur

# DIVIDING INTERVAL
d = np.linspace(1, 2)
# 1 ve 2 de dahil olacak şekilde, ikisi arasını default olarak 50 parçaya böler
d = np.linspace(1, 2, 3)
d = np.linspace(1, 2, num=3)
# ikisi aynı çıktıyı verir. 1-2 arasını 3 parçaya böler
d = np.linspace(1, 10.7, num=4, endpoint=False)
# endpointi dahil etmeyecek şekilde bölümleme yapar

# RANDOM INTEGER ARRAY
e = np.random.randint(1, 10, (3, 4))
# 1-10 arasından random olarak 3e4 array oluşturur
e = np.random.randint(1, 10, (2, 3, 4))
# 1-10 arası random, 2 adet 3e4 array

e = {}
for _ in range(20000):
    val = np.random.randint(1, 11)

    if val not in e:
        e[val] = 1
    else:
        e[val] += 1


# ARRAY OPERATIONS
f = np.array([1, 2, 3])
g = np.array([7, 8, 9])
h = f*g
# aynı indexteki elemanları birbirleriyle çarpar
h = f+g
h = f*3

# ARRAY ATTRIBUTE
k = np.random.randint(1, 10, (4, 3, 5))
# k = k.shape
# x.shape, Array'in kaça kaçlık olduğunu(x,y) verir.
# 4,3,5 çıktısını verir

# k = k.ndim
# x.ndim, Array'in kaç boyutlu olduğunu verir.
# kaç array, kaç kolon, kaç sütun olduğu

# k = k.size
# x.size, Array'in boyutunu, kaç elemana sahip olduğunu verir.
# 4*3*5 yani total size

k = k.dtype
# x.dtype, Array'in elemanlarının veri tipini verir.


### ARRAY RESHAPING
m = np.arange(1,11)
m = m.reshape(5,2)
# array'i 5e2 olacak şekilde değiştirir
n = np.arange(1,11)
n = n.reshape(5,2).ndim
# ndim ile kaç boyutlu olduğu döndürülür

### STACK
o = np.array([1,2,3,4])
p = np.array([5,6,7,8])
# r = np.stack([o,p])
# 2ye4
# stack, tek satırlı ve sütunsuz olan bu iki array'i alt alta birbirinin row'u şekl. birleştirir.
s = np.stack([o,p], axis=1)
# 4e2

### SPLITTING
t = np.array([1,2,3,4,5,6,7,8,9,10])
t = np.split(t , [2,5])
# t array'inin 2 ve 5. indexlerinden önce keserek farklı arrayler oluşturur.
t = t[1]

### INDEXING wıth MULTIDIMENSIONAL ARRAYS
u = np.arange(1,21).reshape(4,5)
v = u[2,2]
v = u[2][2]
v = u[3][1:3]
v = u[::2]
# başlangıç ve bitiş noktaları yok. 2şer 2şer atlayarak al
v = u[:,3]

### FANCY INDEXING
y = np.arange(1,15)
indexes = [0,2,4,6]
# y = y[indexes]
y = np.arange(12).reshape(3,4)
# y = y[ 1:3 , 2:5 ]
# y = y.shape
idx1 = [1,2,0]
idx2 = [1,0,2]
y = y[idx1, idx2]

y = np.arange(20)
y[[1,3,5,7]] = 100
y[[0,2,4,6]] = [000, 200, 400, 600]

### CONDITIONAL INDEXING
# z = np.arange(10)
# z = [z<5]
# değerlerin koşulu sağlama durumunu kontrol edip true false şeklinde döndürür
# z = z[z<5]
# koşulu sağlayan değerleri array şekl döndürür

# z = z[(z<3) | (z>5)]
# z = z[(z<3) & (z>5)]
# ile koşullar eklenebilir


### NUMPY SUM
a = np.arange(1,21).reshape(4,5)

# filt = a<10
# a = [a<10]
# true false döndürür
# a = a[filt]
# koşulu sağlayan değerleri döndürür

# a =np.sum(filt)
sum = np.sum(a)
# arraydeki tüm değerleri toplar

total = np.sum(a,axis=0)
# axis=0 sütun bazında toplama yapar
# axis=1 satır bazında topl. yapar

# print(sum)
# print(total.shape)


### NUMPY ALL
result = np.arange(1,21).reshape(4,5)
# print(result>0)
# tüm elemanları kontrol edip true false değerlerini döndürür

# result = np.all(result>5)
# tüm elemanları kontrol edip tek bir true ya da false değeri döndürür

# result = np.all(result>5 , axis=1)
# satır bazında koşulu kontrol edip true ya da false değerlerini her bir satır için döndürür
# result = np.all(result>5 , axis=0)
# sütun bazlı kontrol eder, tüm sütunlarda koşula uymayan değer old. 4 adet false değeri döner

## all ; and gibi, any ise or gibi düşünülebilir
## all'da tamamını kontrol eder
## any'de ise herhangi birinin koşula uyması yeterlidir



print(result)

# https://github.com/EnginAlpman/Python-Lectures/blob/master/numpy/numpy_introduction.ipynb


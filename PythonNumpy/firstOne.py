import numpy as np

x = np.array([1,2,3,4])
x = np.array(["a","b","c"])

### ZERO ARRAYS
a = np.zeros(10)
a = np.zeros(10, dtype=int)
a = np.zeros((3,4), dtype=int)
a = np.zeros([3,4])
a = np.zeros([4,8,8])
# 4 adet 8e 8 array oluşturur
a=np.zeros([3,8,8,5])

### SPECIFIC ELEMENT ARRAY
b = np.full((4,5),2)
# 2lerden oluşan 4e5 array
b = np.full(4,5)
# 5lerden oluşan 4 elemanlı  array
b = np.full((4,5),"a")
b = np.full((4,5), 2.3)

### CONSECUTİVE NUMBERS ARRAY
c = np.arange(0,10)
# c = np.arange(2,10)
# c = np.arange(2,20,4)
# 2den 20ye kadar +4 ekleyerek array oluşturur
# c = np.arange(35,6, -6)
# 35den 6ya +6 ekleyerek array oluşturur

### DIVIDING INTERVAL
d = np.linspace(1,2)
# 1 ve 2 de dahil olacak şekilde, ikisi arasını default olarak 50 parçaya böler
d = np.linspace(1,2,3)
d = np.linspace(1,2,num=3)
# ikisi aynı çıktıyı verir. 1-2 arasını 3 parçaya böler
d = np.linspace(1,10.7, num=4, endpoint=False)
# endpointi dahil etmeyecek şekilde bölümleme yapar

### RANDOM INTEGER ARRAY
e = np.random.randint(1,10, (3,4))
# 1-10 arasından random olarak 3e4 array oluşturur
e = np.random.randint(1,10, (2,3,4))
# 1-10 arası random, 2 adet 3e4 array

e ={}
for _ in range(20000):
    val = np.random.randint(1,11)

    if val not in e:
        e[val] =1
    else :
        e[val] +=1
 




print(e)
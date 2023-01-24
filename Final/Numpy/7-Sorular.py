import numpy as np
# ?5 tane 1 barındıran bir array oluşturun
print(np.ones(5))
# ?5 tane 0 barındıran bir array oluşturun
print(np.zeros(5))
# ?2'den 100'e kadar olan değerlerden 2'ye tam bölünebilenlerle bir array oluşturun
print(np.arange(2, 100, 2))
# ?5 tane 10 bulunan bir array oluşturun
print(np.array([10]*10))
print(np.ones(5)*10)
# ?1'den 16'ya kadar değer bulunduran 4x4'lük bir matris oluşturun
arr = np.arange(1, 17)
print(arr.reshape(4, 4))
# ?4x4'lük bir birim matris oluşturun
print(np.eye(4, 4))
# ?0 ile 5 arasında rastgele değerler üretin
print(np.random.randint(5))
print(np.random.rand() * 5)
# ?5 x 5'lik bir matrisi Gaussian Distribution'a Göre (randn() fonksiyonu) değerler üreterek oluşturun
print(np.random.randn(25).reshape(5, 5))
# ?1 ile 5 arasındaki mesafeyi eşit parçalara bölerek 20'lik bir array oluşturun
print(np.linspace(1, 5, 20))

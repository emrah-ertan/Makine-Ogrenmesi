import numpy as np
import matplotlib.pyplot as plt

# Eğitim seti
X = np.array([1, 2, 3])
D = np.array([3, 5, 7])
def Hesapla():
# Ağırlık katsayıları başlangıç değeri
    w1 = 1
    b = 1

# Öğrenme katsayısı
    eta = 0.005

# Epoch sayısı
    num_epochs = 20

# Hata dizisi
    E = np.zeros(num_epochs)

# Epoch döngüsü
    for epoch in range(num_epochs):

    # Her bir veri için ağırlık güncellemesi
        for j in range(len(X)):
        # Ağırlık güncellemesi
            w1 = w1 - eta * (-34 + 14 * w1 + 6 * b)
            b = b - eta * (-15 + 6 * w1 + 3 * b)

        # Mevcut ağırlıklar için yapay sinir ağının çıkışı hesaplanır
            v = w1 * X[j] + b
            y = v

        # X(j) girişi için yapay sinir ağı hatası
            e = D[j] - y

            print('w1 = {}; b = {}'.format(w1, b))

    # Epoch için karesel hata
        KareselHata = (1 / 2) * np.sum(e ** 2)
        print('*** Epoch = {}'.format(epoch + 1))
        print('E = {}'.format(KareselHata))

    # Hata dizisi güncellemesi
        E[epoch] = KareselHata


    # Ağırlık ve bias değerleri
        print('Optimizasyon sonucunda Ağırlık, Bias ve Karesel Hata Değerleri')
        print('w1 = {}; b = {}'.format(w1, b))
        print('E = {}'.format(KareselHata))


    # Hata grafiği
        plt.plot(np.arange(num_epochs) + 1, E)
        plt.xlabel('Epoch')
        plt.ylabel('E')
        plt.grid()
        plt.show()
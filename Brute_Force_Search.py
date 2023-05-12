import numpy as np

def Boyut_Hesapla():
    p = 0.0002
    pi = 3.14
    minimum_yaricap = 10e+6
    minimum_maliyet = 10e+6
    adim = 0.01
    yaricap_uzayi = np.arange(1, 10+adim, adim)

    for i in range(len(yaricap_uzayi)):
        h = 430/(pi*yaricap_uzayi[i]**2)
        M = p*(2*pi*yaricap_uzayi[i]**2 + 2*pi*yaricap_uzayi[i]*h)
        if M < minimum_maliyet:
            minimum_maliyet = M
            minimum_yaricap = yaricap_uzayi[i]

    print(f"\nMinimum maliyet için yarıçap değeri: {minimum_yaricap}")
    print(f"Minimum maliyet için yükseklik değeri: {430/(pi*minimum_yaricap**2)}")

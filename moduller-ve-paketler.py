
#? Moduller , kodumuzu güzellestirmek ve kolaylastırmak icin kullanmamıza olanak saglanayan sınıfları , fonksiyonları ve degiskenleri iceren yapılardır.
#? Moduller iki türlüdür. Hazır moduller olabilir veya kendi yazdıgımız modüller olabilir
#? Asagıda en basitinden bir modul nasıl iceri aktarılır ona bakalım.




################################################################################################################
################################################################################################################

#! Paketler ise ilgili modüllerin bir araya getirildiği klasörlerdir. Yani paketler birden çok modülü içerir.
#? Bir Paket nasıl tanımlanır ?

# projemiz/
#  __init__.py
#  moduller/
#  __init__.py
#  modul1
# .py
#  modul2.py
#?Pytho, “projemiz” adında bir paket oluşturdu ve içine “moduller” adında bir alt paket ekledi. “moduller” paketi ise “modul1.py” ve “modul2.py” adlı modülleri içeriyor.

# from projemiz.moduller import modul1
# modul1.fonksiyon()



#? Moduller nasıl içeri aktarılır?
#! 1) import modul_adi

import math as m

dir(m) # Burada 'm' olarak adlandırdıgımız modulun icindeki tüm sınıf fonksiyon gibi yapıları görebiliyoruz.
help(m) # Burada da 'm' olarak adlandırdıgımız modulun nasıl calıstıgını ogrenebiliyoruz.
help(m.factorial)

m.sqrt(16) # 'm' olarak adlandırdıgımız modulun icerisindeki 'sqrt' adlı fonksiyonu kullandık ve parametre olarak 16 degerini verdik.


#! 2) From modul_adi import * 
# Böyle bir içe aktarma işleminde adini verdigimiz modulden , tüm seyleri import ettik.
# Bu tür kullanımda , fonksiyonları çağırırken sadece func adı yazmamız yeterli . Yani fonksiyonları çağırırıken modul adı yazmamıza gerek yok.

#? from __future__ import *
#? division()  # Burada tekrar modul adı yazmadan , direkt __future__ modulundeki division() fonksiyonunu kullandık.


#! 3) From modul_adi import istenilenFonksiyon/Degisken/Class



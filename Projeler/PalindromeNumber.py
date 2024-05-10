"""
#Bu aşamada direk sayıyı str'ye çevirip index bazında giderek palindrome olup olmadığını inceledim.
def Palindrome(x):

    if x < 0:
        print("Negatif sayılar için palindromeluk durumu söz konusu değildir!")
    else:
        x_str = str(x)
        ters_x = x_str[::-1]
        if(x_str==ters_x):

            print(f"{x_str} sayısı palindrom sayıdır.")
        else:
            print(f"{x_str} sayısı palindrom sayı değildir.")

Palindrome(121)
Palindrome(-121)
"""

#Bu kısımda ise basamak kontrolü üzerinden sayının Palindrome olup olmadığını inceledim.
def Palindrome(x):
    x_str = str(x)
    uzunluk = len(x_str)
    if x <0:
        print("Negatif sayılar için palindromeluk durumu söz konusu değildir!")
    else:
        for i in range(uzunluk):
            if (x_str[i] != x_str[uzunluk-i-1]):#sayının sağdan  başlayarak her bir basamağını temsil eder.
                print(f"{x} sayısı palindrome değildir.")
                return
        print(f"{x} sayısı palindrome sayıdır.")


Palindrome(5435)
Palindrome(121)
Palindrome(-121)
Palindrome(0)
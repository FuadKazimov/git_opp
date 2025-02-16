# Bu tapşırıqda BankAccount sinifini yaradaraq istifadəçilərin bank hesablarını 
# idarə edəcəksiniz. İstifadəçilər hesab açıb, balanslarını idarə edə, pul çəkə və 
# köçürmə edə biləcəklər.
# Tələblər:
#     BankAccount sinifini yaradın və aşağıdakı atributları daxil edin:
#         hesab_nomresi – Unikal hesab nömrəsi
#         ad – Hesab sahibinin adı
#         balans – Hesab balansı (default olaraq 0)
#         valyuta – Hesabın valyutası (məsələn, "AZN", "USD", "EUR")
#         hesab_aktivdir – Hesabın aktiv olub-olmamasını göstərən dəyişən (default True)
#     Aşağıdakı metodları yaradın:
#         hesab_melumat() – Hesab haqqında bütün məlumatları ekrana çap edən metod
#         balans_artir(miqdar) – Hesaba müəyyən məbləğdə pul əlavə edən metod
#         pul_cek(miqdar) – Hesabdan pul çıxaran metod (əgər balans yetərsizdirsə, 
#         xəbərdarlıq etməlidir)
#         hesab_bagla() – Hesabı bağlayan metod (aktivliyini False edir, balans sıfır olmalıdır)
#         pul_kocur(diger_hesab, miqdar) – Başqa bir hesaba pul köçürən metod 
#         (balans yetərsizdirsə, xəbərdarlıq etməlidir)
# İcra Nümunəsi:
# Aşağıdakı əməliyyatları yerinə yetirin:
#     İki bank hesabı yaradın:
#         Birinci hesab: "Həsən Əliyev", 1000 AZN balans ilə
#         İkinci hesab: "Aygün Məmmədova", 500 AZN balans ilə
#     Hər iki hesabın məlumatlarını ekrana çıxarın.
#     Birinci hesaba 500 AZN əlavə edin.
#     İkinci hesabdan 200 AZN pul çəkin.
#     Birinci hesabdan ikinci hesaba 300 AZN köçürün.
#     Hər iki hesabın yenilənmiş məlumatlarını çap edin.
#     Birinci hesabı bağlamağa çalışın (əgər balans sıfır deyilsə, xəbərdarlıq edilməlidir).
#     İkinci hesabı tam boşaldıb bağlayın.

class BankAccount:
    def __init__(self, hesab_nomresi, ad, balans = 0, valyuta = "AZN"):
        self.hesab_nomresi = hesab_nomresi
        self.ad = ad
        self.balans = balans
        self.hesab_aktivdir = True
    def hesab_melumat(self):
        return(f"Hesab No: {self.hesab_nomresi}\nAd: {self.ad}\nBalans: {self.balans:.2f} {self.valyuta}\nAktivdir: {self.hesab_aktivdir}")
    
    def balans_artir(self, miqdar):
        if miqdar > 0:
            self.balans += miqdar
            print(f"{miqdar:.2f} {self.valyuta} balansiniza elave edildi")
    def pul_cek(self, miqdar):
        if miqdar > self.balans:
            print("Balansinizda kifayet qeder mebleg yoxdur! ")
        else:
            self.balans -= miqdar 
            print(f"{miqdar:.2f} {self.valyuta} balansinizdan cixarildi ")
    def hesabi_bagla(self):
        if self.balans == 0:
            self.hesab_aktivdir = False
            print("Hesab uğurla bağlandi.")
        else:
            print("Hesabi bağlamaq üçün balans sifir olmalidir!")
    
    def pul_kocur(self, diger_hesab, miqdar):
        if miqdar > self.balans:
            print("Balansda kifayət qədər vəsait yoxdur!")
        else:
            self.balans -= miqdar
            diger_hesab.balans += miqdar
            print(f"{miqdar:.2f} {self.valyuta} {diger_hesab.ad} adli şəxsə köçürüldü.")


hesab1 = BankAccount("001", "Həsən Əliyev", 1000)
hesab2 = BankAccount("002", "Aygün Məmmədova", 500)


hesab1.hesab_melumat()
hesab2.hesab_melumat()

hesab1.balans_artir(500)
hesab2.pul_cek(200)

hesab1.pul_kocur(hesab2, 300)

hesab1.hesab_melumat()
hesab2.hesab_melumat()

hesab1.hesab_bagla()

hesab2.pul_cek(hesab2.balans)
hesab2.hesab_bagla()


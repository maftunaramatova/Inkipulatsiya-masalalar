##1-masala:
# class BankHisobi:
#     def __init__(self,egasi,boshlangich_balans=0):
#         self.__egasi = egasi
#         self.__balans = boshlangich_balans
#
#     def get_egasi(self):
#         return self.__egasi
#
#     def get_boshlangich_balans(self):
#         return self.__balans
#
#     def pul_qosh(self,miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor")
#             return
#         self.__balans += miqdor
#
#     def pul_yech(self,miqdor):
#         if miqdor <= 0:
#             print("Noto'g'ri miqdor")
#         elif miqdor > self.__balans:
#             print("Mablag' yetarli emas!")
#         else:
#             self.__balans -= miqdor
#
# hisobi = BankHisobi("Maftuna",5_000_000)
# print(hisobi.get_egasi())
# print(hisobi.get_boshlangich_balans())
# hisobi.pul_qosh(200_000)
# print(hisobi.get_boshlangich_balans())
# hisobi.pul_yech(200_000)
# print(hisobi.get_boshlangich_balans())
# hisobi.pul_yech(200_000)
# hisobi.pul_qosh(-100_000)

##2-masala:
# class Foydalanuvchi:
#     def __init__(self,ism,parol):
#         self.ism=ism
#         self.__parol=parol
#
#     def get_ism(self):
#         return self.ism
#
#     def get_parol(self):
#         return self.__parol
#
#     def parolni_tekshir(self,kiritilgan_parol):
#         if self.__parol == kiritilgan_parol:
#             return True
#         else:
#             return False
#
#     def parolni_ozgartir(self,eski_parol,yangi_parol):
#         if self.__parol != eski_parol:
#             print("Eski parol noto'g'ri")
#             return False
#         elif len(yangi_parol) < 6:
#             print("yangi parol 6 ta belgidan iborat bo'lishi kerak")
#             return False
#         else:
#             print("Parol muvofiqaytli o'zgartirildi")
#             return True
# user = Foydalanuvchi("Maftuna","maxfiy123")
# print(user.get_parol())
# print(user.parolni_tekshir("noto'g'ri"))
# print(user.parolni_tekshir("maxfiy123"))
#
# user.parolni_ozgartir("xato","yangi456")
# user.parolni_ozgartir("maxfiy123","123")
# user.parolni_ozgartir("maxfiy123","yangiParoli")
#
# print(user.parolni_tekshir("maxfiy123"))
# print(user.parolni_tekshir("yangiParoli"))

##3-masala:
class Talaba:
    def __init__(self,ism,fan):
        self.__ism = ism
        self.__fan = fan
        self.__baholar = []

    def get_ism(self):
        return self.__ism

    def get_fan(self):
        return self.__fan

    def baho_qosh(self,baho):
            if not( 0 <= baho <= 100):
                print("Baho 0 va 100 oralig'ida bo'lishi kerak ")
                return
            else:
                self.__baholar.append(baho)

    def get_baholar(self):
        return self.__baholar.copy()

    def ortacha_baho(self):
        if not self.__baholar:
            print("Hali baholar yo'q!")
            return None
        else:
            return round(sum(self.__baholar)/len(self.__baholar), 2)

talaba = Talaba("Nodira","Matematika")
talaba.baho_qosh(85)
talaba.baho_qosh(92)
talaba.baho_qosh(78)
talaba.baho_qosh(150)
print(talaba.get_baholar())
print(talaba.ortacha_baho())

baholar = talaba.get_baholar()
baholar.append(999)
print(talaba.get_baholar())


##4-Masala:




















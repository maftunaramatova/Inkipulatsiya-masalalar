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
# class Talaba:
#     def __init__(self,ism,fan):
#         self.__ism = ism
#         self.__fan = fan
#         self.__baholar = []
#
#     def get_ism(self):
#         return self.__ism
#
#     def get_fan(self):
#         return self.__fan
#
#     def baho_qosh(self,baho):
#             if not( 0 <= baho <= 100):
#                 print("Baho 0 va 100 oralig'ida bo'lishi kerak ")
#                 return
#             else:
#                 self.__baholar.append(baho)
#
#     def get_baholar(self):
#         return self.__baholar.copy()
#
#     def ortacha_baho(self):
#         if not self.__baholar:
#             print("Hali baholar yo'q!")
#             return None
#         else:
#             return round(sum(self.__baholar)/len(self.__baholar), 2)
#
# talaba = Talaba("Nodira","Matematika")
# talaba.baho_qosh(85)
# talaba.baho_qosh(92)
# talaba.baho_qosh(78)
# talaba.baho_qosh(150)
# print(talaba.get_baholar())
# print(talaba.ortacha_baho())
#
# baholar = talaba.get_baholar()
# baholar.append(999)
# print(talaba.get_baholar())
#

##4-Masala:
# class HaroratSensori:
#     def __init__(self,sensor_id,joylashuv):
#         self.__sensor_id = sensor_id
#         self.__joylashuv = joylashuv
#         self.__olchovlar = []
#         self.__min_harorat = -50
#         self.__max_harorat = 150
#
#     def get_sensor_id(self):
#         return self.__sensor_id
# 
#     def get_joylashuv(self):
#         return self.__joylashuv
#
#     def olchov_qosh(self,harorat,vaqt):
#         if not(self.__min_harorat <= harorat <= self.__max_harorat):
#             print("Xato: harorat -50 dan 150 gacha bo'lishi kerak!")
#         else:
#             self.__olchovlar.append({"harorat":harorat,"vaqt":vaqt})
#
#     def oxirgi_olchov(self):
#         if not self.__olchovlar:
#             return "Hali o'lchov yo'q"
#         return self.__olchovlar[-1].copy()
#
#     def ortacha_harorat(self):
#         if not self.__olchovlar:
#             return 0.0
#         jami = sum(o["harorat"] for o in self.__olchovlar)
#         return round( jami / len(self.__olchovlar),2)
#
#     def olchovlar_soni(self):
#         return len(self.__olchovlar)
#
#     def hisobot(self):
#         oxirgi = self.oxirgi_olchov()
#         if isinstance(oxirgi, str):
#             oxirgi_str = "yo'q"
#         else:
#             oxirgi_str = f"{oxirgi['harorat']} C,({oxirgi['vaqt']})"
#         return (
#             f"Sensor:{self.__sensor_id}|Joylashuv:{self.__joylashuv}"
#             f"O'lchovlar soni:{self.__olchovlar}\n"
#             f"O'rtacha harorat:{self.ortacha_harorat()}C\n"
#             f"Oxirgi o'lchov:{oxirgi_str}\n"
#         )
#
# sensor = HaroratSensori("s-001","1-1")
# sensor.olchov_qosh(22.5,"08:00")
# sensor.olchov_qosh(25.3,"12:00")
# sensor.olchov_qosh(19.8,"18:00")
# sensor.olchov_qosh(200,"20:00")
#
# print(sensor.oxirgi_olchov())
# print(sensor.ortacha_harorat())
# print(sensor.olchovlar_soni())
# print(sensor.hisobot())




















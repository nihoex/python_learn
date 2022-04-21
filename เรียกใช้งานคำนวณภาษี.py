#เรียกใช้งานคำนวณภาษี
from โปรแกรมย่อย import calcVat


saleAmt = int(input('ป้อนยอดขาย' ))

vatAmt = calcVat(saleAmt)
print('คิดภาษีได้' , vatAmt)
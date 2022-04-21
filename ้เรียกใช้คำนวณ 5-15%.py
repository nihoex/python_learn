#เรียกใช้งานคำนวณภาษี
saleAmt = int(input('ป้อนยอดขาย'))

#คือส่งพารามิเตอร์ไปให้โปรแกรมคำนวณ
if saleAmt > 1000 :
    vatAmt = vat5per (saleAmt)
elif saleAmt > 5000 : 
    vatAmt = vat7per (saleAmt)
else :
    vatAmt = vat15per (saleAmt)

print('คิดภาษีได้', vatAmt)
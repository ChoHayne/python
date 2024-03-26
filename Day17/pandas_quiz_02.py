import faker
import random
import pandas as pd

kr = faker.Faker('ko_KR')
# for i in range(100):
#     print(kr.name())

itemList = ['생필품','기호품','스낵류','음료류','주류']
paymentList = ['신용카드','체크카드','카카오페이','네이버페이']
timeList = ['오전','오후','저녁','밤','새벽']

Cu_data = {
    'customer':[kr.name() for i in range(1000)], #1000명
    'purchase_item':[random.choice(itemList) for i in range(1000)],
    'purchase_price':[random.randint(1000,50001) for i in range(1000)], #1000~50000
    'payment':[random.choice(paymentList) for i in range(1000)], #신용카드,체크카드,카카오페이, 네이버페이, 애플페이
    'time':[random.choice(timeList) for i in range(1000)] #오전 오후 저녁 밤 새벽
}

dfCU = pd.DataFrame(Cu_data)
dfCU.sort_values(by="customer")
dfCU.to_csv('cu_data.csv',index=False) #index False를 해서 index 값은 csv에 포함시키지 않음.
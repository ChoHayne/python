data = {
    'Menu':['Americano','Latte','Green Tea', 'Muffin','Sandwich'],
    'Sales':[100,150,90,80,60],
    'Price':[3000,3500,4000,2500,5000]
}

# 총 수입 열까지 만들어서 매출의 오름차순으로 모든 데이터를 보여주세요

import pandas as pd
df = pd.DataFrame(data)
df['Total Sales'] = df['Sales'] * df['Price']
print(df.sort_values('Total Sales'))

df.to_csv('megaCoffee.csv')
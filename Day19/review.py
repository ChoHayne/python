# 사이트 명 Jat to statistics
# Trends in annual Visitor Arrivals to Japan by Country/Area에 있는 CSV 데이터를 가져와서
#1. 2023년 Dec에 모든 나라의 일본 관강 인구를 파이 그래프로 보여주기
#2. 한국사람이 2017~2023년까지 tourism 파이 그래프 만들기



import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('CSV_JPN.csv',encoding='cp949')
filtered_df = df[(df['Year'] == 2023) & (df['Month (abbr)']=='Dec.')]
result_dict = dict(zip(filtered_df['Country/Area'],filtered_df['Visitor Arrivals']))
print(result_dict)

labels = result_dict.keys()
#replace: 35,423 <- ,를 빼버림 ","를 '' 아무것도 없음.으로 교체
sizes = [int(i.replace(",","")) for i in result_dict.values()]

# 파이그래프 보여주기 문법
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.show()
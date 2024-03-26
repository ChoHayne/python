# Pandas 소개
## 개념
"""
효율적인 데이터 관리와 분석을 위해 특별히 설계됨.
'DataFrame'과 'Series'라는 두가지 중요한 자료구조 제공
'DataFrame'~엑셀파일
'Series' ~ 엑셀파일의 각 열 column
"""

import pandas as pd

#  series / dataframe

# pdSeries = pd.Series(['🍒' for i in range(100)]) # Series 는 class
# print(pdSeries) #왼쪽은 인덱스 번호

# 시리즈(Series) 소개 및 생성방법
## 시리즈는 판다스의 기본 구성 요소 중 하나로, 1차원 배열과 비슷해요. 각 데이터는 고유한 인덱스를 갖고 있음.~엑셀의 한 열

#딕셔너리로 시리즈 만들기
# data_dict = {'a': 1, 'b':2, 'c':3}
# series_from_dict = pd.Series(data_dict)
# print(series_from_dict) # 이러면 index를 dict의 index랑 똑같이

## 라인전체 #은 Ctrl+/

# 데이터프레임(DataFrame) 소개 및 생성 방법
## 2차원 테이블

data = {
    '학원 지점': ['신촌점', '부평점', '강남점'],
    '시급':[25000, 26000, 30000],
    '강의 수':[1,3,1]
}
df = pd.DataFrame(data)
# # print(df)
# # print(df['시급']) # 이러면 시리즈 처럼 나옴
# # print(df[['학원 지점','시급']]) #두개이상을 하려면 [[]] 이렇게 해야됨
#
# # row로 데이터 추출
# print(df.loc[0], df.loc[2])
#
#
# # dafaframe 속성
# print(df.shape) # 행과 열의 수 (3,3)
# print(df.dtypes) # 각 열의 데이터 타입 ## object는 대부분 문자, int는 숫자
# print(df.columns) # 열 이름
# print(df.index) # 인덱스
# print(df.values[0][2]) #[행][열] [row][col]
#
# #메소드
# print(df.describe()) # 통계 요약
# print(df.sort_values(by='학원 지점')) #시급에서 오름차순으로 sort해줘
#

df['something'] = df['시급'] * df['강의 수']
print(df)
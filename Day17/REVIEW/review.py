# 복습퀴즈
## 현재 코인의 종류인 이더리움 코인의 3월 1일 부터 3월 26일까지 종가들을 날짜 별로 리스트화 하고
## 이를 엑셀화 시켜서 보여주는 코드 만들기

import FinanceDataReader as fdr

eth = fdr.DataReader("ETH/KRW", "2024-03-01","2024-03-25")
print(eth['Close'])

### 유명한 library들
# NumPy 과학계산, 다차원 배열
# Pandas 데이터 분석 및 조작 표형식에 유리
# Matplotlib 데이터 시각화, 그래프 및 차트
# Scikit-learn 머신러닝
# TensorFlow/Keras 딥러닝
# Flask/django 웹개발
# Requests
# ...
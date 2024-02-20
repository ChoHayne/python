coffee = ['americano','latte','vanila']
price = [2500,3000,3500]
sweetness = ['low','medium','high']
'''
ediya = list(zip(coffee,price)) #zip 서로 연결해줌
print(ediya)
# list 안 tuple형태로 표현 [('americano', 2500), ('latte', 3000), ('vanila', 3500)]

starbucks = dict(zip(coffee,price))
print(starbucks)
#결과값 : {'americano': 2500, 'latte': 3000, 'vanila': 3500} 오 내가 필요하던 그거야
'''
#원하는 형태: {'name':'americano','price':2500},{'name':'latte','price':3000},{'name':'vanila','price':3500},...
#{'그룹A':'아이템A1','그룹B':'아이템B1',...}이런형태가 국룰

starbucks = [{'coffeeName':c, 'coffeePrice': p, 'coffeeSweet': s} for c, p, s in zip(coffee,price,sweetness)]
print(starbucks)
#zip 갯수 상관x
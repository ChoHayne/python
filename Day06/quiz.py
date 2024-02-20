#영화 예매 프로그램 [ 자료구조를 적절히 사용]
'''
1. 사용자로부터 영화종류와 팝콘종류를 입력받음
각영화 팝콘의 가격
1:액션 영화 -10000원
2:로코 -8000원
3:공포 영화 -9000원
팝콘 종류
1. 치즈팝콘:6000원
2.카라멜팝콘:5000원
3. 일반팝콘 5000원
영화와 팝콘을 입력받고 구매한 영화내용, 팝콘의 이름, 총 값을 출력하는 프로그램
'''
'''
movie = dict(action=10000, romance=8000, horror=9000)
popcorn = {
    'cheese' : 6000,
    'caramel' : 5000,
    'original' : 5000
}
userMovie = input("어떤 영화를 보시겠습니까:")
userPopcorn = input("어떤 팝콘을 먹을래:")

print(f"당신이 볼 영화는 {userMovie}, 주문한 팝콘은 {userPopcorn}이며 총 가격은 {movie[userMovie]+popcorn[userPopcorn]}")
'''

theater = {
    'movie':{
        'movieList':['액션영화', '로맨스 코미디', '공포영화'],
        'price':[10000,8000,9000]
    },
    'popcorn':{
        'popcornList':['일반 팝콘','카라멜 팝콘','치즈팝콘'],
        'price':[5000,5000,6000]
    }
}
movie = int(input(f"{theater['movie']['movieList']}중 선택하세요(0~2번):"))
popcorn = int(input(f"{theater['popcorn']['popcornList']}중 선택하세요(0~2번):"))

print(f"당신이 선택한 영화는 {theater['movie']['movieList'][movie]},이며 팝콘은 {theater['popcorn']['popcornList'][popcorn]}이며 총 가격은 {theater['movie']['price'][movie] + theater['popcorn']['price'][popcorn]} 입니다.")
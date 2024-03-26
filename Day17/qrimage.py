import qrcode

sk = "https://ko.wikipedia.org/wiki/SK_%28%EA%B8%B0%EC%97%85%29#/media/%ED%8C%8C%EC%9D%BC:SK_logo.svg"
qr = qrcode.make(sk)
qr.save('./shoe.png') # 같은 경로에 저장함

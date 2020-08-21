# module
# import theater_module
# theater_module.price(3) # 3명이서 씨어터 모듈을 통해 영화보러감
# theater_module.morning_price(4) # 4명이서 씨어터 모듈을 통해 조조로 영화보러감
# theater_module.soldier_price(5) # 군인 5명이서 씨어터 모듈을 통해 영화보러감

# import theater_module as mv #as는 약어로 쓰겠다
# mv.price(3)
# mv.morning_price(3)
# mv.soldier_price(5)

# from theater_module import *
# price(3)
# morning_price(4)
# soldier_price(5)

# from theater_module import price,morning_price
# price(3)
# morning_price(4)
# soldier_price(5) #soldier는 import하지 않았으므로 에러발생

from theater_module import soldier_price as price
price(5)
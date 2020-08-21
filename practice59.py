# package

# import travel.thailand # import는 모듈이나 클래스만 가능

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from은 패키지클래스가 가능

# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to =vietnam.VietnamPackage()
# trip_to.detail()

# from random import *

from travel import *

trip_to = thailand.ThailandPackage()
trip_to.detail()

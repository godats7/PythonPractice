# pip install

# 기본적으로 제공되거나 타인으로부터 만들어진 패키지를  사용하자
# 구글에서 pypi에서 쓰면됨

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())

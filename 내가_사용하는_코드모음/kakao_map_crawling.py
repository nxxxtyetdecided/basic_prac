### 셀레니움으로 탭을 바꿔가며
### 원하는 곳을 검색해
### csv에 저장하는 코드

import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import csv

from bs4 import BeautifulSoup

# 구글 인증(본인에게 해당하는 headers 가져오기)
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"}

list = []

url = "https://map.kakao.com/"

# 현재파일에 있는 크롬 드라이버를 가져와서 열기
options = webdriver.ChromeOptions()  # 크롬 브라우저 옵션

# options.add_argument('headless') # 브라우저 안 띄우기 -> 본인은 확인을 위해 주석처리함
options.add_argument('lang=ko_KR')  # KR 언어
chromedriver_path = "chromedriver.exe"  # 크롬 드라이버 위치
driver = webdriver.Chrome(os.path.join(os.getcwd(), chromedriver_path), options=options)  # chromedriver 열기

# 1. 카카오 지도로 이동
driver.get(url)

searchloc = input("찾고싶은 곳")
filename = input("파일이름: 영어로치기")

# 2. 검색어 입력 후 찾기 버튼 클릭 xpath활용
search_area = driver.find_element_by_xpath('//*[@id="search.keyword.query"]')  # 검색 창
search_area.send_keys(searchloc)  # 검색어 입력
driver.find_element_by_xpath('//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)  # Enter로 검색

time.sleep(2)
# 3 장소 버튼 클릭
# driver.find_element_by_xpath('//*[@id="info.main.options"]/li[2]/a').send_keys(Keys.ENTER)

#더보기 버튼 클릭
driver.find_element_by_xpath('//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)


def storeNamePrint():
    time.sleep(0.2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    place_lists = soup.select('.placelist > .PlaceItem')

    for place in place_lists:
        temp = []
        place_name = place.select('.head_item > .tit_name > .link_name')[0].text  # cafeName
        category = place.select('.head_item > .subcategory')[0].text
        addr = place.select('.addr')[0].text

        description = place.select('.openhour > .periodWarp > a')[0].text

        link = place.select('.contact > a')[1]['href']

        temp.append(place_name)
        temp.append(category)
        temp.append(addr)
        temp.append(description)
        temp.append(link)

        list.append(temp) # 모든 정보를 한 리스트에 담기

    f = open(filename + '.csv', "w", encoding="utf-8-sig", newline="")
    writercsv = csv.writer(f)
    header = ['Name', 'Category', 'Addr', 'Desc', 'Link']
    writercsv.writerow(header)

    for i in list:
        writercsv.writerow(i)

    # f.close()

page = 1
page2 = 0

# 1페이지부터 34페이지까지 출력
for i in range(0, 34):

    # 페이지 넘어가며 출력
    try:
        page2 += 1
        print("**", page, "**")


        time.sleep(1)
        driver.find_element_by_xpath(f'//*[@id="info.search.page.no{page2}"]').send_keys(Keys.ENTER)
        storeNamePrint()
        if (page2) % 5 == 0:
            driver.find_element_by_xpath('//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
            page2 = 0

        page += 1
    except:
        break
print("**크롤링완료**")


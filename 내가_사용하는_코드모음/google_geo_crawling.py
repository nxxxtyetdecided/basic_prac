### google geocode를 이용하여 위도, 경도 크롤링

import googlemaps
import pandas as pd

file_name = 'began_restaurant'

df_list = pd.read_csv(file_name + '.csv', encoding='utf-8')

# 구글맵 키
google_key = '본인 google api key'
gmaps = googlemaps.Client(key=google_key)

# 위도 경도
place_lat = []
place_lng = []

# 위경도 최대최소값
# 우리나라 위도 경도값
max_lat = 38.0
min_lat = 33.0
max_lng = 132.0
min_lng = 126.0

# place
# df_list는 csv배열로 변경 해주기
cnt = 0
for place in df_list["Addr"]:
    # geocode 부분에 해결되지 않았다고 떠도 실행 잘됨
    tmp = gmaps.geocode(place, language='ko')

    # 구글맵 검색 될 경우
    if tmp:
        cnt += 1
        print(cnt)
        tmp_loc = tmp[0].get("geometry")
        tmp_lat = tmp_loc["location"]["lat"]
        tmp_lng = tmp_loc["location"]["lng"]

        # 우리나라 위도 경도 값 안에 들어있는 경우
        if min_lat <= tmp_lat <= max_lat and min_lng <= tmp_lng <= max_lng:
            place_lat.append(tmp_lat)  # 위도 추가
            place_lng.append(tmp_lng)  # 경도 추가

        # 우리나라 위도 경도 값안에 들어있지 않는 경우
        else:
            place_lat.append("0")
            place_lng.append("0")


    # 검색 안 될 경우 0으로 입력
    else:
        print('검색 안됨')
        place_lat.append("0")
        place_lng.append("0")

print("위경도 추가 완료")

# list -&gt; dataframe, 열 이름 변경
df_list2 = pd.DataFrame(place_lat)
df_list2 = df_list2.rename(columns={0: "lat"})
df_list3 = pd.DataFrame(place_lng)
df_list3 = df_list3.rename(columns={0: "lng"})

# dataframe 3개 합치기
df = pd.concat([df_list, df_list2, df_list3], axis=1)
# 위경도 0인 행 삭제
df = df.query("lat != '0'")

df.to_csv(file_name + "location.csv", encoding="utf-8-sig")

df.tail()

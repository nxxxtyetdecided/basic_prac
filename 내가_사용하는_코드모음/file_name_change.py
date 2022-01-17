import os

# 주어진 디렉토리에 있는 항목들의 이름을 담고 있는 리스트를 반환합니다.
# 리스트는 임의의 순서대로 나열
file_path = 'C:\\Users\\user\\Desktop\\pic_separate\\train\\sosungju\\'
file_names = os.listdir(file_path)

i = 1
for name in file_names:
    # src : 파일 경로 + 파일명
    src = os.path.join(file_path, name)
    dst = "sosungju"+str(i) + '.jpg'

    # dst = 파일 경로 + 변경할 파일 명
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1


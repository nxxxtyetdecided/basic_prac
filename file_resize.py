from PIL import Image
import os

raw_path = 'C:\\Users\\user\\Desktop\\albam\\'  # 원본 이미지 경로
token_list = os.listdir(raw_path)  # 원본 이미지 경로 내 폴더들 list

# 모든 이미지 resize 후 저장하기
for token in token_list: # 이미지명을 하나씩 token에 불러옴
    # 이미지 열기
    im = Image.open(raw_path+token)

    # 이미지 resize
    im = im.resize((250, 250))

    # 이미지 JPG로 저장
    im = im.convert('RGB')
    im.save(raw_path +token)
# 인스타그램 첫 페이지

### px를 사용하지 않고
### %나 vh, vw를 사용한 반응형 웹페이지로 구현
부득이 하게 max-width는 px로 설정

## 배운 점
1. position: fixed; 를 설정 후 부모의 width 값을 상속받으려면 %는 안된다.
    -> max-width로 설정해주었으나 width:100%; 도 같이 설정해 주는 것이 좋음(footer 부분 참고)
2. header나 footer를 position:fixed; 로 고정 후 다른 요소들을 가리지 않기 위해 padding 을 줘야한다.
    -> margin을 주면 header나 footer도 그만큼 같이 띄워짐.... why?
    -> footer는 bottom: 0 도 같이 설정해줘야 함
3. align-item, justify-contents 부분 추가 예정

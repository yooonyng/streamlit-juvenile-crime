# **🚔소년범죄와 주변환경의 관계**
![Alt text](/data/img06.jpg)


``` C
📌목차
1. 데이터셋 확인하기
2. 소년범죄 개념과 특징
3. 데이터 분석 목적
4. 데이터 분포를 통해서 알 수 있는 점
5. 저작권, 라이선스 정보
``` 

## 1️⃣. 데이터셋 확인하기
``` C
- 대검찰청_소년범죄자 범행동기
- 대검찰청_소년범죄자 부모관계
- 대검찰청_소년범죄자 교육정도
- 대검찰청_소년범죄자 범행 시 정신상태
- 대검찰청_소년범죄자 전회처분 상황
- 대검찰청_소년범죄자 처분결과
- 대검찰청_소년범죄자 재범기간 및 종류
``` 
소년범죄 데이터를 확인해서
범죄분류를 인덱스로 만들었고 총 범죄건수를 합쳐서 컬럼에 추가해준다.


## 2️⃣. 소년범죄 개념과 특징
> 법적으로 미성년에 해당하는 자의 범죄 행위를 뜻하고, 한국에서는 19세 미만 소년의 범죄 행위를 말한다.
> 소년 범죄는 그 내용에 따라 폭력범죄, 재산범죄, 강력범죄, 교통사범 등으로 구분된다.

1. 범죄 청소년 평균 연령의 저하이다. 대중 매체를 통해 청소년 문화 형성의 중심이 저연령화하고 있기 때문이다.
2. 2인 이상의 다수가 공모하여 범죄를 저지르는 집단화 경향의 추세를 보인다.
3. 여성 청소년 범죄가 증가하고 있다.
4. 소년 재범자가 증가하는 추세이다.
5. 소년 범죄에서 살인, 강도, 강간, 방화와 같은 죄질이 나쁘고 상대방에게 미치는 피해가 큰 강력범죄가 늘어나고 있다.

## 3️⃣. 데이터 분석 목적
이 데이터를 통해서 다음 3가지를 확인하고자한다.
1. 소년범죄의 가장 높은 범죄율 순위 10가지
2. 주변환경과 소년범죄의 연관성
3. 소년범죄의 재범률과 처분결과 상황
``` C
청소년 범죄자의 개인적 특성 및 소질을 중요시하는 개인적 요인인지
범죄자를 둘러싼 가정, 학교, 교우관계, 사회의 문화 또는
가치 체계에 의한영향을 중요시하는 사회·환경적 요인인지 확인해보자
``` 

## 4️⃣. 데이터 분포를 통해서 알 수 있는 점

1. 데이터 분석을 통해서 소년범죄의 가장 높은 범죄순위를 알 수 있었다.

```python
# px.bar를 이용해 차트 만들기

import plotly.express as px
fig2 = px.bar(top10_chart, x='범죄분류', y='총범죄건수',color_discrete_sequence=['firebrick'])
    st.plotly_chart(fig2)
```
![Alt text](/data/chart01.png)

---
2. 소년범죄의 부모관계를 확인할 수 있었으며
실부모와 미혼자부모관계의 차이는 별로 없었다.

```python
# alt.chart를 이용해 파이차트 만들기

import altair as alt
language = ['실(양)부모','미혼자부모관계','무부모','기혼','미상']
    my_choice = st.selectbox('부모 관계 선택',language)
    
    if my_choice == language[0]:
        alt_chart = alt.Chart(df_connect).mark_circle().encode(
        x = '실(양)부모',
        y = '총범죄건수',
        size = '실(양)부모').configure_mark(opacity=0.45,color='brown')
st.altair_chart(alt_chart)

```
![Alt text](/data/chart02.png)
---

3. 소년범죄의 교육정도를 확인할 수 있었고
가장 많은 교육수준이 고등학교 재중과 중학교 재중이 많았다.

```python
# px.pie를 이용해 파이차트 만들기

import plotly.express as px
fig1 = px.pie(df_study_sum,names=['중학교_재중', '중학교_중퇴', '중학교_졸업', '고등학교_재중', '고등학교_중퇴', '고등학교_졸업'],
            values=[13286, 1395, 1748, 23084, 9492, 4232],
            color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig1)
```
![Alt text](/data/chart03.png)
---

4. 소년범죄의 재범률을 확인하기 위해 동종재범과 이종재범을 구분했다.
동종재범의 경우 보통 1년 이내 발생이 가장 많았고 범죄종류는 절도가 가장 많았다.
이종재범의 경우도 1년 이내 발생이 가장 많았으며 절도와 폭행이 가장 많았다..

```python
# px.bar를 이용해 바차트 가로로 만들기

import plotly.express as px
fig1 = px.bar(df_again_1_T, x=df_again_1_T.columns, y=df_again_1_T.index, orientation='h')
st.plotly_chart(fig1)
```
![Alt text](/data/chart04.png)


## 5️⃣. 저작권, 라이선스 정보
- [📁 대검찰청 소년범죄 공공데이터](https://www.data.go.kr/data/3006690/fileData.do)   
- [📁 네이버 심리학용어사전](https://terms.naver.com/entry.naver?cid=41991&docId=2070185&categoryId=41991)





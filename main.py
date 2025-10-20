import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천기 🎯", page_icon="🌟")

st.title("🌈 MBTI로 알아보는 나의 진로 추천기!")
st.write("안녕! 😊 너의 MBTI를 선택하면 딱 어울리는 진로를 추천해줄게. "
         "성격과 찰떡인 학과 정보도 같이 알려줄게요 🎓")

# MBTI 리스트
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

mbti = st.selectbox("👉 나의 MBTI를 골라줘!", mbti_types)

# MBTI별 추천 데이터
career_data = {
    "ISTJ": {
        "careers": ["공무원", "회계사"],
        "explain": [
            "공무원은 체계적이고 책임감이 강한 사람에게 잘 맞아요 💼",
            "회계사는 꼼꼼하고 정확한 걸 좋아하는 성향에게 찰떡이에요 💰"
        ],
        "majors": ["행정학과, 법학과", "경영학과, 회계학과"]
    },
    "ISFJ": {
        "careers": ["간호사", "교사"],
        "explain": [
            "간호사는 따뜻하고 남을 잘 돌보는 성격에 어울려요 💊",
            "교사는 배려심 많고 책임감 있는 사람이 잘해요 👩‍🏫"
        ],
        "majors": ["간호학과, 보건학과", "교육학과, 유아교육과"]
    },
    "INFJ": {
        "careers": ["심리상담사", "작가"],
        "explain": [
            "심리상담사는 사람의 마음을 이해하고 돕는 데에 관심 많은 INFJ에게 어울려요 🧠",
            "작가는 깊은 생각과 감성을 글로 표현하는 걸 좋아하는 사람에게 잘 맞아요 ✍️"
        ],
        "majors": ["심리학과, 사회복지학과", "국문학과, 문예창작과"]
    },
    "INTJ": {
        "careers": ["데이터 분석가", "연구원"],
        "explain": [
            "데이터 분석가는 논리적 사고와 문제 해결력이 뛰어난 유형에게 좋아요 📊",
            "연구원은 독창적이고 분석적인 사람에게 잘 맞아요 🔬"
        ],
        "majors": ["통계학과, 컴퓨터공학과", "자연과학계열, 공학계열"]
    },
    "ENFP": {
        "careers": ["마케터", "크리에이터"],
        "explain": [
            "마케터는 창의적이고 사람과 소통하는 걸 즐기는 ENFP에게 딱이에요 💡",
            "크리에이터는 자유롭고 표현력이 풍부한 성격에 어울려요 🎥"
        ],
        "majors": ["경영학과, 광고홍보학과", "미디어커뮤니케이션학과, 디자인학과"]
    },
    "ENTJ": {
        "careers": ["기업가", "경영 컨설턴트"],
        "explain": [
            "기업가는 리더십 있고 도전 정신 강한 ENTJ에게 어울려요 🚀",
            "경영 컨설턴트는 전략적으로 생각하고 목표 지향적인 사람에게 좋아요 🧭"
        ],
        "majors": ["경영학과, 경제학과", "산업공학과, 국제경영학과"]
    },
    # 다른 MBTI 유형들도 여기에 추가 가능
}

# 결과 출력
if mbti in career_data:
    st.subheader(f"✨ {mbti} 유형에게 어울리는 진로는?")
    data = career_data[mbti]

    for i in range(2):
        st.markdown(f"#### 💼 진로 {i+1}: {data['careers'][i]}")
        st.write(data["explain"][i])
        st.markdown(f"📘 관련 학과: **{data['majors'][i]}**")
        st.divider()
else:
    st.info("해당 MBTI의 정보는 아직 준비 중이에요. 곧 업데이트될 예정이에요 😉")

st.write("💬 **Tip:** MBTI는 참고용이에요! 네가 좋아하는 일과 잘하는 일이 제일 중요하답니다 💖")

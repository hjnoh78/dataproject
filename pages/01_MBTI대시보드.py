import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 시각화", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# MBTI 열 감지
mbti_types = ["INTJ","INTP","ENTJ","ENTP","INFJ","INFP","ENFJ","ENFP",
              "ISTJ","ISFJ","ESTJ","ESFJ","ISTP","ISFP","ESTP","ESFP"]
mbti_cols = [c for c in df.columns if c.upper() in mbti_types]

# 국가 컬럼 추정
country_cols = [c for c in df.columns if "country" in c.lower() or c.lower() in ["nation","location","state","region","name"]]
country_col = country_cols[0] if country_cols else df.columns[0]

# UI
st.title("🌍 국가별 MBTI 분포 시각화")
st.write("국가를 선택하면 해당 국가의 MBTI 비율을 인터랙티브하게 볼 수 있습니다.")

selected_country = st.selectbox("국가를 선택하세요:", sorted(df[country_col].unique()))

# 선택한 국가 데이터 추출
row = df[df[country_col] == selected_country].iloc[0]
mbti_data = row[mbti_cols].astype(float).sort_values(ascending=False).reset_index()
mbti_data.columns = ["MBTI", "Count"]

# 비율 계산
total = mbti_data["Count"].sum()
mbti_data["Ratio"] = mbti_data["Count"] / total * 100

# 색상 설정 (1등은 빨간색, 나머지는 파랑 계열 그라데이션)
grad_colors = px.colors.sequential.Blues[::-1]  # 진한 파랑 → 연한 파랑
grad_used = grad_colors[:len(mbti_data)-1] if len(mbti_data) > 1 else grad_colors
colors = ["#FF4C4C"] + grad_used  # 첫 번째 막대(1등)는 빨강

# Plotly 그래프
fig = px.bar(
    mbti_data,
    x="MBTI",
    y="Ratio",
    text=mbti_data["Ratio"].map(lambda x: f"{x:.1f}%"),
    color="MBTI",
    color_discrete_sequence=colors,
    title=f"🇨🇦 {selected_country}의 MBTI 비율",
)

fig.update_layout(
    xaxis_title="MBTI 유형",
    yaxis_title="비율 (%)",
    title_font_size=22,
    plot_bgcolor="white",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

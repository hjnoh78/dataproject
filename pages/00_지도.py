import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import MarkerCluster, HeatMap

st.set_page_config(page_title="서울 인기 관광지 Top 10 (외국인 선호)", page_icon="🗺️", layout="wide")

st.title("🗺️ 외국인이 좋아하는 서울 주요 관광지 Top 10")
st.caption("Streamlit + Folium 데모 | 마커 클릭 시 간단 설명을 볼 수 있어요!")

# Top 10 spots (이름, 위도, 경도, 간단 설명)
spots = [
    {
        "name": "경복궁 (Gyeongbokgung Palace)",
        "lat": 37.5796, "lon": 126.9770,
        "desc": "조선의 법궁. 근정전과 근정문, 근정문 앞 수문장교대식이 유명해요."
    },
    {
        "name": "북촌한옥마을 (Bukchon Hanok Village)",
        "lat": 37.5826, "lon": 126.9830,
        "desc": "전통 한옥 골목 풍경으로 사진 스팟이 많아요. 주민 배려 필수!"
    },
    {
        "name": "명동 쇼핑거리 (Myeongdong Shopping Street)",
        "lat": 37.5636, "lon": 126.9850,
        "desc": "코스메틱, 길거리 음식, 쇼핑의 성지!"
    },
    {
        "name": "남산서울타워 (N Seoul Tower)",
        "lat": 37.5512, "lon": 126.9882,
        "desc": "서울의 스카이라인을 한눈에. 케이블카/남산순환버스 이용 가능."
    },
    {
        "name": "동대문디자인플라자 DDP (Dongdaemun Design Plaza)",
        "lat": 37.5665, "lon": 127.0090,
        "desc": "자하 하디드의 유선형 건축물. 전시·행사·야경이 매력적!"
    },
    {
        "name": "인사동 (Insadong)",
        "lat": 37.5740, "lon": 126.9853,
        "desc": "전통 공예·다도·갤러리. 골목골목 볼거리가 많아요."
    },
    {
        "name": "홍대 (Hongdae)",
        "lat": 37.5572, "lon": 126.9250,
        "desc": "젊음의 거리! 라이브뮤직, 클럽, 스트리트 퍼포먼스."
    },
    {
        "name": "롯데월드 (Lotte World, Jamsil)",
        "lat": 37.5110, "lon": 127.0980,
        "desc": "실내·야외 테마파크와 석촌호수 산책 코스."
    },
    {
        "name": "코엑스 & 별마당도서관 (COEX & Starfield Library)",
        "lat": 37.5126, "lon": 127.0588,
        "desc": "초대형 실내 서가 포토 스팟 + 전시·쇼핑의 메카."
    },
    {
        "name": "창덕궁 (Changdeokgung Palace)",
        "lat": 37.5823, "lon": 126.9910,
        "desc": "유네스코 세계유산. 후원 관광은 사전예약이 좋아요."
    },
]

# 사이드바 옵션
with st.sidebar:
    st.header("⚙️ 지도 옵션")
    tile = st.selectbox(
        "타일(배경지도) 선택",
        ["OpenStreetMap", "CartoDB positron", "CartoDB dark_matter", "Stamen Terrain", "Stamen Toner"],
        index=1,
    )
    use_cluster = st.checkbox("마커 클러스터 사용", value=True)
    show_heatmap = st.checkbox("히트맵 표시", value=False)
    st.markdown("---")
    st.markdown("**Tip**: 마커를 클릭하면 장소 설명을 볼 수 있어요!")

# 지도 중심(서울 시청 인근 좌표)과 초기 줌
center_lat, center_lon = 37.5665, 126.9780
m = folium.Map(location=[center_lat, center_lon], zoom_start=12, tiles=tile)

# 마커 추가
if use_cluster:
    cluster = MarkerCluster(name="관광지 클러스터").add_to(m)
    target = cluster
else:
    target = m

for s in spots:
    popup_html = f"<b>{s['name']}</b><br>{s['desc']}"
    folium.Marker(
        [s["lat"], s["lon"]],
        popup=popup_html,
        tooltip=s["name"],
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(target)

# 히트맵 옵션
if show_heatmap:
    heat_data = [[s["lat"], s["lon"], 1] for s in spots]
    HeatMap(heat_data, name="인기 히트맵", radius=30, blur=20).add_to(m)

# 레이어 컨트롤
folium.LayerControl().add_to(m)

# 렌더링
st_data = st_folium(m, width="100%", height=700)

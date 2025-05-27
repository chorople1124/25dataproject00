
import streamlit as st
import folium
from streamlit_folium import st_folium

# 서울 서초구 중심 좌표
SEOCHO_COORDS = (37.4765, 127.0334)

def main():
    st.title("서울시 서초구 지도")

    # folium 지도 생성
    m = folium.Map(location=SEOCHO_COORDS, zoom_start=14)

    # 마커 추가 (예: 서초구청)
    folium.Marker(
        location=SEOCHO_COORDS,
        popup="서초구청",
        tooltip="서초구청"
    ).add_to(m)

    # 스트림릿에 folium 지도 띄우기
    st_folium(m, width=700, height=500)

if __name__ == "__main__":
    main()

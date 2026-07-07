import streamlit as st
from pathlib import Path

st.set_page_config(page_title="파일깎기", page_icon="📁", layout="wide")

html_path = Path(__file__).with_name("파일깎기.html")

if not html_path.exists():
    st.error("HTML 파일을 찾을 수 없습니다. 같은 폴더에 파일깎기.html이 있는지 확인해 주세요.")
    st.stop()

html = html_path.read_text(encoding="utf-8")

st.title("파일깎기")
st.caption(
    "찐최종, 찐찐최종, 최종_진짜... 뒤죽박죽 쌓인 파일들, 이제 일일이 열어보며 확인하지 않아도 됩니다. "
    "AI가 파일명과 내용을 함께 분석해 최신 버전을 가려내고, 원하는 규칙에 맞춰 이름을 한 번에 정리해 드립니다."
)

st.components.v1.html(html, height=2200, scrolling=True)

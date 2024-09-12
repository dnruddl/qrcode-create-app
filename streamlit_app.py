import streamlit as st
import qrcode
from io import BytesIO
from PIL import Image

# 앱 제목
st.title("QR 코드 생성기")

# 사용자로부터 입력받기
text = st.text_input("QR 코드를 생성할 텍스트를 입력하세요:")

# QR 코드 생성 버튼
if st.button("QR 코드 생성"):
    if text:
        # QR 코드 생성
        qr_img = qrcode.make(text)
        
        # PIL 이미지를 바이트로 변환
        buf = BytesIO()
        qr_img.save(buf, format="PNG")
        buf.seek(0)
        
        # Streamlit에서 QR 코드 표시
        st.image(buf, caption="생성된 QR 코드", use_column_width=True)
        
        # QR 코드 다운로드 버튼 추가
        st.download_button("QR 코드 다운로드", buf, file_name="qrcode.png")
    else:
        st.warning("텍스트를 입력하세요!")

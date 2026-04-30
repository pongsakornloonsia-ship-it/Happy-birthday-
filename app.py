import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------------- CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffd6e0, #ffffff);
}
.title {
    text-align:center;
    font-size:50px;
    font-weight:bold;
}
.subtitle {
    text-align:center;
    font-size:20px;
    margin-bottom:40px;
}
.section {
    margin-top:80px;
    text-align:center;
}
.text {
    font-size:20px;
    max-width:700px;
    margin:auto;
}
.big {
    font-size:28px;
    font-weight:bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------- NAME INPUT ----------------
name = st.text_input("ใส่ชื่อแฟนของเธอ 💖")

if name == "":
    name = "เธอ"

# ---------------- HERO ----------------
st.markdown(f'<div class="title">For {name} ❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">ของขวัญที่เราตั้งใจทำให้</div>', unsafe_allow_html=True)

# ---------------- COUNTDOWN ----------------
target_date = datetime(2026, 6, 26)
now = datetime.now()
diff = target_date - now

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("นับถอยหลังถึงวันสำคัญ 🎂")

if diff.total_seconds() > 0:
    st.markdown(f'<div class="big">{diff.days} วัน {diff.seconds//3600} ชั่วโมง</div>', unsafe_allow_html=True)
else:
    st.success("วันนี้แหละ ❤️")

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- STORY ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("มันเริ่มจากวันธรรมดาๆ")
st.markdown(f'<div class="text">ตอนนั้นเราไม่ได้คิดเลยว่า {name} จะกลายเป็นคนสำคัญขนาดนี้</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- MEMORIES ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("ระหว่างทางของเรา")
st.markdown(f'<div class="text">เรามีทั้งช่วงเวลาที่ดี และไม่ดี แต่สุดท้ายเราก็ยังเลือกกัน</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- REASONS ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("ทำไมยังเลือกเธอ")
st.markdown(f"""
<div class="text">
- เพราะอยู่กับ {name} แล้วสบายใจ<br>
- เพราะเราเป็นตัวเองได้<br>
- เพราะต่อให้ทะเลาะ ก็ยังอยากมี {name}<br>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TYPING EFFECT ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("มีอะไรอยากบอก...")

placeholder = st.empty()
message = f"{name} คือหนึ่งในสิ่งที่ดีที่สุดในชีวิตเรา"

typed = ""
for char in message:
    typed += char
    placeholder.markdown(f"<div class='big'>{typed}</div>", unsafe_allow_html=True)
    time.sleep(0.05)

st.markdown('</div>', unsafe_allow_html=True)

# ---------------- SURPRISE ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
if st.button("กดรับของขวัญ 🎁"):
    st.balloons()
    st.success(f"สุขสันต์วันเกิดนะ {name} ❤️ อยู่กับเรานานๆนะ")
st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EXTRA ----------------
st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("805 วัน")
st.markdown(f'<div class="text">มันไม่ใช่แค่ตัวเลข แต่มันคือทุกช่วงเวลาที่เรามีกัน</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

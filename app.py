import streamlit as st
from datetime import datetime

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------- คำนวณวัน ----------
start_date = datetime(2024, 2, 14)
today = datetime.now()
days = (today - start_date).days

# ---------- CSS ----------
st.markdown(f"""
<style>
body {{
    background: linear-gradient(135deg, #ff758c, #ff7eb3, #fad0c4);
    color: white;
}}

.container {{
    text-align: center;
    padding: 50px 20px;
}}

.title {{
    font-size: 45px;
    font-weight: bold;
    margin-bottom: 20px;
}}

.days {{
    font-size: 80px;
    font-weight: bold;
    color: #fff;
    text-shadow: 0px 0px 20px rgba(255,255,255,0.8);
}}

.text {{
    font-size: 22px;
    max-width: 700px;
    margin: auto;
    margin-top: 20px;
}}

.card {{
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    margin-top: 40px;
}}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="container">
    <div class="title">เราอยู่ด้วยกันมาแล้ว ❤️</div>
    <div class="days">{days} วัน</div>
    <div class="text">ตั้งแต่วันที่ 14 กุมภาพันธ์ 2024</div>
</div>
""", unsafe_allow_html=True)

# ---------- CARD ----------
st.markdown(f"""
<div class="card">
    <div class="text">
    ตอนนั้นเราอาจไม่ได้คิดอะไรขนาดนี้  
    แต่ตอนนี้…มันกลายเป็นทุกอย่างไปแล้วจริงๆ
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- MESSAGE ----------
st.markdown(f"""
<div class="card">
    <div class="text">
    ไม่ว่าจะมีช่วงดี หรือช่วงที่งอนกัน  
    สุดท้ายเราก็ยังเลือกกันอยู่ดี  
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- FINAL ----------
if st.button("กดดูต่อ 💌"):
    st.balloons()
    st.markdown(f"""
    <div class="card">
        <div class="text">
        สุขสันต์วันเกิดนะ ❤️  
        ขอบคุณที่อยู่กับเรามาตลอด {days} วัน  
        และหวังว่าจะมีอีกเยอะๆเลยนะ
        </div>
    </div>
    """, unsafe_allow_html=True)

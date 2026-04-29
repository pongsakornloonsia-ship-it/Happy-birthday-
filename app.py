import streamlit as st

st.set_page_config(page_title="805 Days With You ❤️", layout="wide")

# CSS ระดับโปร
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffd6e0, #ffffff);
}

/* hero image */
.hero {
    position: relative;
    text-align: center;
    color: white;
}

.hero img {
    width: 100%;
    border-radius: 20px;
}

.overlay {
    position: absolute;
    top: 40%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 40px;
    font-weight: bold;
    text-shadow: 0px 0px 10px black;
}

/* section */
.section {
    margin-top: 80px;
    text-align: center;
}

.text {
    font-size: 20px;
    max-width: 700px;
    margin: auto;
}

/* fade-in */
.fade {
    opacity: 0;
    transform: translateY(40px);
    animation: fadeIn 1.5s forwards;
}

@keyframes fadeIn {
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
""", unsafe_allow_html=True)

# 🔥 HERO (รูปแรกสำคัญสุด)
st.markdown('<div class="hero">', unsafe_allow_html=True)
st.image("images/pic1.jpg", use_container_width=True)
st.markdown('<div class="overlay">805 Days With You ❤️</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section fade">', unsafe_allow_html=True)
st.markdown('<div class="text">รูปนี้…คือจุดเริ่มต้นของทุกอย่าง</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# STORY
st.markdown('<div class="section fade">', unsafe_allow_html=True)
st.header("มันเริ่มจากวันธรรมดาๆ")
st.markdown('<div class="text">ตอนนั้นเราไม่ได้คิดเลยว่ามันจะกลายเป็น 805 วันแบบนี้</div>', unsafe_allow_html=True)
st.image("images/pic2.jpg", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# MEMORIES
st.markdown('<div class="section fade">', unsafe_allow_html=True)
st.header("ระหว่างทาง")
st.markdown('<div class="text">มีทั้งดี ทั้งงอน ทั้งทะเลาะ แต่สุดท้ายเราก็ยังอยู่ตรงนี้</div>', unsafe_allow_html=True)
st.image("images/pic3.jpg", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# REASONS
st.markdown('<div class="section fade">', unsafe_allow_html=True)
st.header("ทำไมถึงยังเลือกเธอ")
st.markdown("""
<div class="text">
- เพราะอยู่ด้วยแล้วสบายใจ<br>
- เพราะไม่ต้องพยายามเป็นคนอื่น<br>
- เพราะต่อให้ทะเลาะกัน ยังไงก็อยากมีเธอ<br>
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# FINAL MESSAGE
st.markdown('<div class="section fade">', unsafe_allow_html=True)
st.header("และสุดท้าย…")
st.markdown('<div class="text">805 วันมันไม่ใช่แค่เวลา แต่มันคือทุกอย่างที่เรามีกัน</div>', unsafe_allow_html=True)

if st.button("กดดูของขวัญ 🎁"):
    st.success("สุขสันต์วันเกิดนะ ❤️ อยู่กับเรานานๆนะ เราไม่อยากเสียเธอไปเลยจริงๆ")

st.markdown('</div>', unsafe_allow_html=True)

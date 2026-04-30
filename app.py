import streamlit as st
import time

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------- STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 0

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
}
.box {
    background: white;
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    text-align: center;
}
.big {font-size:28px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------- PROGRESS ----------
progress = st.session_state.step / 5
st.progress(progress)

st.markdown("<div class='box'>", unsafe_allow_html=True)

# ---------- STEP 0 ----------
if st.session_state.step == 0:
    st.markdown("<div class='big'>อยากให้เธอลองเล่นอะไรหน่อย 👀</div>", unsafe_allow_html=True)
    if st.button("เริ่ม"):
        st.session_state.step = 1
        st.rerun()

# ---------- STEP 1 ----------
elif st.session_state.step == 1:
    st.markdown("<div class='big'>คิดว่าเราจะพูดอะไร?</div>", unsafe_allow_html=True)
    st.radio("", ["บอกรัก", "ง้อ", "บ่น", "ไม่รู้"])
    
    if st.button("ต่อ"):
        st.session_state.step = 2
        st.rerun()

# ---------- STEP 2 ----------
elif st.session_state.step == 2:
    placeholder = st.empty()
    text = "จริงๆแล้ว..."
    
    typed = ""
    for c in text:
        typed += c
        placeholder.markdown(f"<div class='big'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(0.05)

    if st.button("ต่อไป"):
        st.session_state.step = 3
        st.rerun()

# ---------- STEP 3 ----------
elif st.session_state.step == 3:
    st.markdown("<div class='big'>805 วันที่ผ่านมา...</div>", unsafe_allow_html=True)
    st.write("มันมีทั้งดีและไม่ดี แต่สุดท้ายเราก็ยังอยู่ตรงนี้")

    if st.button("ต่อ"):
        st.session_state.step = 4
        st.rerun()

# ---------- STEP 4 ----------
elif st.session_state.step == 4:
    st.markdown("<div class='big'>มีอะไรอยากบอก</div>", unsafe_allow_html=True)

    msg = "เราไม่ได้ดีที่สุด แต่เราจะพยายามเพื่อเธอ"
    placeholder = st.empty()
    typed = ""

    for c in msg:
        typed += c
        placeholder.markdown(f"<div class='big'>{typed}</div>", unsafe_allow_html=True)
        time.sleep(0.04)

    if st.button("สุดท้ายแล้ว"):
        st.session_state.step = 5
        st.rerun()

# ---------- FINAL ----------
elif st.session_state.step == 5:
    st.balloons()
    st.markdown("<div class='big'>สุขสันต์วันเกิดนะ ❤️</div>", unsafe_allow_html=True)
    st.success("อยู่กับเรานานๆนะ")

st.markdown("</div>", unsafe_allow_html=True)

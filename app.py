import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="For You ❤️", layout="centered")

# ---------- CSS ----------
st.markdown("""
<style>
body {background: linear-gradient(#ffd6e0, white);}
.center {text-align:center;}
.big {font-size:30px; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# ---------- START ----------
st.markdown("<h1 class='center'>อย่าพึ่งรีบอ่านนะ 👀</h1>", unsafe_allow_html=True)

if st.button("กดเริ่ม"):
    
    st.markdown("<h2 class='center'>โอเค งั้นเริ่มจริงๆละ</h2>", unsafe_allow_html=True)
    time.sleep(1)

    # ---------- STEP 1 ----------
    choice = st.radio(
        "คิดว่าเราจะพูดอะไร?",
        ["บอกรัก", "บ่น", "ง้อ", "ไม่รู้เหมือนกัน"]
    )

    if choice:
        st.write("ฮ่าๆ เดี๋ยวรู้ 😉")

    # ---------- STEP 2 ----------
    if st.button("ต่อไป"):
        st.markdown("<div class='center'>จริงๆแล้ว...</div>", unsafe_allow_html=True)
        time.sleep(1)

        # ---------- TYPING ----------
        msg = "เราตั้งใจทำสิ่งนี้ให้เธอจริงๆนะ"
        placeholder = st.empty()
        typed = ""
        for c in msg:
            typed += c
            placeholder.markdown(f"<div class='big'>{typed}</div>", unsafe_allow_html=True)
            time.sleep(0.05)

        # ---------- NEXT ----------
        if st.button("ยังไม่หมดนะ กดต่อ"):
            st.write("คิดว่า 805 วันที่ผ่านมาเป็นยังไงบ้าง?")

            mood = st.selectbox(
                "เลือกความรู้สึก",
                ["ดีมาก", "งงๆ", "มีทั้งดีและไม่ดี", "อยากฆ่าเธอ (ล้อเล่น)"]
            )

            if mood:
                st.write("เราเองก็คิดเหมือนกัน")

            # ---------- FINAL ----------
            if st.button("โอเค มาถึงตรงนี้ละ"):
                st.balloons()
                st.markdown(f"<h2 class='center'>สุขสันต์วันเกิดนะ ❤️</h2>", unsafe_allow_html=True)
                st.write("ขอบคุณที่อยู่ด้วยกันมานะ")

                if st.button("กดสุดท้าย"):
                    st.success("อยู่กับเรานานๆนะ เราไม่ได้อยากเสียเธอไปเลยจริงๆ")

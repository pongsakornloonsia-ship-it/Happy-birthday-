import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="For You ❤️", page_icon="💖", layout="centered")

# -------------------- DATA --------------------
start_date = date(2024, 2, 14)
today = date.today()
days_together = (today - start_date).days
weeks_together = days_together // 7
months_together = days_together // 30

memories = [
    "วันที่คุยกันแล้วรู้สึกว่า เธอไม่เหมือนใคร",
    "วันที่งอนกัน แต่สุดท้ายก็ยังกลับมาคุยกัน",
    "วันที่รู้สึกว่าอยู่ด้วยกันแล้วสบายใจ",
    "วันที่อยากเก็บไว้เป็นความทรงจำดี ๆ",
    "วันที่ธรรมดา แต่พอมีเธอแล้วมันพิเศษ",
]

small_love_notes = [
    "เธอเป็นคนที่ทำให้วันธรรมดาดูดีขึ้น",
    "ไม่ต้องหวานเยอะ แค่มีเธอก็พอแล้ว",
    "เราไม่ได้ชอบอะไรเวอร์ ๆ แต่ชอบเธอมากจริง ๆ",
    "อยู่ด้วยกันแบบนี้ไปเรื่อย ๆ ก็ดีแล้ว",
]

# -------------------- STATE --------------------
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "picked_memory" not in st.session_state:
    st.session_state.picked_memory = random.choice(memories)

# -------------------- CSS --------------------
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 112, 159, 0.18), transparent 28%),
            radial-gradient(circle at top right, rgba(126, 87, 194, 0.16), transparent 25%),
            linear-gradient(135deg, #24172f 0%, #352243 45%, #4a2f52 100%);
        color: #f7f1f8;
    }

    .block-container {
        max-width: 920px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    .hero {
        padding: 28px 22px;
        border-radius: 28px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 16px 40px rgba(0,0,0,0.24);
        text-align: center;
        backdrop-filter: blur(10px);
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        color: rgba(255,255,255,0.82);
        font-size: 0.92rem;
        margin-bottom: 14px;
    }

    .title {
        font-size: clamp(2rem, 4.5vw, 3.6rem);
        font-weight: 900;
        margin: 0;
        color: #fff;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 680px;
        color: rgba(255,255,255,0.78);
        line-height: 1.7;
        font-size: 1rem;
    }

    .stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-top: 18px;
    }

    .stat {
        border-radius: 20px;
        padding: 16px 14px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.10);
    }

    .num {
        font-size: 2rem;
        font-weight: 900;
        color: #fff;
        line-height: 1;
    }

    .label {
        margin-top: 6px;
        color: rgba(255,255,255,0.72);
        font-size: 0.92rem;
    }

    .box {
        margin-top: 16px;
        padding: 18px 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.10);
        box-shadow: 0 14px 32px rgba(0,0,0,0.18);
    }

    .box h2 {
        margin: 0 0 10px 0;
        font-size: 1.35rem;
        color: #fff;
    }

    .box p {
        margin: 0;
        color: rgba(255,255,255,0.78);
        line-height: 1.7;
    }

    .card {
        padding: 16px 16px;
        border-radius: 18px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.10);
        margin-top: 12px;
    }

    .card-title {
        color: #fff;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .chip-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 12px;
    }

    .chip {
        padding: 8px 12px;
        border-radius: 999px;
        background: linear-gradient(135deg, rgba(255, 105, 135, 0.18), rgba(157, 93, 228, 0.18));
        border: 1px solid rgba(255,255,255,0.10);
        color: #fff;
        font-size: 0.92rem;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 0;
        padding: 0.8rem 1rem;
        background: linear-gradient(135deg, #ff5f8f, #8c5bff);
        color: white;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(0,0,0,0.22);
    }

    .small-note {
        color: rgba(255,255,255,0.7);
        font-size: 0.94rem;
        line-height: 1.6;
    }
</style>
""", unsafe_allow_html=True)

# -------------------- HERO --------------------
st.markdown("""
<div class="hero">
    <div class="badge">Birthday Gift • สำหรับเธอ</div>
    <div class="title">ของขวัญวันเกิดของเธอ 💖</div>
    <div class="subtitle">
        เว็บนี้ทำมาให้ดูนุ่มขึ้น สีไม่มืดเกิน อ่านไม่เยอะเกิน
        และมีลูกเล่นพอให้กดเล่นได้ ไม่จบไว
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- STATS --------------------
st.markdown(f"""
<div class="stats">
    <div class="stat">
        <div class="num">{days_together}</div>
        <div class="label">วันที่เริ่มคบ</div>
    </div>
    <div class="stat">
        <div class="num">{weeks_together}</div>
        <div class="label">สัปดาห์โดยประมาณ</div>
    </div>
    <div class="stat">
        <div class="num">{months_together}</div>
        <div class="label">เดือนโดยประมาณ</div>
    </div>
</div>
""", unsafe_allow_html=True)

# -------------------- FEATURE 1: TABS --------------------
tab1, tab2, tab3, tab4 = st.tabs(["เรื่องสั้น", "ความทรงจำ", "เล่นนิดนึง", "เซอร์ไพรส์"])

with tab1:
    st.markdown("""
    <div class="box">
        <h2>เรื่องสั้น ๆ</h2>
        <p>
            ตั้งแต่วันที่ 14/02/2024 จนถึงวันนี้ มันไม่ใช่แค่เวลาที่ผ่านไป
            แต่มันคือช่วงที่มีความหมายจริง ๆ สำหรับเรา
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">สิ่งที่อยากบอกเธอ</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="small-note">
        เราไม่ได้อยากเขียนเยอะ แค่อยากให้เธอรู้ว่า...
        เธอสำคัญกับเรามากกว่าที่พูดบ่อย ๆ นั่นแหละ
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="box">
        <h2>ความทรงจำ</h2>
        <p>กดปุ่มเพื่อสุ่มความทรงจำสั้น ๆ หนึ่งอัน</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("สุ่มความทรงจำ"):
        st.session_state.picked_memory = random.choice(memories)

    st.markdown(f"""
    <div class="card">
        <div class="card-title">ตอนนี้ที่สุ่มได้</div>
        <div class="small-note">{st.session_state.picked_memory}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="chip-row">', unsafe_allow_html=True)
    for note in small_love_notes:
        st.markdown(f'<span class="chip">{note}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="box">
        <h2>เล่นนิดนึง</h2>
        <p>เลื่อนความคิดถึง แล้วให้เว็บตอบกลับแบบสั้น ๆ</p>
    </div>
    """, unsafe_allow_html=True)

    mood = st.slider("ระดับความคิดถึง", 0, 100, 62)
    st.progress(mood / 100)

    if mood < 35:
        reply = "ยังนิ่ง ๆ อยู่ แต่ก็คิดถึงนะ"
    elif mood < 75:
        reply = "เริ่มอินแล้ว เธอเข้ามาในหัวละ"
    else:
        reply = "โอเค ตอนนี้คิดถึงเธอจริงจังเลย"

    st.markdown(f"""
    <div class="card">
        <div class="card-title">ผลลัพธ์</div>
        <div class="small-note">{reply}</div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="box">
        <h2>เซอร์ไพรส์</h2>
        <p>มีข้อความลับให้เธอเปิดเอง จะได้ไม่รู้สึกว่าเว็บมันจบง่ายเกินไป</p>
    </div>
    """, unsafe_allow_html=True)

    st.checkbox("เปิดข้อความลับ", key="secret_toggle")
    st.session_state.secret_open = st.session_state.get("secret_toggle", False)

    if st.session_state.secret_open:
        st.markdown("""
        <div class="card">
            <div class="card-title">ข้อความลับ</div>
            <div class="small-note">
                ครีมอาจไม่ค่อยชอบให้เรียกชื่อเล่น แต่สำหรับเรา
                เธอคือคนที่ทำให้วันธรรมดาดูดีขึ้นจริง ๆ
                ของขวัญนี้เลยอยากให้มันดูอบอุ่น พอดี ๆ และไม่รีบจบ
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("กดรับของขวัญ 🎁"):
        st.balloons()
        st.success("สุขสันต์วันเกิดนะ เธอ 💖 ขอให้ปีนี้เป็นปีที่ดีมาก ๆ")

# -------------------- FOOTER MESSAGE --------------------
st.markdown("""
<div class="box">
    <h2>ท้ายสุด</h2>
    <p>
        เราตั้งใจทำให้เว็บนี้ดูไม่มืดเกิน ไม่โล่งเกิน และไม่อ่านเยอะเกินไป
        ถ้าอยากให้มันตรงกว่านี้อีก ก็แค่เปลี่ยนข้อความบางประโยคให้เป็นเรื่องของเธอสองคนจริง ๆ
    </p>
</div>
""", unsafe_allow_html=True)

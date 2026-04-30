import streamlit as st
from datetime import date
import random

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

today = date.today()
birthday_this_year = date(today.year, 6, 26)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, 6, 26)
days_to_birthday = (next_birthday - today).days

start_date = date(2024, 2, 14)
days_together = (today - start_date).days

wishes = [
    "สุขสันต์วันเกิดนะเธอ 💖",
    "ขอให้วันนี้มีแต่เรื่องดี ๆ",
    "ขอให้เธอยิ้มเยอะ ๆ เลย",
    "วันนี้เป็นวันของเธอจริง ๆ",
    "ขอให้ปีนี้ใจดีกับเธอมาก ๆ",
    "ของขวัญชิ้นนี้ตั้งใจทำให้เธอ",
]

memories = [
    "วันที่คุยกันแล้วไม่อยากหยุด",
    "วันที่งอนกันแล้วก็ยังกลับมาคุย",
    "วันที่ธรรมดา แต่จำได้ชัด",
    "วันที่อยู่ด้วยกันแล้วสบายใจ",
    "วันที่รู้สึกว่าเธอสำคัญขึ้นเรื่อย ๆ",
]

tiny_lines = [
    "เธอทำให้วันธรรมดาดีขึ้น",
    "ไม่ต้องเยอะ แต่ขอให้เป็นเธอ",
    "บางทีแค่มีเธอก็พอแล้ว",
    "วันนี้อยากให้เธอยิ้มเยอะ ๆ",
    "เว็บนี้ทำมาเพื่อเธอจริง ๆ",
]

if "wish_index" not in st.session_state:
    st.session_state.wish_index = 0
if "memory_index" not in st.session_state:
    st.session_state.memory_index = 0
if "candles" not in st.session_state:
    st.session_state.candles = 6
if "spark" not in st.session_state:
    st.session_state.spark = 0
if "gift_open" not in st.session_state:
    st.session_state.gift_open = False
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "mood" not in st.session_state:
    st.session_state.mood = 72

st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(255, 187, 214, 0.55), transparent 24%),
            radial-gradient(circle at 90% 18%, rgba(181, 163, 255, 0.40), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(255, 222, 170, 0.30), transparent 28%),
            linear-gradient(135deg, #fcecf3 0%, #f4edff 48%, #fff4de 100%);
        background-attachment: fixed;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    .floatwrap {
        position: fixed;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .heart {
        position: absolute;
        bottom: -40px;
        opacity: 0.22;
        animation: floatup linear infinite;
        user-select: none;
    }

    .spark {
        position: absolute;
        border-radius: 999px;
        opacity: 0.28;
        animation: drift ease-in-out infinite;
    }

    @keyframes floatup {
        0% { transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }
        12% { opacity: 0.28; }
        100% { transform: translateY(-115vh) scale(1.2) rotate(20deg); opacity: 0; }
    }

    @keyframes drift {
        0%, 100% { transform: translateY(0) translateX(0); }
        50% { transform: translateY(-12px) translateX(14px); }
    }

    .hero {
        position: relative;
        z-index: 2;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(125, 87, 140, 0.10);
        border-radius: 30px;
        padding: 28px 24px;
        text-align: center;
        box-shadow: 0 18px 40px rgba(105, 71, 102, 0.10);
        backdrop-filter: blur(10px);
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.85);
        border: 1px solid rgba(125, 87, 140, 0.10);
        color: #8a5e8f;
        font-weight: 800;
        margin-bottom: 12px;
        font-size: 0.92rem;
    }

    .title {
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 900;
        margin: 0;
        color: #5a3460;
        letter-spacing: -0.03em;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 840px;
        color: #725a72;
        line-height: 1.75;
        font-size: 1rem;
    }

    .topgrid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-top: 18px;
        position: relative;
        z-index: 2;
    }

    .stat {
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(125, 87, 140, 0.10);
        border-radius: 22px;
        padding: 16px 14px;
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        text-align: center;
    }

    .num {
        font-size: 2rem;
        font-weight: 900;
        color: #6a3f73;
        line-height: 1;
    }

    .label {
        margin-top: 6px;
        color: #7c687b;
        font-size: 0.92rem;
    }

    .panel {
        margin-top: 18px;
        padding: 18px;
        border-radius: 26px;
        background: rgba(255,255,255,0.70);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 26px rgba(105, 71, 102, 0.08);
        position: relative;
        z-index: 2;
        backdrop-filter: blur(8px);
    }

    .panel h2 {
        margin: 0 0 8px 0;
        color: #5a3460;
        font-size: 1.35rem;
    }

    .panel p {
        margin: 0;
        color: #725a72;
        line-height: 1.72;
    }

    .chips {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 12px;
    }

    .chip {
        padding: 8px 12px;
        border-radius: 999px;
        background: linear-gradient(135deg, rgba(255, 146, 184, 0.24), rgba(173, 142, 255, 0.24));
        border: 1px solid rgba(125, 87, 140, 0.10);
        color: #5f3966;
        font-weight: 700;
        font-size: 0.92rem;
    }

    .glass {
        padding: 16px;
        border-radius: 22px;
        background: rgba(255,255,255,0.80);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        height: 100%;
    }

    .gtitle {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .gbody {
        color: #725a72;
        line-height: 1.68;
        font-size: 0.96rem;
    }

    .story {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        margin-top: 12px;
    }

    .story .t {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .story .d {
        color: #725a72;
        line-height: 1.65;
        font-size: 0.95rem;
    }

    .final {
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.84);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 24px rgba(105, 71, 102, 0.08);
        text-align: center;
    }

    .final h3 {
        margin: 0 0 8px 0;
        color: #5a3460;
        font-size: 1.45rem;
    }

    .final p {
        color: #725a72;
        line-height: 1.7;
        margin: 0;
    }

    .bigtext {
        color: #5a3460;
        font-size: 1.1rem;
        line-height: 1.8;
        font-weight: 700;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7da8, #b07cff);
        color: white;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(94, 60, 97, 0.18);
        transition: transform 0.16s ease, box-shadow 0.16s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(94, 60, 97, 0.22);
    }

    @media (max-width: 1100px) {
        .topgrid { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 700px) {
        .topgrid { grid-template-columns: 1fr; }
        .hero { padding: 22px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

hearts = "".join(
    f'<span class="heart" style="left:{random.randint(0,100)}%; '
    f'font-size:{random.randint(16,32)}px; '
    f'animation-duration:{random.randint(8,14)}s; '
    f'animation-delay:{random.uniform(0,6):.2f}s;">❤</span>'
    for _ in range(18)
)
sparks = "".join(
    f'<span class="spark" style="left:{random.randint(0,100)}%; top:{random.randint(0,100)}%; '
    f'width:{random.randint(8,18)}px; height:{random.randint(8,18)}px; '
    f'background: rgba({random.randint(220,255)}, {random.randint(160,220)}, {random.randint(190,255)}, 0.35); '
    f'animation-duration:{random.randint(5,10)}s; '
    f'animation-delay:{random.uniform(0,4):.2f}s;"></span>'
    for _ in range(12)
)

st.markdown(f'<div class="floatwrap">{hearts}{sparks}</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="hero">
        <div class="badge">Birthday Gift for เธอ 🎂</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="subtitle">
            วันนี้ขอให้เป็นวันของเธอจริง ๆ เปิดมาแล้วกดเล่นได้ มีของให้สุ่ม มีของให้เปิด
            มีเค้ก มีประกาย และมีข้อความที่ตั้งใจเขียนให้มันรู้สึกเหมือนของขวัญจริง
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="topgrid">
        <div class="stat"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="stat"><div class="num">{days_together}</div><div class="label">วันที่เริ่มคบกัน</div></div>
        <div class="stat"><div class="num">1</div><div class="label">คนพิเศษ</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="panel">
        <h2>กดเล่นได้เลย</h2>
        <p>ไม่ต้องอ่านยาว แค่กดแล้วมันเปลี่ยนให้ดูน่าสนใจกว่าเดิม</p>
        <div class="chips">
            <span class="chip">🎁 เปิดของขวัญ</span>
            <span class="chip">🎂 เป่าเค้ก</span>
            <span class="chip">🫶 สุ่มคำอวยพร</span>
            <span class="chip">✨ เปิดประกาย</span>
            <span class="chip">💌 เปิดข้อความลับ</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("สุ่มคำอวยพร 🎀"):
        st.session_state.wish_index = random.randint(0, len(wishes) - 1)
        st.session_state.spark += 1
with c2:
    if st.button("จุดเทียน 🕯️"):
        st.session_state.candles = 6
        st.session_state.spark += 1
with c3:
    if st.button("เป่าเค้ก 🎉"):
        st.session_state.candles = 0
        st.session_state.gift_open = True
        st.balloons()

candles = "🕯️ " * st.session_state.candles if st.session_state.candles > 0 else "🎂 ✨ 🎂"

st.markdown(
    f"""
    <div class="panel">
        <h2>เค้กวันนี้</h2>
        <p style="margin-bottom:10px;">กดปุ่มข้างบนแล้วดูเค้กเปลี่ยน</p>
        <div class="bigtext" style="font-size:2rem; text-align:center;">{candles}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([1.1, 0.9])

with left:
    st.markdown(
        f"""
        <div class="glass">
            <div class="gtitle">คำอวยพรที่สุ่มได้</div>
            <div class="gbody">{wishes[st.session_state.wish_index]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("กดให้มีประกาย ✨"):
        st.session_state.gift_open = True
        st.snow()

    st.markdown(
        f"""
        <div class="story">
            <div class="t">กดไปแล้ว</div>
            <div class="d">{st.session_state.spark} ครั้ง</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="story">
            <div class="t">ข้อความที่อยากจำ</div>
            <div class="d">{tiny_lines[st.session_state.wish_index % len(tiny_lines)]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with right:
    if st.button("สุ่มความทรงจำ"):
        st.session_state.memory_index = random.randint(0, len(memories) - 1)

    st.markdown(
        f"""
        <div class="glass">
            <div class="gtitle">ความทรงจำสั้น ๆ</div>
            <div class="gbody">{memories[st.session_state.memory_index]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.session_state.mood = st.slider("ระดับความน่ารักของวันนี้", 0, 100, st.session_state.mood)
    st.progress(st.session_state.mood / 100)

    if st.session_state.mood < 30:
        mood_text = "ยังนุ่ม ๆ อยู่"
    elif st.session_state.mood < 70:
        mood_text = "เริ่มเข้าฟีลของวันเกิดแล้ว"
    else:
        mood_text = "ตอนนี้ดูเป็นวันพิเศษเต็ม ๆ"

    st.markdown(
        f"""
        <div class="story">
            <div class="t">ผลลัพธ์</div>
            <div class="d">{mood_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="panel">
        <h2>ของเล็ก ๆ อีกนิด</h2>
        <p>ไว้ให้หน้าดูไม่โล่งและไม่เงียบ</p>
    </div>
    """,
    unsafe_allow_html=True,
)

a, b, c, d = st.columns(4)
cards = [
    ("💗", "วันนี้", "เป็นของเธอ"),
    ("🎂", "เค้ก", "เปลี่ยนได้"),
    ("✨", "ประกาย", "กดได้"),
    ("🫶", "ฟีล", "เลือกได้"),
]
for col, (x, y, z) in zip([a, b, c, d], cards):
    with col:
        st.markdown(
            f"""
            <div class="glass" style="min-height:130px;">
                <div class="gtitle">{x} {y}</div>
                <div class="gbody">{z}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown(
    """
    <div class="panel">
        <h2>ข้อความลับ</h2>
        <p>เปิดเมื่อพร้อม</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.checkbox("เปิดข้อความลับ", key="secret_toggle")
if st.session_state.secret_toggle:
    st.markdown(
        f"""
        <div class="final">
            <h3>สุขสันต์วันเกิดนะเธอ 💖</h3>
            <p>
                ขอให้วันนี้เธอยิ้มได้เยอะ ๆ กินของอร่อยได้เต็มที่
                แล้วก็มีแต่เรื่องดี ๆ เข้ามาแบบไม่ต้องเหนื่อยหาเอง<br><br>
                ถ้าเรียกครีมบ้างก็เพราะน่ารัก แต่สุดท้ายก็ยังอยากเรียกเธออยู่ดี
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

note = st.text_area(
    "ข้อความถึงเธอ",
    value="สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ และมีแต่เรื่องที่ชอบ",
    height=110,
)

st.download_button(
    "ดาวน์โหลดข้อความนี้",
    data=note,
    file_name="birthday_message.txt",
    mime="text/plain",
    use_container_width=True,
)

if st.session_state.gift_open:
    st.markdown(
        """
        <div class="final">
            <h3>ของขวัญเปิดแล้ว 🎁</h3>
            <p>วันนี้เป็นวันของเธอจริง ๆ ขอให้เป็นวันดีที่จำได้ไปนาน ๆ</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

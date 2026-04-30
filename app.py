import streamlit as st
from datetime import date
import random

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- DATA ----------
start_date = date(2024, 2, 14)
today = date.today()
days_together = (today - start_date).days

birthday_month = 6
birthday_day = 26
birthday_this_year = date(today.year, birthday_month, birthday_day)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, birthday_month, birthday_day)
days_to_birthday = (next_birthday - today).days

quotes = [
    "สุขสันต์วันเกิดนะเธอ 💖",
    "วันนี้เป็นวันของเธอ",
    "ขอให้ปีนี้มีแต่เรื่องดี ๆ",
    "ของขวัญชิ้นนี้ตั้งใจทำให้เธอ",
    "เธอคือคนสำคัญของเราเสมอ",
]

mini_notes = [
    "อยู่ด้วยแล้วสบายใจ",
    "แค่คุยกันก็ดีแล้ว",
    "วันธรรมดาก็พิเศษได้",
    "ไม่ต้องเยอะ แต่ต้องจริงใจ",
    "เธอคือคนพิเศษของวันนี้",
]

if "page" not in st.session_state:
    st.session_state.page = 0
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0
if "note_index" not in st.session_state:
    st.session_state.note_index = 0
if "spark_count" not in st.session_state:
    st.session_state.spark_count = 0
if "gift_open" not in st.session_state:
    st.session_state.gift_open = False
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "mood" not in st.session_state:
    st.session_state.mood = 68

# ---------- CSS ----------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 15% 15%, rgba(255, 168, 198, 0.55), transparent 24%),
            radial-gradient(circle at 85% 20%, rgba(171, 145, 255, 0.38), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(255, 214, 142, 0.30), transparent 26%),
            linear-gradient(135deg, #fde8ef 0%, #f4e8ff 46%, #fff1dd 100%);
        background-attachment: fixed;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    .floating {
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
        animation: floatUp linear infinite;
        user-select: none;
        filter: blur(0.1px);
    }

    .sparkle {
        position: absolute;
        border-radius: 999px;
        opacity: 0.35;
        animation: drift linear infinite;
    }

    @keyframes floatUp {
        0% { transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }
        10% { opacity: 0.28; }
        100% { transform: translateY(-115vh) scale(1.2) rotate(18deg); opacity: 0; }
    }

    @keyframes drift {
        0% { transform: translateY(0) translateX(0); opacity: 0.15; }
        50% { transform: translateY(-18px) translateX(20px); opacity: 0.32; }
        100% { transform: translateY(0) translateX(0); opacity: 0.15; }
    }

    .hero {
        position: relative;
        z-index: 2;
        padding: 28px 22px;
        border-radius: 30px;
        background: rgba(255,255,255,0.68);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 18px 40px rgba(105, 71, 102, 0.11);
        backdrop-filter: blur(10px);
        text-align: center;
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.82);
        border: 1px solid rgba(125, 87, 140, 0.10);
        color: #8a5e8f;
        font-weight: 800;
        margin-bottom: 12px;
        font-size: 0.92rem;
    }

    .title {
        font-size: clamp(2.3rem, 5vw, 4.3rem);
        font-weight: 900;
        margin: 0;
        color: #5a3460;
        letter-spacing: -0.03em;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 820px;
        color: #6f5a73;
        line-height: 1.75;
        font-size: 1rem;
    }

    .rowbox {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-top: 18px;
    }

    .stat {
        background: rgba(255,255,255,0.72);
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
        background: rgba(255,255,255,0.63);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 26px rgba(105, 71, 102, 0.08);
        position: relative;
        z-index: 2;
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
        background: rgba(255,255,255,0.76);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        height: 100%;
    }

    .glass-title {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .glass-body {
        color: #725a72;
        line-height: 1.68;
        font-size: 0.96rem;
    }

    .grid2 {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-top: 12px;
    }

    .grid4 {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-top: 12px;
    }

    .mini {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.76);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
        animation: pulse 2.8s ease-in-out infinite;
    }

    @keyframes pulse {
        0%,100% { transform: translateY(0px); }
        50% { transform: translateY(-2px); }
    }

    .mini .k {
        color: #5a3460;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .mini .v {
        color: #725a72;
        font-size: 0.95rem;
        line-height: 1.65;
    }

    .story {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.74);
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
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(125, 87, 140, 0.10);
        box-shadow: 0 12px 24px rgba(105, 71, 102, 0.08);
        text-align: center;
    }

    .final h3 {
        margin: 0 0 8px 0;
        color: #5a3460;
        font-size: 1.5rem;
    }

    .final p {
        color: #725a72;
        line-height: 1.7;
        margin: 0;
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
        transition: transform 0.16s ease, box-shadow 0.16s ease, opacity 0.16s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(94, 60, 97, 0.22);
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.99);
    }

    .center {
        text-align: center;
    }

    @media (max-width: 1100px) {
        .grid4 { grid-template-columns: repeat(2, 1fr); }
        .rowbox { grid-template-columns: 1fr; }
    }

    @media (max-width: 700px) {
        .grid2, .grid4 { grid-template-columns: 1fr; }
        .hero { padding: 22px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- FLOATING EFFECTS ----------
hearts_html = "".join(
    f'<span class="heart" style="left:{random.randint(0,100)}%; '
    f'animation-duration:{random.randint(8,14)}s; '
    f'animation-delay:{random.uniform(0,6):.2f}s; '
    f'font-size:{random.randint(16,34)}px;">❤</span>'
    for _ in range(20)
)

sparkles_html = "".join(
    f'<span class="sparkle" style="left:{random.randint(0,100)}%; top:{random.randint(0,100)}%; '
    f'width:{random.randint(8,18)}px; height:{random.randint(8,18)}px; '
    f'background: rgba({random.randint(220,255)}, {random.randint(160,220)}, {random.randint(190,255)}, 0.35); '
    f'animation-duration:{random.randint(5,10)}s; '
    f'animation-delay:{random.uniform(0,4):.2f}s;"></span>'
    for _ in range(12)
)

st.markdown(
    f"""
    <div class="floating">
        {hearts_html}
        {sparkles_html}
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- HERO ----------
st.markdown(
    f"""
    <div class="hero">
        <div class="badge">Birthday Gift for เธอ 🎂</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="subtitle">
            วันนี้เป็นวันของเธอจริง ๆ เว็บนี้เลยทำให้ดูเป็นของขวัญ ไม่ใช่เว็บเปล่า ๆ
            มีเอฟเฟกต์ มีปุ่มกด มีสีพอดี ๆ และมีจุดให้เล่นหลายแบบ
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="rowbox">
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
        <h2>ลูกเล่นในเว็บนี้</h2>
        <p>มีหลายอย่างให้กดและเปลี่ยน ไม่ดูนิ่งหรือโล่งจนเกินไป</p>
        <div class="chips">
            <span class="chip">🎨 พื้นหลังไล่เฉด</span>
            <span class="chip">💫 หัวใจลอย</span>
            <span class="chip">✨ จุดประกาย</span>
            <span class="chip">🎁 ปุ่มเซอร์ไพรส์</span>
            <span class="chip">🫶 สุ่มข้อความ</span>
            <span class="chip">🎚️ สไลเดอร์ฟีล</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------- LAYOUT ----------
colA, colB = st.columns([1.2, 0.8])

with colA:
    st.markdown(
        """
        <div class="panel">
            <h2>ข้อความแรก</h2>
            <p>ไม่ได้อยากให้เว็บนี้ยาวจนเหนื่อย แค่อยากให้มันดูตั้งใจและมีอารมณ์ของของขวัญจริง ๆ</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("สุ่มข้อความวันเกิด"):
        st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)

    st.markdown(
        f"""
        <div class="final" style="margin-top:12px; text-align:left;">
            <h3>{quotes[st.session_state.quote_index]}</h3>
            <p>กดแล้วข้อความจะเปลี่ยนไปอีก</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("เพิ่มจังหวะของเว็บ"):
        st.session_state.spark_count += 1
        st.balloons()

    st.markdown(
        f"""
        <div class="story">
            <div class="t">จำนวนครั้งที่กด</div>
            <div class="d">{st.session_state.spark_count} ครั้ง</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with colB:
    st.markdown(
        """
        <div class="panel">
            <h2>ความทรงจำสั้น ๆ</h2>
            <p>กดเพื่อสลับข้อความให้ดูมีการเคลื่อนไหว</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("สุ่มความทรงจำ"):
        st.session_state.note_index = (st.session_state.note_index + 1) % len(mini_notes)

    st.markdown(
        f"""
        <div class="final" style="margin-top:12px; text-align:left;">
            <h3>{mini_notes[st.session_state.note_index]}</h3>
            <p>อันนี้สุ่มวนได้</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    mood = st.slider("ระดับความอบอุ่นของวัน", 0, 100, st.session_state.mood)
    st.session_state.mood = mood
    st.progress(mood / 100)

    if mood < 30:
        msg = "ยังนุ่ม ๆ อยู่"
    elif mood < 70:
        msg = "เริ่มเหมือนของขวัญแล้ว"
    else:
        msg = "ตอนนี้ดูเป็นวันพิเศษชัดเจน"

    st.markdown(
        f"""
        <div class="story">
            <div class="t">ผลลัพธ์</div>
            <div class="d">{msg}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- MORE SECTIONS ----------
st.markdown(
    """
    <div class="panel">
        <h2>4 ช่องสั้น ๆ</h2>
        <p>ช่วยให้หน้าดูแน่นขึ้นโดยไม่ต้องใส่ข้อความเยอะเกิน</p>
    </div>
    """,
    unsafe_allow_html=True,
)

g1, g2, g3, g4 = st.columns(4)
blocks = [
    ("✨", "วันนี้", "วันของเธอ"),
    ("🎁", "เว็บนี้", "ตั้งใจทำจริง"),
    ("💌", "ข้อความ", "สั้นแต่ตรง"),
    ("🫶", "ฟีล", "อบอุ่นพอดี"),
]
for col, (a, b, c) in zip([g1, g2, g3, g4], blocks):
    with col:
        st.markdown(
            f"""
            <div class="mini">
                <div class="k">{a} {b}</div>
                <div class="v">{c}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- INTERACTION ----------
st.markdown(
    """
    <div class="panel">
        <h2>เล่นสักหน่อย</h2>
        <p>มีปุ่มให้เปิดของขวัญและเปลี่ยนโหมดจบ</p>
    </div>
    """,
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    if st.button("เปิดของขวัญ 🎀"):
        st.session_state.gift_open = True
        st.snow()

with c2:
    if st.button("เปิดประกาย ✨"):
        st.session_state.gift_open = True
        st.balloons()

if st.session_state.gift_open:
    st.markdown(
        """
        <div class="final center">
            <h3>ของขวัญวันเกิดของเธอ</h3>
            <p>
                ขอให้วันนี้มีแต่เรื่องดี ๆ และหวังว่าเว็บนี้จะทำให้เธอรู้สึกว่า
                มันเป็นของขวัญที่ตั้งใจทำจริง ไม่ใช่หน้าเว็บธรรมดา
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- SECRET NOTE ----------
st.markdown(
    """
    <div class="panel">
        <h2>ข้อความลับ</h2>
        <p>กดเปิดเมื่อพร้อม</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.checkbox("เปิดข้อความลับ", key="secret_open")
if st.session_state.secret_open:
    st.markdown(
        """
        <div class="final">
            <h3>สุขสันต์วันเกิดนะเธอ 💖</h3>
            <p>
                ถึงจะเรียกครีมบ้าง แต่ส่วนใหญ่ก็ยังชอบเรียกเธออยู่ดี
                เว็บนี้ตั้งใจให้มีสี มีจังหวะ มีลูกเล่น และเป็นของขวัญที่ดูพิเศษจริง ๆ
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

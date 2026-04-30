import streamlit as st
from datetime import date
from html import escape
import random

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎁",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -------------------- DATE --------------------
today = date.today()
birthday_this_year = date(today.year, 6, 26)
next_birthday = birthday_this_year if today <= birthday_this_year else date(today.year + 1, 6, 26)
days_to_birthday = (next_birthday - today).days

# -------------------- DATA --------------------
wishes = [
    "สุขสันต์วันเกิดนะเธอ ขอให้วันนี้มีแต่คนใจดีกับเธอ",
    "ขอให้ปีนี้เบาขึ้นนิดนึง แล้วก็มีเรื่องดี ๆ โผล่มาแบบไม่ทันตั้งตัว",
    "ขอให้เธอได้ยิ้มเยอะ ๆ กินของอร่อย ๆ และไม่ต้องคิดเยอะ",
    "วันนี้เป็นวันของเธอ ลองใจดีกับตัวเองหน่อยก็ได้",
    "ขอให้ทุกอย่างที่เหนื่อยอยู่ ค่อย ๆ เบาลงทีละนิด",
    "ขอให้เธอเจอแต่วันสบายใจ แบบไม่ต้องฝืนอะไรเลย",
    "ไม่ต้องพยายามเป็นคนเพอร์เฟกต์ แค่เป็นเธอก็พอ",
    "ขอให้ปีนี้มีแต่เรื่องน่ารัก ๆ และเรื่องหนัก ๆ หายไปไกล ๆ",
    "สุขสันต์วันเกิดนะ ขอให้เธอมีความสุขแบบเต็ม ๆ",
    "ขอให้เธอยิ้มได้ง่ายกว่าที่ผ่านมา",
    "อยากให้วันนี้เป็นวันที่เธอรู้สึกว่าตัวเองสำคัญมาก",
    "ขอให้วันนี้ดีพอจนเธออยากจำไปอีกนาน",
]

tiny_notes = [
    "เธอทำให้วันธรรมดาดูดีขึ้น",
    "บางทีแค่มีเธออยู่ก็พอแล้ว",
    "ไม่ต้องเยอะ แต่ขอให้เป็นเรื่องของเธอ",
    "วันพิเศษแบบนี้ควรมีรอยยิ้มเยอะ ๆ",
    "ของขวัญชิ้นนี้ตั้งใจทำจริง ๆ",
]

memories = [
    "วันที่คุยกันแล้วรู้สึกว่าไม่อยากวางมือถือ",
    "วันที่งอนกันนิดหน่อย แต่สุดท้ายก็กลับมาคุยกัน",
    "วันที่ยิ้มเพราะอีกฝ่ายแบบไม่รู้ตัว",
    "วันที่ธรรมดามาก แต่กลับจำได้ชัด",
    "วันที่รู้สึกว่าเธอสำคัญขึ้นเรื่อย ๆ",
]

moods = [
    "อยากได้ฟีลน่ารัก ๆ",
    "อยากได้ฟีลอบอุ่น",
    "อยากได้ฟีลขี้เล่น",
    "อยากได้ฟีลเงียบ ๆ แต่กินใจ",
]

gift_types = [
    "ข้อความสั้น ๆ",
    "คำอวยพรยาวหน่อย",
    "ของขวัญแบบกดเล่นได้",
    "อะไรที่ดูตั้งใจมาก ๆ",
]

reasons = [
    "อยู่ด้วยแล้วสบายใจ",
    "คุยด้วยแล้วไม่อึดอัด",
    "เป็นตัวเองได้",
    "ทำให้วันธรรมดาไม่ธรรมดา",
    "เป็นเธอแบบนี้แหละ ดีแล้ว",
]

# -------------------- STATE --------------------
if "wish_index" not in st.session_state:
    st.session_state.wish_index = 0
if "note_index" not in st.session_state:
    st.session_state.note_index = 0
if "cake_candles" not in st.session_state:
    st.session_state.cake_candles = 5
if "gift_open" not in st.session_state:
    st.session_state.gift_open = False
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "spark_count" not in st.session_state:
    st.session_state.spark_count = 0
if "memory_index" not in st.session_state:
    st.session_state.memory_index = 0
if "mood_value" not in st.session_state:
    st.session_state.mood_value = 68

# -------------------- CSS --------------------
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 15% 15%, rgba(255, 160, 194, 0.45), transparent 24%),
            radial-gradient(circle at 85% 20%, rgba(178, 152, 255, 0.30), transparent 22%),
            radial-gradient(circle at 50% 95%, rgba(255, 216, 155, 0.24), transparent 28%),
            linear-gradient(135deg, #fde9f1 0%, #f5ecff 46%, #fff2de 100%);
        background-attachment: fixed;
    }

    .block-container {
        max-width: 1240px;
        padding-top: 1rem;
        padding-bottom: 2.5rem;
    }

    .float-wrap {
        position: fixed;
        inset: 0;
        pointer-events: none;
        overflow: hidden;
        z-index: 0;
    }

    .heart, .spark {
        position: absolute;
        user-select: none;
        pointer-events: none;
        opacity: 0.22;
    }

    .heart {
        bottom: -40px;
        animation: floatUp linear infinite;
    }

    .spark {
        border-radius: 999px;
        animation: drift ease-in-out infinite;
        opacity: 0.34;
    }

    @keyframes floatUp {
        0% { transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }
        12% { opacity: 0.28; }
        100% { transform: translateY(-115vh) scale(1.2) rotate(20deg); opacity: 0; }
    }

    @keyframes drift {
        0%, 100% { transform: translateY(0) translateX(0); }
        50% { transform: translateY(-14px) translateX(12px); }
    }

    .hero {
        position: relative;
        z-index: 2;
        padding: 30px 24px;
        border-radius: 32px;
        background: rgba(255,255,255,0.72);
        border: 1px solid rgba(130, 84, 144, 0.10);
        box-shadow: 0 18px 40px rgba(106, 72, 104, 0.10);
        text-align: center;
        margin-bottom: 18px;
        backdrop-filter: blur(10px);
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.86);
        border: 1px solid rgba(130, 84, 144, 0.10);
        color: #8b5e91;
        font-weight: 800;
        margin-bottom: 12px;
        font-size: 0.92rem;
    }

    .title {
        font-size: clamp(2.2rem, 5vw, 4.3rem);
        font-weight: 900;
        margin: 0;
        color: #5b3563;
        letter-spacing: -0.03em;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 840px;
        color: #725a72;
        line-height: 1.78;
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
        background: rgba(255,255,255,0.74);
        border: 1px solid rgba(130, 84, 144, 0.10);
        border-radius: 22px;
        padding: 16px 14px;
        box-shadow: 0 10px 22px rgba(106, 72, 104, 0.08);
        text-align: center;
    }

    .num {
        font-size: 2rem;
        font-weight: 900;
        color: #6c4074;
        line-height: 1;
    }

    .label {
        margin-top: 6px;
        color: #7b687b;
        font-size: 0.92rem;
    }

    .panel {
        margin-top: 18px;
        padding: 18px;
        border-radius: 26px;
        background: rgba(255,255,255,0.66);
        border: 1px solid rgba(130, 84, 144, 0.10);
        box-shadow: 0 12px 26px rgba(106, 72, 104, 0.08);
        position: relative;
        z-index: 2;
        backdrop-filter: blur(8px);
    }

    .panel h2 {
        margin: 0 0 8px 0;
        color: #5b3563;
        font-size: 1.35rem;
    }

    .panel p {
        margin: 0;
        color: #735b73;
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
        border: 1px solid rgba(130, 84, 144, 0.10);
        color: #5f3966;
        font-weight: 700;
        font-size: 0.92rem;
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

    .glass {
        padding: 16px;
        border-radius: 22px;
        background: rgba(255,255,255,0.78);
        border: 1px solid rgba(130, 84, 144, 0.10);
        box-shadow: 0 10px 22px rgba(106, 72, 104, 0.08);
        height: 100%;
    }

    .gtitle {
        color: #5b3563;
        font-weight: 900;
        margin-bottom: 8px;
    }

    .gbody {
        color: #735b73;
        line-height: 1.68;
        font-size: 0.96rem;
    }

    .story {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.76);
        border: 1px solid rgba(130, 84, 144, 0.10);
        box-shadow: 0 10px 22px rgba(106, 72, 104, 0.08);
        margin-top: 12px;
    }

    .story .t {
        color: #5b3563;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .story .d {
        color: #735b73;
        line-height: 1.65;
        font-size: 0.95rem;
    }

    .final {
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.80);
        border: 1px solid rgba(130, 84, 144, 0.10);
        box-shadow: 0 12px 24px rgba(106, 72, 104, 0.08);
        text-align: center;
    }

    .final h3 {
        margin: 0 0 8px 0;
        color: #5b3563;
        font-size: 1.45rem;
    }

    .final p {
        color: #735b73;
        line-height: 1.7;
        margin: 0;
    }

    .bigtext {
        color: #5b3563;
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
        .topgrid, .grid4 { grid-template-columns: repeat(2, 1fr); }
    }

    @media (max-width: 700px) {
        .topgrid, .grid2, .grid4 { grid-template-columns: 1fr; }
        .hero { padding: 22px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- FLOATING EFFECTS --------------------
hearts_html = "".join(
    f'<span class="heart" style="left:{random.randint(0,100)}%; '
    f'font-size:{random.randint(16,32)}px; '
    f'animation-duration:{random.randint(8,14)}s; '
    f'animation-delay:{random.uniform(0,6):.2f}s;">❤</span>'
    for _ in range(18)
)

sparkles_html = "".join(
    f'<span class="spark" style="left:{random.randint(0,100)}%; top:{random.randint(0,100)}%; '
    f'width:{random.randint(8,18)}px; height:{random.randint(8,18)}px; '
    f'background: rgba({random.randint(220,255)}, {random.randint(160,220)}, {random.randint(190,255)}, 0.35); '
    f'animation-duration:{random.randint(5,10)}s; '
    f'animation-delay:{random.uniform(0,4):.2f}s;"></span>'
    for _ in range(12)
)

st.markdown(
    f"""
    <div class="float-wrap">
        {hearts_html}
        {sparkles_html}
    </div>
    """,
    unsafe_allow_html=True,
)

def wrap_card(title, body):
    return f"""
    <div class="glass">
        <div class="gtitle">{title}</div>
        <div class="gbody">{body}</div>
    </div>
    """

# -------------------- HERO --------------------
st.markdown(
    """
    <div class="hero">
        <div class="badge">Birthday Gift for เธอ 🎂</div>
        <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
        <div class="subtitle">
            วันนี้ไม่ต้องคิดอะไรเยอะ ขอให้มันเป็นวันของเธอจริง ๆ
            เปิดมาแล้วกดเล่นได้ มีอะไรให้ยิ้ม มีอะไรให้เซอร์ไพรส์
            และไม่ใช่หน้าเว็บโล่ง ๆ ที่ดูแล้วจบในสิบวิ
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- TOP STAT --------------------
st.markdown(
    f"""
    <div class="topgrid">
        <div class="stat"><div class="num">{days_to_birthday}</div><div class="label">วันถึงวันเกิดถัดไป</div></div>
        <div class="stat"><div class="num">1</div><div class="label">วันพิเศษของเธอ</div></div>
        <div class="stat"><div class="num">∞</div><div class="label">ความตั้งใจ</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- FEATURE CHIPS --------------------
st.markdown(
    """
    <div class="panel">
        <h2>ของที่ใส่มาให้เว็บไม่เงียบ</h2>
        <p>เปิดแล้วมีอะไรให้เล่น ไม่ใช่แค่ดูแล้วผ่านไป</p>
        <div class="chips">
            <span class="chip">🎨 สีละมุน</span>
            <span class="chip">💫 หัวใจลอย</span>
            <span class="chip">✨ ประกายวิบวับ</span>
            <span class="chip">🎁 เปิดของขวัญ</span>
            <span class="chip">🫶 สุ่มคำอวยพร</span>
            <span class="chip">🎂 เป่าเค้ก</span>
            <span class="chip">🎚️ สไลเดอร์ฟีล</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- ACTIONS --------------------
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("สุ่มคำอวยพร 🎀"):
        st.session_state.wish_index = random.randint(0, len(wishes) - 1)
        st.session_state.spark_count += 1

with c2:
    if st.button("จุดเทียน 🕯️"):
        st.session_state.cake_candles = 5
        st.session_state.spark_count += 1

with c3:
    if st.button("เป่าเค้ก 🎉"):
        st.session_state.cake_candles = 0
        st.session_state.gift_open = True
        st.balloons()

candles = "🕯️ " * st.session_state.cake_candles if st.session_state.cake_candles > 0 else "✨ 🎂 ✨"

st.markdown(
    f"""
    <div class="panel center">
        <h2>เค้กของวันนี้</h2>
        <p style="margin-bottom:10px;">แตะปุ่มด้านบนแล้วดูว่าเทียนจะเปลี่ยนยังไง</p>
        <div class="bigtext" style="font-size:2rem;">{candles}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- MAIN GRID --------------------
left, right = st.columns([1.1, 0.9])

with left:
    st.markdown(wrap_card("คำอวยพรที่สุ่มได้", wishes[st.session_state.wish_index]), unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="story">
            <div class="t">ปุ่มที่กดไปแล้ว</div>
            <div class="d">{st.session_state.spark_count} ครั้ง</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if st.button("กดให้มีประกาย ✨"):
        st.session_state.gift_open = True
        st.snow()

    if st.session_state.gift_open:
        st.markdown(
            """
            <div class="final">
                <h3>เปิดของขวัญแล้ว</h3>
                <p>วันนี้เป็นวันของเธอจริง ๆ ขอให้มันดีแบบที่จำได้ไปอีกนาน</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

with right:
    nickname = st.text_input("ถ้าอยากใส่ชื่อเล่น", value="ครีม")
    nickname = escape(nickname.strip() or "ครีม")

    vibe = st.selectbox("วันนี้อยากได้ฟีลแบบไหน", moods)
    gift = st.selectbox("ของขวัญที่เข้ากับวันนี้", gift_types)

    st.markdown(
        f"""
        <div class="story">
            <div class="t">ฟีลที่เลือก</div>
            <div class="d">{vibe}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="story">
            <div class="t">ของขวัญแบบที่เหมาะ</div>
            <div class="d">{gift}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- 4 SMALL CARDS --------------------
st.markdown(
    """
    <div class="panel">
        <h2>อะไรอีกนิดที่ทำให้เว็บดูมีชีวิต</h2>
        <p>ไม่ต้องเยอะ แต่อยากให้มันกดแล้วรู้สึกว่าเว็บไม่แบน</p>
    </div>
    """,
    unsafe_allow_html=True,
)

g1, g2, g3, g4 = st.columns(4)
blocks = [
    ("💗", "วันนี้", "เป็นวันของเธอ"),
    ("🎂", "เค้ก", "เปลี่ยนเทียนได้"),
    ("🫶", "ความรู้สึก", "สุ่มได้เรื่อย ๆ"),
    ("✨", "จังหวะ", "มีประกายให้กด"),
]
for col, (a, b, c) in zip([g1, g2, g3, g4], blocks):
    with col:
        st.markdown(
            f"""
            <div class="glass" style="min-height:128px;">
                <div class="gtitle">{a} {b}</div>
                <div class="gbody">{c}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# -------------------- MEMORIES --------------------
st.markdown(
    """
    <div class="panel">
        <h2>ความทรงจำสั้น ๆ</h2>
        <p>กดสุ่มแล้วมันจะเปลี่ยนเป็นประโยคใหม่</p>
    </div>
    """,
    unsafe_allow_html=True,
)

m1, m2 = st.columns([1, 1])
with m1:
    if st.button("สุ่มความทรงจำ"):
        st.session_state.memory_index = random.randint(0, len(memories) - 1)

with m2:
    st.markdown(
        f"""
        <div class="final" style="text-align:left;">
            <h3>{memories[st.session_state.memory_index]}</h3>
            <p>{tiny_notes[st.session_state.memory_index % len(tiny_notes)]}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- MOOD GAME --------------------
st.markdown(
    """
    <div class="panel">
        <h2>เล่นอีกนิด</h2>
        <p>ตรงนี้เอาไว้เช็กว่าเว็บวันนี้ควรน่ารักแค่ไหน</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.session_state.mood_value = st.slider("ระดับความน่ารักของวันนี้", 0, 100, st.session_state.mood_value)
st.progress(st.session_state.mood_value / 100)

if st.session_state.mood_value < 30:
    mood_reply = "ยังนุ่มอยู่ แต่เริ่มมีฟีลแล้ว"
elif st.session_state.mood_value < 70:
    mood_reply = "เริ่มพอดี กำลังน่ารักเลย"
else:
    mood_reply = "โอเค ตอนนี้เป็นวันพิเศษแบบชัดเจน"

st.markdown(
    f"""
    <div class="story">
        <div class="t">ผลลัพธ์</div>
        <div class="d">{mood_reply}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- SECRET MESSAGE --------------------
st.markdown(
    """
    <div class="panel">
        <h2>ข้อความเก็บไว้</h2>
        <p>เปิดเมื่อพร้อม</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.checkbox("เปิดข้อความเก็บไว้", key="secret_toggle")
if st.session_state.secret_toggle:
    st.markdown(
        f"""
        <div class="final">
            <h3>สุขสันต์วันเกิดนะ {nickname} 💖</h3>
            <p>
                ขอให้วันนี้มีแต่เรื่องดี ๆ แบบที่ไม่ต้องพยายามหาเอง<br>
                ขอให้ยิ้มได้เยอะ ๆ กินของอร่อยได้เต็มที่<br>
                และขอให้ปีนี้ใจดีกับเธอมากกว่าที่ผ่านมา
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

msg = st.text_area(
    "ข้อความถึงเธอ",
    value="สุขสันต์วันเกิดนะเธอ ขอให้วันนี้เป็นวันที่ดีมาก ๆ แล้วก็มีแต่เรื่องที่ชอบ",
    height=110,
)

st.download_button(
    "ดาวน์โหลดข้อความนี้",
    data=msg,
    file_name="birthday_message.txt",
    mime="text/plain",
    use_container_width=True,
)

# -------------------- REASONS --------------------
st.markdown(
    """
    <div class="panel">
        <h2>เหตุผลสั้น ๆ ที่อยากบอก</h2>
        <p>ไม่ต้องยาว แค่ให้รู้ว่าเธอสำคัญ</p>
        <div class="grid2">
    """,
    unsafe_allow_html=True,
)

for r in reasons:
    st.markdown(
        f"""
        <div class="story">
            <div class="t">• {r}</div>
            <div class="d">แค่นี้ก็พอแล้วสำหรับความรู้สึกดี ๆ</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div></div>", unsafe_allow_html=True)

# -------------------- FINAL --------------------
st.markdown(
    """
    <div class="final">
        <h3>สุขสันต์วันเกิดนะเธอ 🎂</h3>
        <p>
            ขอให้วันนี้ดีแบบที่เธอไม่ต้องฝืนยิ้ม<br>
            ขอให้มีความสุขเยอะ ๆ แล้วก็จำได้ว่าตัวเองมีค่ามากแค่ไหน
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

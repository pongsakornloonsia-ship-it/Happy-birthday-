import streamlit as st
from datetime import date, datetime
import random

st.set_page_config(
    page_title="Happy Birthday 🎂",
    page_icon="🎂",
    layout="wide"
)

# ---------- DATE ----------
birthday_month = 6
birthday_day = 26
today = date.today()
this_year_birthday = date(today.year, birthday_month, birthday_day)
next_birthday = this_year_birthday if today <= this_year_birthday else date(today.year + 1, birthday_month, birthday_day)
days_to_birthday = (next_birthday - today).days

start_date = date(2024, 2, 14)
days_together = (today - start_date).days

# ---------- STATE ----------
if "gift_open" not in st.session_state:
    st.session_state.gift_open = False
if "note_open" not in st.session_state:
    st.session_state.note_open = False
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0
if "memory_index" not in st.session_state:
    st.session_state.memory_index = 0
if "clicks" not in st.session_state:
    st.session_state.clicks = 0

quotes = [
    "สุขสันต์วันเกิดนะเธอ 🎂",
    "ขอให้ปีนี้เป็นปีที่ดีมาก ๆ",
    "ตั้งใจทำเว็บนี้ให้เป็นของขวัญจริง ๆ",
    "เธอเป็นคนสำคัญของเราเสมอ",
    "วันนี้ต้องเป็นวันของเธอเท่านั้น",
]

memories = [
    "วันที่เริ่มคุยกันแล้วรู้สึกว่าใช่",
    "วันที่อยากทักหาเธอมากกว่าปกติ",
    "วันที่ยิ้มเพราะเธอโดยไม่รู้ตัว",
    "วันที่ธรรมดา แต่จำได้ชัด",
    "วันที่อยากเก็บไว้เป็นของขวัญทางใจ",
]

# ---------- CSS ----------
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 148, 180, 0.32), transparent 25%),
        radial-gradient(circle at top right, rgba(162, 123, 255, 0.24), transparent 22%),
        radial-gradient(circle at bottom center, rgba(255, 205, 120, 0.18), transparent 28%),
        linear-gradient(135deg, #f7dce8 0%, #f4eaff 45%, #fff0db 100%);
}

.block-container {
    max-width: 1180px;
    padding-top: 1rem;
    padding-bottom: 2.5rem;
}

.hero {
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(120, 80, 130, 0.10);
    border-radius: 30px;
    padding: 30px 24px;
    box-shadow: 0 16px 36px rgba(105, 71, 102, 0.12);
    text-align: center;
    margin-bottom: 18px;
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    background: rgba(255,255,255,0.86);
    color: #8b5c8f;
    border: 1px solid rgba(120, 80, 130, 0.10);
    font-weight: 700;
    margin-bottom: 12px;
}

.title {
    font-size: clamp(2.2rem, 5vw, 4.2rem);
    font-weight: 900;
    color: #5a3460;
    margin: 0;
}

.subtitle {
    color: #755a75;
    line-height: 1.75;
    margin: 12px auto 0 auto;
    max-width: 800px;
    font-size: 1rem;
}

.stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
    margin-top: 18px;
}

.stat {
    background: rgba(255,255,255,0.72);
    border: 1px solid rgba(120, 80, 130, 0.10);
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
    color: #7c687a;
    font-size: 0.92rem;
}

.section {
    margin-top: 18px;
    padding: 18px;
    border-radius: 26px;
    background: rgba(255,255,255,0.62);
    border: 1px solid rgba(120, 80, 130, 0.10);
    box-shadow: 0 12px 26px rgba(105, 71, 102, 0.08);
}

.section h2 {
    margin: 0 0 8px 0;
    color: #5a3460;
    font-size: 1.35rem;
}

.section p {
    margin: 0;
    color: #725a72;
    line-height: 1.72;
}

.card {
    padding: 16px;
    border-radius: 22px;
    background: rgba(255,255,255,0.74);
    border: 1px solid rgba(120, 80, 130, 0.10);
    box-shadow: 0 10px 22px rgba(105, 71, 102, 0.08);
    height: 100%;
}

.card-title {
    color: #5a3460;
    font-weight: 900;
    margin-bottom: 8px;
}

.card-body {
    color: #725a72;
    line-height: 1.68;
    font-size: 0.96rem;
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
    border: 1px solid rgba(120, 80, 130, 0.10);
    color: #5f3966;
    font-weight: 700;
    font-size: 0.92rem;
}

.story {
    padding: 14px;
    border-radius: 20px;
    background: rgba(255,255,255,0.74);
    border: 1px solid rgba(120, 80, 130, 0.10);
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

div.stButton > button {
    width: 100%;
    border-radius: 999px;
    border: 0;
    padding: 0.82rem 1rem;
    background: linear-gradient(135deg, #ff7da8, #b07cff);
    color: white;
    font-weight: 800;
    box-shadow: 0 10px 24px rgba(94, 60, 97, 0.18);
}

textarea, input, select {
    border-radius: 16px !important;
}

.final {
    padding: 18px;
    border-radius: 24px;
    background: rgba(255,255,255,0.76);
    border: 1px solid rgba(120, 80, 130, 0.10);
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

@media (max-width: 900px) {
    .stats { grid-template-columns: 1fr; }
}
</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown(f"""
<div class="hero">
    <div class="badge">Birthday Gift for เธอ 🎂</div>
    <div class="title">สุขสันต์วันเกิดนะเธอ 💖</div>
    <div class="subtitle">
        เว็บนี้ตั้งใจทำให้ดูเป็นของขวัญวันเกิดชัด ๆ สีพอดี ๆ ไม่มืดเกิน ไม่โล่งเกิน
        และมีลูกเล่นให้กดเล่นหลายจุด
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- STATS ----------
st.markdown(f"""
<div class="stats">
    <div class="stat">
        <div class="num">{days_to_birthday}</div>
        <div class="label">วันถึงวันเกิดถัดไป</div>
    </div>
    <div class="stat">
        <div class="num">{days_together}</div>
        <div class="label">วันที่เริ่มคบกัน</div>
    </div>
    <div class="stat">
        <div class="num">1</div>
        <div class="label">คนพิเศษที่สุด</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- CHIPS ----------
st.markdown("""
<div class="section">
    <h2>ของที่ใส่มาในเว็บนี้</h2>
    <p>ทำให้มันดูมีอะไร แต่ไม่ยัดจนแน่น</p>
    <div class="chips">
        <span class="chip">🎨 พื้นหลังมีสี</span>
        <span class="chip">🎁 ฟีลของขวัญวันเกิด</span>
        <span class="chip">💌 ข้อความสุ่ม</span>
        <span class="chip">🫶 ปุ่มให้กดเล่น</span>
        <span class="chip">🎚️ เลื่อนระดับฟีล</span>
        <span class="chip">📖 อ่านง่ายขึ้น</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- TABS ----------
tab1, tab2, tab3, tab4 = st.tabs(["หน้าแรก", "ความทรงจำ", "เล่นนิดนึง", "ปิดท้าย"])

with tab1:
    c1, c2 = st.columns([1.2, 1])
    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-title">ข้อความแรก</div>
            <div class="card-body">
                วันนี้เป็นวันของเธอจริง ๆ
                เราเลยอยากทำเว็บที่ดูเป็นของขวัญมากกว่าดูเหมือนหน้าแอปธรรมดา
                และตั้งใจให้โทนมันสว่างพอดี ไม่มืดทึบ
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("สุ่มข้อความวันเกิด"):
            st.session_state.quote_index = random.randint(0, len(quotes) - 1)

        st.markdown(f"""
        <div class="final" style="margin-top:12px; text-align:left;">
            <h3>ข้อความที่สุ่มได้</h3>
            <p>{quotes[st.session_state.quote_index]}</p>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-title">สิ่งที่อยากให้เธอรู้</div>
            <div class="card-body">
                ไม่ต้องอ่านเยอะก็ได้ แค่เปิดมาแล้วรู้สึกว่าเว็บนี้ตั้งใจทำเพื่อเธอจริง ๆ ก็พอ
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button("เปลี่ยนบรรยากาศ"):
            st.session_state.clicks += 1

        st.markdown(f"""
        <div class="final" style="margin-top:12px; text-align:left;">
            <h3>กดเล่นแล้ว</h3>
            <p>{st.session_state.clicks} ครั้ง</p>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="section">
        <h2>ความทรงจำสั้น ๆ</h2>
        <p>ไม่ยาว แต่พอให้รู้ว่ามันมีเรื่องของเราอยู่</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("สุ่มความทรงจำ"):
        st.session_state.memory_index = random.randint(0, len(memories) - 1)

    st.markdown(f"""
    <div class="final" style="text-align:left;">
        <h3>{memories[st.session_state.memory_index]}</h3>
        <p>อันนี้คือโมเมนต์สั้น ๆ ที่อยากเก็บไว้ในเว็บของขวัญนี้</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="story">
        <div class="t">วันแรก</div>
        <div class="d">เริ่มคบกัน แล้วมันก็กลายเป็นเรื่องสำคัญขึ้นเรื่อย ๆ</div>
    </div>
    <div class="story">
        <div class="t">วันเกิดนี้</div>
        <div class="d">เลยอยากทำให้มันดูพิเศษกว่าวันปกติ</div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="section">
        <h2>เล่นสักหน่อย</h2>
        <p>มีตัวเลือกให้เว็บตอบกลับแบบสั้น ๆ</p>
    </div>
    """, unsafe_allow_html=True)

    mood = st.slider("ระดับความอบอุ่น", 0, 100, 63)
    st.progress(mood / 100)

    if mood < 35:
        mood_text = "ยังนุ่ม ๆ อยู่ แต่มีสีสันขึ้นแล้ว"
    elif mood < 75:
        mood_text = "เริ่มเข้าฟีลของของขวัญวันเกิดแล้ว"
    else:
        mood_text = "โอเค ตอนนี้มันเป็นของขวัญจริงจังแล้ว"

    st.markdown(f"""
    <div class="final" style="margin-top:12px; text-align:left;">
        <h3>ผลลัพธ์</h3>
        <p>{mood_text}</p>
    </div>
    """, unsafe_allow_html=True)

    vibe = st.radio("เลือกฟีลของเว็บ", ["หวานนิด ๆ", "อบอุ่นพอดี", "เรียบแต่พิเศษ", "น่ารักแบบไม่เยอะ"], horizontal=True)

    st.markdown(f"""
    <div class="story">
        <div class="t">ฟีลที่เลือก</div>
        <div class="d">{vibe}</div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="section">
        <h2>ปิดท้าย</h2>
        <p>มีปุ่มเซอร์ไพรส์ไว้ให้กดตอนจบ</p>
    </div>
    """, unsafe_allow_html=True)

    nickname = st.text_input("ชื่อเล่นที่อยากใช้", value="ครีม")
    note = st.text_area("ข้อความถึงเธอ", value="สุขสันต์วันเกิดนะเธอ ขอบคุณที่อยู่ด้วยกัน และขอให้วันนี้เป็นวันที่ดีมาก ๆ", height=110)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("เปิดของขวัญ 🎁"):
            st.session_state.gift_open = True
            st.balloons()

    with col2:
        if st.button("เพิ่มประกาย ✨"):
            st.snow()

    if st.session_state.gift_open:
        st.markdown(f"""
        <div class="final">
            <h3>สุขสันต์วันเกิดนะเธอ 💖</h3>
            <p>
                {note}<br><br>
                ถึงจะเรียก {nickname} บ้าง หรือเรียกเธอบ่อย ๆ บ้าง
                แต่เว็บนี้ตั้งใจทำมาเพื่อเธอจริง ๆ
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.download_button(
        "ดาวน์โหลดข้อความนี้",
        data=note,
        file_name="birthday_message.txt",
        mime="text/plain",
        use_container_width=True
    )

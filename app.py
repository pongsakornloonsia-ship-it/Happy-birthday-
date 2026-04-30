import streamlit as st
from datetime import date
import random

# =========================
# PAGE SETUP
# =========================
st.set_page_config(
    page_title="ของขวัญวันเกิดของเธอ 💖",
    page_icon="🎁",
    layout="wide",
)

# =========================
# DATA
# =========================
start_date = date(2024, 2, 14)
today = date.today()
days_together = (today - start_date).days
weeks_together = days_together // 7
months_together = days_together // 30

quotes = [
    "เธอทำให้วันธรรมดาดูมีความหมายมากขึ้น",
    "เราไม่ได้อยากเขียนเยอะ แค่อยากให้เธอรู้ว่าเธอสำคัญ",
    "บางวันไม่ต้องมีอะไรพิเศษ แค่มีเธอก็พอแล้ว",
    "ของขวัญชิ้นนี้ไม่ได้หวือหวา แต่ตั้งใจมากจริง ๆ",
    "อยู่ด้วยกันแบบนี้ต่อไป ก็ดีแล้ว",
]

memories = [
    ("วันแรก", "วันที่เริ่มคบกัน แล้วทุกอย่างก็ไม่เหมือนเดิมอีกเลย"),
    ("ช่วงงอน", "ต่อให้มีงอนกันบ้าง สุดท้ายก็ยังเลือกกันอยู่"),
    ("วันที่สบายใจ", "วันที่แค่คุยกันเฉย ๆ ก็รู้สึกดีแล้ว"),
    ("วันธรรมดา", "วันที่ไม่มีอะไรเยอะ แต่กลับจำได้ชัด"),
    ("วันที่พิเศษ", "วันที่เธอทำให้รู้สึกว่า เรื่องของเราสำคัญจริง ๆ"),
]

mini_cards = [
    ("✨", "ไม่ต้องหวานเวอร์", "แค่เป็นตัวเองก็พอแล้ว"),
    ("💗", "ใช้คำว่าเธอ", "เรียกแบบนี้แหละที่เป็นสไตล์ของเรา"),
    ("🎀", "โทนสีพอดี ๆ", "สดขึ้น แต่ไม่สว่างจ้า"),
    ("🫶", "มีลูกเล่น", "กดเล่นได้หลายอย่าง ไม่จบไว"),
    ("🎁", "ฟีลของขวัญ", "ตั้งใจให้ดูเป็นของขวัญจริง"),
    ("🌷", "เรียบแต่มีชีวิต", "ไม่โล่ง และไม่รก"),
]

special_notes = [
    "เธอเป็นคนที่ทำให้เรายิ้มง่ายขึ้น",
    "บางทีไม่ต้องพูดเยอะ แค่มีเธอก็พอ",
    "วันนี้อาจเป็นวันเกิดของเธอ แต่เราแอบรู้สึกว่าเป็นวันที่สำคัญของเราเหมือนกัน",
    "ครีมเป็นชื่อที่น่ารักนะ แต่เราชอบเรียกเธอมากกว่า",
]

vibes = [
    "หวานนิด ๆ",
    "อบอุ่นพอดี",
    "น่ารักแบบเรียบ ๆ",
    "พิเศษแบบไม่ต้องดัง",
]

gift_options = [
    "ข้อความสั้น ๆ แต่ตรงใจ",
    "การ์ดเล็ก ๆ ที่กดแล้วมีเซอร์ไพรส์",
    "เว็บที่เล่าเรื่องของเราจริง ๆ",
    "ของขวัญที่มีความตั้งใจมากกว่าความแพง",
]

reasons = [
    "อยู่ด้วยแล้วสบายใจ",
    "ไม่ต้องพยายามเป็นใคร",
    "คุยกันแล้วรู้สึกดี",
    "มีงอนบ้าง แต่ก็ยังอยากคุยกันต่อ",
    "เป็นเธอแบบนี้แหละ ดีแล้ว",
]

# =========================
# SESSION STATE
# =========================
if "quote_index" not in st.session_state:
    st.session_state.quote_index = 0
if "memory_index" not in st.session_state:
    st.session_state.memory_index = 0
if "love_clicks" not in st.session_state:
    st.session_state.love_clicks = 0
if "secret_open" not in st.session_state:
    st.session_state.secret_open = False
if "final_open" not in st.session_state:
    st.session_state.final_open = False
if "picked_vibe" not in st.session_state:
    st.session_state.picked_vibe = vibes[1]

# =========================
# CSS
# =========================
st.markdown(
    """
    <style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(255, 190, 214, 0.55), transparent 22%),
            radial-gradient(circle at 90% 20%, rgba(188, 179, 255, 0.42), transparent 20%),
            radial-gradient(circle at 50% 90%, rgba(255, 220, 174, 0.35), transparent 24%),
            linear-gradient(135deg, #f7d9e8 0%, #f4e7ff 42%, #ffe8d6 100%);
        color: #3b2340;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 1.1rem;
        padding-bottom: 2.5rem;
    }

    .hero {
        padding: 28px 24px;
        border-radius: 30px;
        background: rgba(255,255,255,0.44);
        border: 1px solid rgba(255,255,255,0.55);
        box-shadow: 0 18px 40px rgba(94, 60, 97, 0.12);
        backdrop-filter: blur(10px);
        text-align: center;
        margin-bottom: 18px;
    }

    .badge {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.70);
        border: 1px solid rgba(132, 88, 148, 0.10);
        color: #7b547d;
        font-size: 0.92rem;
        margin-bottom: 12px;
        font-weight: 700;
    }

    .title {
        font-size: clamp(2.2rem, 4.6vw, 4rem);
        font-weight: 900;
        margin: 0;
        color: #522a55;
        letter-spacing: -0.03em;
    }

    .subtitle {
        margin: 12px auto 0 auto;
        max-width: 760px;
        color: #6f5571;
        line-height: 1.72;
        font-size: 1.02rem;
    }

    .stats {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-top: 18px;
    }

    .stat {
        padding: 16px 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.62);
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 10px 24px rgba(90, 64, 98, 0.08);
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
        color: #7d687e;
        font-size: 0.92rem;
    }

    .section {
        margin-top: 18px;
        padding: 18px;
        border-radius: 26px;
        background: rgba(255,255,255,0.50);
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 14px 32px rgba(94, 60, 97, 0.10);
        backdrop-filter: blur(8px);
    }

    .section h2 {
        margin: 0 0 8px 0;
        color: #553059;
        font-size: 1.35rem;
    }

    .section p {
        margin: 0;
        color: #6e5970;
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
        background: linear-gradient(135deg, rgba(255, 143, 182, 0.24), rgba(177, 145, 255, 0.24));
        border: 1px solid rgba(132, 88, 148, 0.10);
        color: #5a355f;
        font-weight: 700;
        font-size: 0.92rem;
    }

    .card {
        height: 100%;
        padding: 16px 16px 14px 16px;
        border-radius: 22px;
        background: rgba(255,255,255,0.66);
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 10px 24px rgba(90, 64, 98, 0.08);
    }

    .icon {
        width: 40px;
        height: 40px;
        border-radius: 14px;
        display: grid;
        place-items: center;
        font-size: 1.1rem;
        background: linear-gradient(135deg, rgba(255, 143, 182, 0.35), rgba(177, 145, 255, 0.35));
        margin-bottom: 10px;
    }

    .card-title {
        color: #5a355f;
        font-size: 1.02rem;
        font-weight: 900;
        margin-bottom: 7px;
    }

    .card-body {
        color: #6e5970;
        font-size: 0.95rem;
        line-height: 1.68;
    }

    .mini-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
        margin-top: 12px;
    }

    .mini {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.60);
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 10px 22px rgba(90, 64, 98, 0.08);
    }

    .mini .k {
        color: #5a355f;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .mini .v {
        color: #6e5970;
        font-size: 0.95rem;
        line-height: 1.65;
    }

    .story-list {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
        margin-top: 12px;
    }

    .story {
        padding: 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.62);
        border: 1px solid rgba(132, 88, 148, 0.10);
    }

    .story .t {
        color: #5a355f;
        font-weight: 900;
        margin-bottom: 6px;
    }

    .story .d {
        color: #6e5970;
        line-height: 1.65;
        font-size: 0.95rem;
    }

    .soft-box {
        padding: 16px;
        border-radius: 22px;
        background: linear-gradient(135deg, rgba(255,255,255,0.62), rgba(255,255,255,0.50));
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 10px 22px rgba(90, 64, 98, 0.08);
    }

    .big-note {
        font-size: 1.1rem;
        color: #5a355f;
        font-weight: 800;
        line-height: 1.72;
    }

    .muted {
        color: #6e5970;
        line-height: 1.72;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 0;
        padding: 0.82rem 1rem;
        background: linear-gradient(135deg, #ff7ea8, #a87bff);
        color: white;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(94, 60, 97, 0.18);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 28px rgba(94, 60, 97, 0.22);
    }

    .footer-box {
        margin-top: 18px;
        padding: 18px;
        border-radius: 24px;
        background: rgba(255,255,255,0.58);
        border: 1px solid rgba(132, 88, 148, 0.10);
        box-shadow: 0 12px 26px rgba(90, 64, 98, 0.08);
        text-align: center;
    }

    .footer-big {
        font-size: 1.35rem;
        font-weight: 900;
        color: #5a355f;
        margin-bottom: 6px;
    }

    .footer-small {
        color: #6e5970;
        line-height: 1.72;
    }

    @media (max-width: 900px) {
        .stats, .mini-grid, .story-list {
            grid-template-columns: 1fr 1fr;
        }
    }

    @media (max-width: 700px) {
        .stats, .mini-grid, .story-list {
            grid-template-columns: 1fr;
        }
        .hero {
            padding: 22px 16px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# TITLE
# =========================
st.markdown(
    """
    <div class="hero">
        <div class="badge">Birthday Gift • สำหรับเธอ</div>
        <div class="title">ของขวัญวันเกิดที่ตั้งใจทำจริง ๆ 💖</div>
        <div class="subtitle">
            โทนนี้ปรับให้สว่างขึ้นแบบพอดี ๆ ไม่มืดเกิน และมีลูกเล่นหลายส่วน
            เพื่อให้มันดูเป็นของขวัญ ไม่ใช่หน้าแอปโล่ง ๆ
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# =========================
# METRICS
# =========================
st.markdown(
    f"""
    <div class="stats">
        <div class="stat"><div class="num">{days_together}</div><div class="label">วันตั้งแต่ 14/02/2024</div></div>
        <div class="stat"><div class="num">{weeks_together}</div><div class="label">สัปดาห์โดยประมาณ</div></div>
        <div class="stat"><div class="num">{months_together}</div><div class="label">เดือนโดยประมาณ</div></div>
        <div class="stat"><div class="num">1</div><div class="label">คนพิเศษคนนี้</div></div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <h2>ชิ้นเล็ก ๆ ที่อยู่ในของขวัญนี้</h2>
        <p>เว็บนี้ไม่ได้พยายามยัดทุกอย่างให้ยาวเกินไป แต่เพิ่มลูกเล่นให้มันมีชีวิตขึ้น</p>
        <div class="chips">
    """,
    unsafe_allow_html=True,
)

for chip in [
    "💗 ใช้สีพอดี ๆ",
    "🎁 มีความเป็นของขวัญ",
    "✨ มีข้อความสุ่ม",
    "🫶 มีปุ่มกดเล่น",
    "🌷 โทนอุ่น ไม่ดำ",
    "📖 อ่านง่ายกว่าเดิม",
]:
    st.markdown(f'<span class="chip">{chip}</span>', unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# =========================
# TABS
# =========================
tab1, tab2, tab3, tab4, tab5 = st.tabs(["ภาพรวม", "ความทรงจำ", "เล่นสักหน่อย", "กล่องข้อความ", "เซอร์ไพรส์"])

# -------------------------
# TAB 1: Overview
# -------------------------
with tab1:
    col1, col2 = st.columns([1.35, 1])
    with col1:
        st.markdown(
            """
            <div class="soft-box">
                <div class="big-note">เว็บนี้ตั้งใจให้ดู “อบอุ่น” มากกว่าดู “เยอะ”</div>
                <div class="muted" style="margin-top:8px;">
                    เลยใช้ข้อความสั้น ๆ, การ์ดนุ่ม ๆ, สีพาสเทลแบบไม่จ้า และมีปุ่มให้กดเล่นนิดหน่อย
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            """
            <div class="section">
                <h2>ข้อความสุ่มหนึ่งประโยค</h2>
                <p>กดปุ่มแล้วเว็บจะสุ่มประโยคให้ใหม่</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("สุ่มข้อความ"):
            st.session_state.quote_index = random.randint(0, len(quotes) - 1)

        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left;">
                <div class="footer-big">“{quotes[st.session_state.quote_index]}”</div>
                <div class="footer-small">อันนี้เปลี่ยนทุกครั้งที่กดปุ่ม</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="section">
                <h2>4 คำที่ทำให้หน้าเว็บดูมีอะไร</h2>
                <p>อันนี้ช่วยให้หน้าแรกไม่โล่งเกิน</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        for icon, title, body in mini_cards:
            st.markdown(
                f"""
                <div class="card" style="margin-bottom:12px;">
                    <div class="icon">{icon}</div>
                    <div class="card-title">{title}</div>
                    <div class="card-body">{body}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# -------------------------
# TAB 2: Memories
# -------------------------
with tab2:
    st.markdown(
        """
        <div class="section">
            <h2>ความทรงจำสั้น ๆ</h2>
            <p>ไม่ต้องยาว แค่ให้มีจุดจำได้ก็พอ</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("สุ่มความทรงจำ"):
            st.session_state.memory_index = random.randint(0, len(memories) - 1)

        current_memory_title, current_memory_text = memories[st.session_state.memory_index]
        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left;">
                <div class="footer-big">{current_memory_title}</div>
                <div class="footer-small">{current_memory_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        picked = st.selectbox(
            "เลือกความทรงจำที่อยากเปิด",
            [m[0] for m in memories],
            index=st.session_state.memory_index,
        )
        idx = [m[0] for m in memories].index(picked)
        st.session_state.memory_index = idx

        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left; margin-top:12px;">
                <div class="footer-big">{memories[idx][0]}</div>
                <div class="footer-small">{memories[idx][1]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="story-list">
            <div class="story">
                <div class="t">วันแรก</div>
                <div class="d">เริ่มคบกัน และทุกอย่างก็ค่อย ๆ มีความหมายขึ้น</div>
            </div>
            <div class="story">
                <div class="t">ระหว่างทาง</div>
                <div class="d">มีทั้งดีและไม่ดี แต่ก็ยังอยู่กันตรงนี้</div>
            </div>
            <div class="story">
                <div class="t">วันนี้</div>
                <div class="d">มันไม่ได้เป็นแค่วันที่ผ่านมา แต่มันคือเรื่องของเรา</div>
            </div>
            <div class="story">
                <div class="t">วันพิเศษ</div>
                <div class="d">เพราะวันเกิดเธอเลยกลายเป็นวันที่อยากทำอะไรให้เยอะขึ้น</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------------
# TAB 3: Play
# -------------------------
with tab3:
    st.markdown(
        """
        <div class="section">
            <h2>เล่นสักหน่อย</h2>
            <p>มีปุ่มและตัวเลือกให้เว็บดูมีปฏิสัมพันธ์มากขึ้น</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2 = st.columns(2)

    with c1:
        mood = st.slider("ระดับความคิดถึง", 0, 100, 58)
        st.progress(mood / 100)

        if mood < 35:
            mood_text = "ยังนิ่ง ๆ อยู่ แต่ก็แอบคิดถึงนะ"
        elif mood < 75:
            mood_text = "เริ่มอินแล้ว หน้าเว็บเริ่มมีฟีลขึ้น"
        else:
            mood_text = "โอเค ตอนนี้คิดถึงจริงจังแล้ว"

        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left; margin-top:12px;">
                <div class="footer-big">ผลลัพธ์</div>
                <div class="footer-small">{mood_text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        vibe = st.radio("วันนี้อยากได้ฟีลไหน", vibes, horizontal=False)
        st.session_state.picked_vibe = vibe

    with c2:
        gift = st.selectbox("ของขวัญแบบไหนที่เข้ากับเธอที่สุด", gift_options)
        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left;">
                <div class="footer-big">เหมาะสุดน่าจะเป็น</div>
                <div class="footer-small">{gift}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.button("กดนับครั้งที่คิดถึง"):
            st.session_state.love_clicks += 1

        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left; margin-top:12px;">
                <div class="footer-big">กดไปแล้ว {st.session_state.love_clicks} ครั้ง</div>
                <div class="footer-small">
                    ยิ่งกด ยิ่งเหมือนของขวัญชิ้นนี้ตั้งใจมากขึ้น
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if st.session_state.love_clicks >= 3:
            st.info("เริ่มมีความน่ารักแล้วนะ")

# -------------------------
# TAB 4: Message box
# -------------------------
with tab4:
    st.markdown(
        """
        <div class="section">
            <h2>กล่องข้อความ</h2>
            <p>ตรงนี้ทำให้เว็บมีความเป็นของขวัญที่ “แก้เองได้”</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    nickname = st.text_input("ชื่อเล่นแฟน (ใส่ไว้เฉพาะตอนอยากใช้)", value="ครีม")
    special_line = random.choice(special_notes)

    st.markdown(
        f"""
        <div class="soft-box">
            <div class="big-note">ข้อความพิเศษของวันนี้</div>
            <div class="muted" style="margin-top:8px;">
                {special_line}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.checkbox("เปิดข้อความลับ", key="secret_toggle")
    st.session_state.secret_open = st.session_state.secret_toggle

    if st.session_state.secret_open:
        st.markdown(
            f"""
            <div class="footer-box" style="text-align:left; margin-top:12px;">
                <div class="footer-big">ข้อความลับ</div>
                <div class="footer-small">
                    {nickname} อาจเป็นชื่อที่น่ารัก แต่สำหรับเรา ส่วนใหญ่ยังชอบเรียกเธอมากกว่าอยู่ดี
                    ของขวัญชิ้นนี้เลยตั้งใจให้ดูอบอุ่น พอดี ๆ และเป็นของเธอจริง ๆ
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    note = st.text_area(
        "เขียนข้อความถึงเธอได้ตรงนี้",
        value="สุขสันต์วันเกิดนะเธอ ขอบคุณที่อยู่ด้วยกัน และขอให้ปีนี้เป็นปีที่ดีมาก ๆ",
        height=120,
    )

    st.download_button(
        label="ดาวน์โหลดข้อความนี้",
        data=note,
        file_name="birthday_message.txt",
        mime="text/plain",
        use_container_width=True,
    )

# -------------------------
# TAB 5: Surprise
# -------------------------
with tab5:
    st.markdown(
        """
        <div class="section">
            <h2>เซอร์ไพรส์</h2>
            <p>ให้ของขวัญปิดท้ายดูมีจังหวะขึ้นอีกนิด</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("กดรับของขวัญ 🎁"):
            st.session_state.final_open = True
            st.balloons()

    wi

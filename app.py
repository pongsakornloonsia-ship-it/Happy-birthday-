import streamlit as st
from datetime import date
import random

st.set_page_config(page_title="Birthday Gift ❤️", page_icon="💖", layout="centered")

# -------------------- DATE --------------------
start_date = date(2024, 2, 14)
today = date.today()
days_together = (today - start_date).days
weeks_together = days_together // 7
months_together = days_together // 30

# -------------------- STATE --------------------
if "show_secret" not in st.session_state:
    st.session_state.show_secret = False
if "show_final" not in st.session_state:
    st.session_state.show_final = False

# -------------------- CSS --------------------
st.markdown(
    """
    <style>
    :root{
        --bg1:#ff4d8d;
        --bg2:#7c4dff;
        --bg3:#ffb84d;
        --card:rgba(17, 17, 28, 0.58);
        --card2:rgba(255, 255, 255, 0.08);
        --text:#fff7fb;
        --muted:rgba(255,255,255,0.78);
        --line:rgba(255,255,255,0.14);
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, rgba(255,77,141,0.45), transparent 28%),
            radial-gradient(circle at 90% 20%, rgba(124,77,255,0.40), transparent 26%),
            radial-gradient(circle at 50% 90%, rgba(255,184,77,0.30), transparent 28%),
            linear-gradient(135deg, #120b2e 0%, #1d1040 45%, #2b114d 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 980px;
        padding-top: 1.2rem;
        padding-bottom: 3rem;
    }

    .page {
        position: relative;
        z-index: 2;
    }

    .hero {
        position: relative;
        overflow: hidden;
        border: 1px solid var(--line);
        border-radius: 30px;
        padding: 34px 24px 28px 24px;
        background:
            linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0.05)),
            radial-gradient(circle at top left, rgba(255,77,141,0.18), transparent 32%),
            radial-gradient(circle at top right, rgba(124,77,255,0.16), transparent 30%);
        box-shadow: 0 18px 50px rgba(0,0,0,0.32);
        backdrop-filter: blur(10px);
        text-align: center;
        margin-bottom: 22px;
    }

    .eyebrow {
        display: inline-block;
        padding: 7px 14px;
        border-radius: 999px;
        background: rgba(255,255,255,0.10);
        border: 1px solid rgba(255,255,255,0.15);
        color: var(--muted);
        font-size: 0.9rem;
        letter-spacing: 0.2px;
        margin-bottom: 14px;
    }

    .title {
        font-size: clamp(2.2rem, 5vw, 4.2rem);
        line-height: 1.03;
        font-weight: 900;
        margin: 0;
        color: #fff;
        text-shadow: 0 0 18px rgba(255,255,255,0.15);
    }

    .subtitle {
        margin: 14px auto 0 auto;
        max-width: 740px;
        color: var(--muted);
        font-size: 1.05rem;
        line-height: 1.7;
    }

    .stats {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 14px;
        margin-top: 22px;
    }

    .stat {
        border-radius: 22px;
        padding: 18px 16px;
        background: linear-gradient(180deg, rgba(255,255,255,0.12), rgba(255,255,255,0.06));
        border: 1px solid rgba(255,255,255,0.14);
        box-shadow: 0 8px 24px rgba(0,0,0,0.18);
    }

    .stat .num {
        font-size: 2rem;
        font-weight: 900;
        color: #fff;
        line-height: 1.0;
    }

    .stat .label {
        margin-top: 7px;
        color: var(--muted);
        font-size: 0.95rem;
    }

    .section {
        margin-top: 22px;
        padding: 22px 20px;
        border-radius: 28px;
        background: var(--card);
        border: 1px solid var(--line);
        box-shadow: 0 12px 36px rgba(0,0,0,0.28);
        backdrop-filter: blur(10px);
    }

    .section h2 {
        margin: 0 0 10px 0;
        color: #fff;
        font-size: 1.5rem;
        letter-spacing: 0.2px;
    }

    .section p {
        color: var(--muted);
        line-height: 1.75;
        margin: 0;
        font-size: 1rem;
    }

    .line {
        width: 100%;
        height: 1px;
        margin: 18px 0;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.25), transparent);
    }

    .grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 14px;
        margin-top: 14px;
    }

    .card {
        min-height: 156px;
        padding: 16px 16px 14px 16px;
        border-radius: 22px;
        background: linear-gradient(180deg, rgba(255,255,255,0.11), rgba(255,255,255,0.05));
        border: 1px solid rgba(255,255,255,0.12);
        box-shadow: 0 12px 26px rgba(0,0,0,0.17);
    }

    .card .icon {
        width: 42px;
        height: 42px;
        border-radius: 14px;
        display: grid;
        place-items: center;
        font-size: 1.25rem;
        background: linear-gradient(135deg, rgba(255,77,141,0.4), rgba(124,77,255,0.32));
        margin-bottom: 10px;
    }

    .card .card-title {
        color: #fff;
        font-size: 1.05rem;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .card .card-body {
        color: rgba(255,255,255,0.78);
        font-size: 0.96rem;
        line-height: 1.65;
    }

    .timeline {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-top: 14px;
    }

    .step {
        padding: 16px 14px;
        border-radius: 20px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        min-height: 122px;
    }

    .step .t {
        color: #fff;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .step .d {
        color: var(--muted);
        font-size: 0.92rem;
        line-height: 1.6;
    }

    .pill-row {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 12px;
    }

    .pill {
        display: inline-block;
        padding: 9px 13px;
        border-radius: 999px;
        font-size: 0.92rem;
        color: #fff;
        background: linear-gradient(135deg, rgba(255,77,141,0.22), rgba(124,77,255,0.22));
        border: 1px solid rgba(255,255,255,0.14);
    }

    .question {
        padding: 16px;
        border-radius: 20px;
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.12);
        margin-top: 14px;
    }

    .final-box {
        text-align: center;
        padding: 22px 18px;
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(255,77,141,0.18), rgba(124,77,255,0.18));
        border: 1px solid rgba(255,255,255,0.14);
    }

    .final-big {
        font-size: 1.5rem;
        font-weight: 900;
        color: #fff;
        margin-bottom: 8px;
    }

    .final-small {
        color: var(--muted);
        line-height: 1.7;
    }

    .streamlit-button button {
        border: none !important;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 999px;
        border: 0;
        padding: 0.82rem 1.15rem;
        background: linear-gradient(135deg, #ff4d8d, #7c4dff);
        color: white;
        font-weight: 800;
        box-shadow: 0 12px 26px rgba(0,0,0,0.22);
        transition: transform 0.15s ease, box-shadow 0.15s ease, opacity 0.15s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 16px 30px rgba(0,0,0,0.26);
    }

    div.stButton > button:active {
        transform: translateY(0px) scale(0.99);
    }

    .hearts {
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
        filter: blur(0.2px);
        user-select: none;
    }

    @keyframes floatUp {
        0% { transform: translateY(0) scale(0.9) rotate(0deg); opacity: 0; }
        10% { opacity: 0.24; }
        100% { transform: translateY(-115vh) scale(1.2) rotate(18deg); opacity: 0; }
    }

    .spark {
        position: absolute;
        border-radius: 999px;
        filter: blur(1px);
        opacity: 0.32;
        pointer-events: none;
    }

    .sp1 { width: 180px; height: 180px; left: -50px; top: 80px; background: rgba(255,77,141,0.23); }
    .sp2 { width: 220px; height: 220px; right: -70px; top: 230px; background: rgba(124,77,255,0.20); }
    .sp3 { width: 160px; height: 160px; left: 36%; top: 8px; background: rgba(255,184,77,0.17); }

    @media (max-width: 720px) {
        .stats, .grid, .timeline {
            grid-template-columns: 1fr;
        }
        .hero { padding: 28px 16px 22px 16px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- FLOATING HEARTS --------------------
hearts_html = "".join(
    f'<span class="heart" style="left:{random.randint(0,100)}%; '
    f'animation-duration:{random.randint(8,14)}s; '
    f'animation-delay:{random.uniform(0,6):.2f}s; '
    f'font-size:{random.randint(16,34)}px;">❤</span>'
    for _ in range(18)
)

st.markdown(
    f"""
    <div class="hearts">
        <div class="spark sp1"></div>
        <div class="spark sp2"></div>
        <div class="spark sp3"></div>
        {hearts_html}
    </div>
    """,
    unsafe_allow_html=True,
)

# -------------------- HELPERS --------------------
def html_card(icon: str, title: str, body: str) -> str:
    return f"""
    <div class="card">
        <div class="icon">{icon}</div>
        <div class="card-title">{title}</div>
        <div class="card-body">{body}</div>
    </div>
    """

# -------------------- CONTENT --------------------
st.markdown('<div class="page">', unsafe_allow_html=True)

st.markdown(
    f"""
    <div class="hero">
        <div class="eyebrow">Birthday Edition • เริ่มคบกันวันที่ 14/02/2024</div>
        <div class="title">ของขวัญวันเกิดสำหรับคนสำคัญ 💖</div>
        <div class="subtitle">
            เว็บนี้ทำขึ้นมาเพื่อเก็บความรู้สึกดี ๆ ระหว่างเราไว้ในที่เดียว
            ให้มันดูจริงจังขึ้น ไม่จืด ไม่โล่ง และไม่เหมือนเว็บเดโม่
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="section">
        <h2>เวลาที่เราเดินมาด้วยกัน</h2>
        <p>นับจากวันที่ 14 กุมภาพันธ์ 2024 ถึงวันนี้</p>
        <div class="stats">
            <div class="stat">
                <div class="num">{days_together}</div>
                <div class="label">วัน</div>
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
        <div class="pill-row">
            <span class="pill">💫 14/02/2024</span>
            <span class="pill">🎂 Birthday Gift</span>
            <span class="pill">💌 Made with effort</span>
            <span class="pill">🌈 No blank white screen</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <h2>10 อย่างที่อยากให้จำ</h2>
        <p>อันนี้คือ 10 ฟีเจอร์/ความหมายที่เพิ่มเข้ามา เพื่อให้เว็บดูมีอะไรและไม่จบไว</p>
        <div class="grid">
    """,
    unsafe_allow_html=True,
)

reasons = [
    ("✨", "เว็บมีธีมสีเข้มแบบไล่เฉด", "ไม่ขาวจืดแล้ว พื้นหลังเป็น gradient หลายชั้น มีความลึกและดูเหมือนงานจริง"),
    ("💖", "มีการ์ดโปร่งแสง", "ทำให้เนื้อหาเด่นขึ้น ดูโมเดิร์น และไม่ลอยหายไปกับพื้นหลัง"),
    ("🌙", "มีดาวและแสงเรือง", "เพิ่มบรรยากาศให้โรแมนติกขึ้นโดยไม่ต้องใช้รูป"),
    ("💘", "มีหัวใจลอยแบบต่อเนื่อง", "หน้าเว็บดูมีชีวิต ไม่ใช่หน้าโล่ง ๆ ธรรมดา"),
    ("🎁", "มีปุ่มเซอร์ไพรส์", "ให้คนกดแล้วค่อยเห็นข้อความพิเศษ เพิ่มจังหวะของขวัญ"),
    ("🧠", "คำนวณวันจากวันที่จริง", "แสดงจำนวนวันที่เริ่มคบจาก 14/02/2024 แบบอัตโนมัติ"),
    ("🔥", "มีตัวเลขใหญ่เป็นพระเอก", "ทำให้ข้อมูลสำคัญเด่นขึ้นมากกว่าข้อความทั่วไป"),
    ("📜", "มีไทม์ไลน์สั้น ๆ", "ช่วยเล่าเรื่องให้เว็บมีโครง ไม่ดูเหมือนกองข้อความ"),
    ("🎨", "มีปุ่มและชิปสีสด", "ช่วยพยุงสายตาและทำให้เว็บดูสนุกขึ้น"),
    ("💎", "มีข้อความปิดท้ายแบบตั้งใจ", "ทำให้เว็บจบแบบมีอารมณ์ ไม่ใช่จบแบบว่างเปล่า"),
]

for i in range(0, len(reasons), 2):
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(html_card(*reasons[i]), unsafe_allow_html=True)
    with c2:
        st.markdown(html_card(*reasons[i + 1]), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">
        <h2>ไทม์ไลน์สั้น ๆ</h2>
        <p>เอาไว้ช่วยให้เว็บดูมีเรื่องเล่า ไม่ใช่แค่ข้อความกระจัดกระจาย</p>
        <div class="timeline">
            <div class="step">
                <div class="t">14/02/2024</div>
                <div class="d">วันที่เริ่มคบกัน และเป็นจุดเริ่มต้นของทุกอย่าง</div>
            </div>
            <div class="step">
                <div class="t">ระหว่างทาง</div>
                <div class="d">มีทั้งวันที่ดีและไม่ดี แต่ก็ยังเดินมาด้วยกัน</div>
            </div>
            <div class="step">
                <div class="t">วันนี้</div>
                <div class="d">เว็บนี้คือหลักฐานว่าเรื่องของเราไม่ธรรมดา</div>
            </div>
            <div class="step">
                <div class="t">วันเกิดนี้</div>
                <div class="d">ถูกทำให้เป็นของขวัญ ไม่ใช่แค่หน้าเว็บทั่ว ๆ ไป</div>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <h2>โหมดความคิดถึง</h2>
        <p>เลื่อนเพื่อปรับอารมณ์ให้หน้าเว็บดูมีปฏิสัมพันธ์มากขึ้น</p>
    """,
    unsafe_allow_html=True,
)

mood = st.slider("ระดับความคิดถึง", 0, 100, 84)
st.progress(mood / 100)

if mood < 35:
    mood_text = "วันนี้ยังยิ้มอยู่ แต่ก็คิดถึงอยู่ดี"
elif mood < 70:
    mood_text = "เริ่มอินแล้ว หน้าเว็บเริ่มมีน้ำหนัก"
else:
    mood_text = "โอเค ตอนนี้เริ่มเป็นของขวัญจริง ๆ แล้ว"

st.markdown(
    f"""
    <div class="question">
        <div style="color:#fff;font-weight:800;margin-bottom:6px;">ผลลัพธ์ของตอนนี้</div>
        <div style="color:rgba(255,255,255,0.82);line-height:1.7;">{mood_text}</div>
    </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section">
        <h2>ข้อความลับ</h2>
        <p>อันนี้กดเปิดเองได้ ให้มันมีจังหวะและไม่จบไว</p>
    """,
    unsafe_allow_html=True,
)

st.checkbox("เปิดข้อความลับ", key="secret_toggle")
st.session_state.show_secret = st.session_state.get("secret_toggle", False)

if st.session_state.show_secret:
    st.markdown(
        """
        <div class="final-box">
            <div class="final-big">เราอาจไม่ได้ทำเว็บที่ใหญ่ที่สุด</div>
            <div class="final-small">
                แต่เราอยากให้มันเป็นเว็บที่มีความหมายที่สุดสำหรับเธอ<br>
                ทุกสี ทุกข้อความ และทุกปุ่ม ถูกใส่มาเพื่อให้มันรู้สึกเหมือนของขวัญจริง ๆ
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div class="section">
        <h2>กดเพื่อเปิดเซอร์ไพรส์</h2>
        <p>อันนี้เป็นตอนจบของของขวัญ กดแล้วให้มันดูพิเศษขึ้นอีกนิด</p>
    """,
    unsafe_allow_html=True,
)

if st.button("กดรับของขวัญ 🎀"):
    st.session_state.show_final = True
    st.balloons()

if st.session_state.show_final:
    st.markdown(
        """
        <div class="final-box">
            <div class="final-big">สุขสันต์วันเกิดนะ 💖</div>
            <div class="final-small">
                ขอบคุณที่อยู่ด้วยกันตั้งแต่วันที่ 14/02/2024<br>
                ขอให้ปีนี้เป็นปีที่ดี มีแต่เรื่องดี ๆ และมีเราคอยอยู่ข้าง ๆ เสมอ
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("</div>", unsafe_allow_html=True)

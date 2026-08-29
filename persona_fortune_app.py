import streamlit as st
import streamlit.components.v1 as components
import random
import base64
import os
from datetime import date

# ------------------------------
# 설정: 여기에 본인 제휴 링크를 넣으세요
# ------------------------------
COUPANG_LINK = "https://link.coupang.com/a/gATwbtGIIS"
TOSS_LINK = "https://toss.me/여기에_본인_토스_쉐어링크"

# ------------------------------
# 배경 이미지 설정
# 이 파일과 같은 폴더에 background.jpg (또는 .png) 파일을 넣으면
# 자동으로 배경으로 깔리고, 없으면 기존 그라데이션이 그대로 사용됩니다.
# ------------------------------
BACKGROUND_IMAGE_PATH = "background.jpg"


def _get_base64_image(path: str):
    if not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


_bg_base64 = _get_base64_image(BACKGROUND_IMAGE_PATH)
if _bg_base64:
    _ext = BACKGROUND_IMAGE_PATH.split(".")[-1]
    _background_css = f"""
    .stApp {{
        background-image: linear-gradient(rgba(20,18,22,0.82), rgba(20,18,22,0.82)),
                           url("data:image/{_ext};base64,{_bg_base64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
else:
    _background_css = """
    .stApp {
        background: linear-gradient(180deg, #1c1a1f 0%, #2a2630 50%, #1c1a1f 100%);
    }
    """

st.set_page_config(page_title="운세 캐릭터관", page_icon="🔮", layout="centered")

st.markdown(f"<style>{_background_css}</style>", unsafe_allow_html=True)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 1.2rem;
    }
    .title-blue {
        background: linear-gradient(90deg, #6ec6ff, #3fa9f5, #1e88e5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .title-warm {
        background: linear-gradient(90deg, #ffcf6b, #ff9d4d, #ff7043);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 18px rgba(255, 180, 90, 0.35);
    }
    .persona-avatar {
        font-size: 3.6rem;
        width: 100px;
        height: 100px;
        line-height: 100px;
        border-radius: 50%;
        margin: 0 auto 14px auto;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
        overflow: hidden;
    }
    .persona-avatar svg {
        width: 72px;
        height: 72px;
    }
    .persona-name {
        text-align: center;
        font-size: 1.2rem;
        font-weight: 800;
        color: #f9d976;
        margin-bottom: 18px;
    }
    .speech-bubble {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 18px;
        padding: 20px 22px;
        font-size: 1.05rem;
        color: #f0eaff;
        line-height: 1.65;
        margin-bottom: 24px;
    }
    .fortune-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 22px;
        margin-bottom: 12px;
    }
    .fortune-cat-title {
        font-size: 1.05rem;
        font-weight: 700;
        color: #f9d976;
        margin-bottom: 4px;
    }
    .fortune-cat-text {
        font-size: 0.98rem;
        color: #f0eaff;
        line-height: 1.6;
    }
    .lucky-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        color: #f5f0ff;
        margin: 16px 0;
    }
    .progress-dots {
        text-align: center;
        margin-bottom: 20px;
        color: #a89bb5;
        font-size: 0.85rem;
        letter-spacing: 3px;
    }
    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #f9d976, #c99df0);
        color: #1c1a1f;
        font-weight: 800;
        font-size: 1.05rem;
        border-radius: 30px;
        border: none;
        padding: 12px 28px;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    div[data-testid="stButton"] button p {
        text-align: center;
        width: 100%;
        font-size: 1.05rem;
    }
    div[data-testid="stLinkButton"] a {
        border-radius: 30px !important;
        font-weight: 900 !important;
        font-size: 1.4rem !important;
        letter-spacing: 0.2px !important;
        padding: 20px 6px !important;
        line-height: 1.25 !important;
        color: #ffffff !important;
        background: linear-gradient(180deg, #ffb066 0%, #ff5e3a 100%) !important;
        text-shadow: 0 1px 3px rgba(0,0,0,0.35) !important;
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.5),
            inset 0 -3px 6px rgba(0,0,0,0.25),
            0 6px 0 #c23e1f,
            0 10px 18px rgba(0,0,0,0.45) !important;
        border: none !important;
        transform: translateY(0);
        -webkit-text-size-adjust: 100% !important;
        text-size-adjust: 100% !important;
    }
    div[data-testid="stLinkButton"] a * {
        font-size: 1.4rem !important;
        font-weight: 900 !important;
        color: #ffffff !important;
    }
    @media (max-width: 480px) {
        div[data-testid="stLinkButton"] a {
            font-size: 1.8rem !important;
            padding: 20px 8px !important;
            line-height: 1.3 !important;
        }
        div[data-testid="stLinkButton"] a * {
            font-size: 1.8rem !important;
        }
    }
    div[data-testid*="olumn"]:nth-of-type(2) div[data-testid="stLinkButton"] a,
    div[data-testid*="olumn"]:nth-of-type(2) div[data-testid="stLinkButton"] a * {
        background: linear-gradient(180deg, #4dabff 0%, #0064ff 100%) !important;
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.5),
            inset 0 -3px 6px rgba(0,0,0,0.25),
            0 6px 0 #0047b8,
            0 10px 18px rgba(0,0,0,0.45) !important;
    }
    [data-testid="stCaptionContainer"] p, .stCaption {
        color: #cbb8d8 !important;
        opacity: 1 !important;
    }
    label, .stSlider label {
        color: #cbb8d8 !important;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown p {
        color: #f5f0ff !important;
        opacity: 1 !important;
    }
    div[data-testid="stTextInput"] input {
        background: rgba(255,255,255,0.08) !important;
        color: #f5f0ff !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] { border-radius: 12px !important; }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] div {
        background: rgba(255,255,255,0.08) !important;
        color: #f5f0ff !important;
        border-color: rgba(255,255,255,0.2) !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        border: 1px solid rgba(255,255,255,0.2) !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] span { color: #f5f0ff !important; }
    div[data-baseweb="select"] svg { fill: #f9d976 !important; }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 캐릭터 페르소나 10종
# 각 페르소나: 인사말 / 이름 질문 / 이름 리액션 / 생년 리액션 / 버튼 문구 / 마무리 멘트
# ------------------------------
PERSONAS = {
    "mz_shaman": {
        "name": "MZ 여자무당", "emoji": "🔪", "color": "#b5283b",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#1c1c1c"/>
            <path d="M30 100 C33 84 40 74 50 74 C60 74 67 84 70 100 Z" fill="#7a1f2b"/>
            <rect x="44" y="56" width="12" height="14" rx="4" fill="#f3d9c0"/>
            <circle cx="50" cy="44" r="19" fill="#f3d9c0"/>
            <ellipse cx="43" cy="43" rx="2.6" ry="1.8" fill="#1a1a1a"/>
            <ellipse cx="57" cy="43" rx="2.6" ry="1.8" fill="#1a1a1a"/>
            <path d="M39 39 Q43 36.5 47 38" stroke="#1a1a1a" stroke-width="1.2" fill="none" stroke-linecap="round"/>
            <path d="M53 38 Q57 36.5 61 39" stroke="#1a1a1a" stroke-width="1.2" fill="none" stroke-linecap="round"/>
            <path d="M50 45 L48.5 50 Q50 51.2 51.5 50" stroke="#d8ac86" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M44 55 Q50 59 56 55" stroke="#a83246" stroke-width="2.2" fill="none" stroke-linecap="round"/>
            <path d="M27 40 Q25 70 33 82 L38 78 Q32 60 33 42 Z" fill="#141414"/>
            <path d="M73 40 Q75 70 67 82 L62 78 Q68 60 67 42 Z" fill="#141414"/>
            <path d="M29 34 Q50 16 71 34 Q69 24 50 20 Q31 24 29 34 Z" fill="#141414"/>
            <ellipse cx="50" cy="26" rx="30" ry="7" fill="#0d0d0d"/>
            <path d="M38 26 Q50 8 62 26 Z" fill="#0d0d0d"/>
            <circle cx="50" cy="22" r="6" fill="#c9a15a"/>
            <circle cx="50" cy="22" r="6" fill="none" stroke="#8a6a34" stroke-width="1"/>
            <g transform="translate(50,72)">
                <path d="M-22 14 L4 -14 L8 -10 L-18 18 Z" fill="#d8d8d8" stroke="#9a9a9a" stroke-width="0.5"/>
                <path d="M22 14 L-4 -14 L-8 -10 L18 18 Z" fill="#d8d8d8" stroke="#9a9a9a" stroke-width="0.5"/>
                <circle cx="-22" cy="14" r="3" fill="#c0392b"/>
                <circle cx="22" cy="14" r="3" fill="#c0392b"/>
            </g>
        </svg>''',
        "greeting": "안뇽! 나 지금 좀 신기 올라와서ㅋㅋ 몇 개만 물어볼게!",
        "ask_name": "너 이름이 뭐야?",
        "react_name": lambda n: f"{n}?ㅋㅋ 이름 딱 좋다! 느낌 온다ㅋㅋ" if n else "음... 익명으로 봐줄게ㅋㅋ",
        "ask_year": "생년월일도 알려줘! 몇 년생이야?",
        "react_birth": lambda z: f"오 {z}띠구나! 그럼 이제 진짜 신내림 받아볼게~",
        "button_label": "운세 보여줄게 🔮",
        "closing": "이거 완전 찐이니까 믿어봐ㅋㅋ 오늘 대박나길!",
    },
    "tarot_master": {
        "name": "신비로운 타로 마스터", "emoji": "🃏", "color": "#7b5ea7",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M15 100 C15 75 32 68 50 68 C68 68 85 75 85 100 Z" fill="#4b2e83"/>
            <path d="M38 100 C39 82 44 72 50 72 C56 72 61 82 62 100 Z" fill="#7b5ea7"/>
            <circle cx="50" cy="45" r="17" fill="#f0d5b8"/>
            <ellipse cx="44" cy="44" rx="2.2" ry="1.6" fill="#2b2b2b"/>
            <ellipse cx="56" cy="44" rx="2.2" ry="1.6" fill="#2b2b2b"/>
            <path d="M50 46 L49 51 Q50 52.2 51 51" stroke="#c9a87a" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M35 50 Q50 78 65 50 Q58 62 50 64 Q42 62 35 50 Z" fill="#e8e8e8"/>
            <path d="M45 55 Q50 58 55 55" stroke="#8a7050" stroke-width="1.4" fill="none" stroke-linecap="round"/>
            <path d="M38 40 Q43 36 47 39" stroke="#d8d8d8" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M53 39 Q57 36 62 40" stroke="#d8d8d8" stroke-width="2" fill="none" stroke-linecap="round"/>
            <path d="M28 34 Q50 -8 72 34 Q50 26 28 34 Z" fill="#4b2e83"/>
            <path d="M22 36 Q50 24 78 36 L74 42 Q50 32 26 42 Z" fill="#5e3a9e"/>
            <circle cx="50" cy="6" r="3" fill="#ffe066"/>
            <circle cx="40" cy="16" r="1.6" fill="#ffe066"/>
            <circle cx="60" cy="20" r="1.6" fill="#ffe066"/>
        </svg>''',
        "greeting": "카드가 당신을 기다리고 있습니다. 조용히 마음을 가라앉히고, 오늘의 운명을 들여다보겠습니다.",
        "ask_name": "성함을 말씀해주시겠습니까?",
        "react_name": lambda n: f"{n}... 좋은 이름입니다. 카드가 그 이름을 기억하겠군요." if n else "이름을 밝히지 않으셔도 좋습니다. 익명의 기운도 읽을 수 있으니까요.",
        "ask_year": "생년월일을 알려주십시오.",
        "react_birth": lambda z: f"{z}띠의 기운이군요. 카드를 준비하겠습니다.",
        "button_label": "카드를 펼치겠습니다 🃏",
        "closing": "카드는 거짓말을 하지 않습니다. 오늘 하루, 이 흐름을 마음에 새기시길.",
    },
    "grandma_shaman": {
        "name": "따뜻한 할머니 무당", "emoji": "🍵", "color": "#d98e5f",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#d98e5f"/>
            <path d="M32 100 C34 84 41 74 50 74 C59 74 66 84 68 100 Z" fill="#fff3e6"/>
            <rect x="44" y="56" width="12" height="14" rx="4" fill="#e8c39a"/>
            <circle cx="50" cy="45" r="18" fill="#e8c39a"/>
            <path d="M35 48 Q37 50 35 52" stroke="#c9a172" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M65 48 Q63 50 65 52" stroke="#c9a172" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M40 43 Q43 40 46 43" stroke="#3a2a1a" stroke-width="1.6" fill="none" stroke-linecap="round"/>
            <path d="M54 43 Q57 40 60 43" stroke="#3a2a1a" stroke-width="1.6" fill="none" stroke-linecap="round"/>
            <path d="M39 37 Q43 35 47 37" stroke="#c9c9c9" stroke-width="1.2" fill="none" stroke-linecap="round"/>
            <path d="M53 37 Q57 35 61 37" stroke="#c9c9c9" stroke-width="1.2" fill="none" stroke-linecap="round"/>
            <path d="M50 45 L49 50 Q50 51 51 50" stroke="#c9a172" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M42 54 Q50 60 58 54" stroke="#a8674a" stroke-width="2" fill="none" stroke-linecap="round"/>
            <circle cx="50" cy="20" r="9" fill="#e5e5e5"/>
            <path d="M32 30 Q50 10 68 30 Q66 20 50 16 Q34 20 32 30 Z" fill="#eaeaea"/>
            <line x1="38" y1="20" x2="62" y2="20" stroke="#c9a15a" stroke-width="2" stroke-linecap="round"/>
            <circle cx="62" cy="20" r="2" fill="#c9a15a"/>
        </svg>''',
        "greeting": "아이고 왔능가~ 할미가 오늘 하루 봐줄 텡께 이리 앉아보소.",
        "ask_name": "이름이 뭐라고 혔지?",
        "react_name": lambda n: f"{n}이여? 이름도 참 이쁘네." if n else "이름 안 갈쳐줘도 괜찮여~",
        "ask_year": "언제 태어났능가? 생년월일 좀 알려주소.",
        "react_birth": lambda z: f"{z}띠구먼. 잠깐만 기다려보소, 할미가 봐줄텡께.",
        "button_label": "어디 한번 봐줄게 🍵",
        "closing": "괜찮혀, 다 잘 될 거여. 오늘 하루도 애썼다잉.",
    },
    "baby_fox": {
        "name": "말랑말랑 아기여우", "emoji": "🦊", "color": "#ff9662",
        "greeting": "안녕! 나는 숲속 아기여우야! 오늘 네 운세, 내가 콕콕 짚어줄게!",
        "ask_name": "너 이름이 뭐야? 알려줘!",
        "react_name": lambda n: f"{n}! 이름 완전 예쁘다!!" if n else "이름 없어도 괜찮아! 그냥 봐줄게!",
        "ask_year": "언제 태어났어? 생년월일 알려줘!",
        "react_birth": lambda z: f"우와 {z}띠야?! 완전 신기하다! 잠깐만 기다려봐!",
        "button_label": "운세 찾아올게 🦊",
        "closing": "히히, 오늘도 럭키하게 보내! 나중에 또 놀러와~",
    },
    "fortune_master40": {
        "name": "40대 역술인", "emoji": "🎋", "color": "#4a6fa5",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#25324a"/>
            <path d="M32 100 C34 84 41 74 50 74 C59 74 66 84 68 100 Z" fill="#f2f2f2"/>
            <rect x="44" y="56" width="12" height="14" rx="4" fill="#e8c9a8"/>
            <circle cx="50" cy="45" r="18" fill="#e8c9a8"/>
            <ellipse cx="43" cy="44" rx="2.2" ry="1.6" fill="#1a1a1a"/>
            <ellipse cx="57" cy="44" rx="2.2" ry="1.6" fill="#1a1a1a"/>
            <path d="M38 39 L48 38" stroke="#1a1a1a" stroke-width="1.4" stroke-linecap="round"/>
            <path d="M52 38 L62 39" stroke="#1a1a1a" stroke-width="1.4" stroke-linecap="round"/>
            <path d="M50 45 L49 51 Q50 52.2 51 51" stroke="#c9a172" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M42 54 Q50 51 58 54 Q50 57 42 54 Z" fill="#3a3a3a"/>
            <path d="M45 58 Q50 60 55 58" stroke="#8a5a3a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
            <rect x="42" y="6" width="16" height="16" rx="3" fill="#111111"/>
            <ellipse cx="50" cy="24" rx="26" ry="6" fill="#111111"/>
        </svg>''',
        "greeting": "어서 오십시오. 사주를 오래 봐온 사람으로서, 오늘 하루의 기운을 차분히 짚어드리겠습니다.",
        "ask_name": "성함이 어떻게 되십니까?",
        "react_name": lambda n: f"{n} 님이시군요. 잘 알겠습니다." if n else "성함은 말씀 안 하셔도 무방합니다.",
        "ask_year": "생년월일을 말씀해주시죠.",
        "react_birth": lambda z: f"{z}띠시군요. 사주를 짚어보겠습니다.",
        "button_label": "사주를 풀어드리겠습니다 🎋",
        "closing": "오늘 말씀드린 내용, 참고 삼아 하루를 보내시면 좋겠습니다.",
    },
    "joseon_monk": {
        "name": "조선시대 승려", "emoji": "📿", "color": "#8a7355",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#7a6248"/>
            <path d="M50 68 C60 68 66 76 66 88 L66 100 L34 100 L34 84 C34 76 42 68 50 68 Z" fill="#c9b896"/>
            <rect x="44" y="56" width="12" height="14" rx="4" fill="#e8c9a8"/>
            <circle cx="50" cy="42" r="19" fill="#e8c9a8"/>
            <path d="M40 42 Q43 44 46 42" stroke="#3a2a1a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
            <path d="M54 42 Q57 44 60 42" stroke="#3a2a1a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
            <path d="M50 43 L49 48 Q50 49.2 51 48" stroke="#c9a172" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M43 52 Q50 56 57 52" stroke="#8a5a3a" stroke-width="1.6" fill="none" stroke-linecap="round"/>
            <circle cx="50" cy="28" r="1.4" fill="#c0392b"/>
            <g fill="#c9a15a" stroke="#5a3a1a" stroke-width="1">
                <circle cx="38" cy="72" r="2.4"/>
                <circle cx="44" cy="76" r="2.4"/>
                <circle cx="50" cy="78" r="2.4"/>
                <circle cx="56" cy="76" r="2.4"/>
                <circle cx="62" cy="72" r="2.4"/>
            </g>
        </svg>''',
        "greeting": "나무관세음보살. 그대의 발걸음이 이곳에 닿은 것도 인연이니, 오늘의 기운을 살펴보겠소.",
        "ask_name": "그대의 이름은 무엇이오?",
        "react_name": lambda n: f"{n}이라, 좋은 이름을 가지셨소." if n else "이름을 밝히지 않아도 무방하오.",
        "ask_year": "태어난 해와 날을 알려주시오.",
        "react_birth": lambda z: f"{z}띠이시구려. 잠시 기다려보시오.",
        "button_label": "기운을 살펴보겠소 📿",
        "closing": "모든 것은 마음먹기에 달렸소. 부디 평안한 하루 되시오.",
    },
    "fox_spirit": {
        "name": "여우신령", "emoji": "🌙", "color": "#9b59b6",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 100 C12 76 30 66 50 66 C70 66 88 76 88 100 Z" fill="#3d2a5c"/>
            <path d="M30 100 C32 82 40 72 50 72 C60 72 68 82 70 100 Z" fill="#c9b8e8"/>
            <path d="M28 24 L36 4 L44 26 Z" fill="#f2eee8"/>
            <path d="M31 22 L36 10 L40 24 Z" fill="#e8b3c9"/>
            <path d="M72 24 L64 4 L56 26 Z" fill="#f2eee8"/>
            <path d="M69 22 L64 10 L60 24 Z" fill="#e8b3c9"/>
            <rect x="44" y="55" width="12" height="14" rx="4" fill="#f5ece0"/>
            <circle cx="50" cy="43" r="19" fill="#f5ece0"/>
            <path d="M27 38 Q22 66 30 84 L36 80 Q29 60 30 40 Z" fill="#e8e4f0"/>
            <path d="M73 38 Q78 66 70 84 L64 80 Q71 60 70 40 Z" fill="#e8e4f0"/>
            <path d="M29 32 Q50 14 71 32 Q68 22 50 18 Q32 22 29 32 Z" fill="#e8e4f0"/>
            <path d="M39 42 Q43 39 47 42 Q43 44 39 42 Z" fill="#9b59b6"/>
            <path d="M53 42 Q57 39 61 42 Q57 44 53 42 Z" fill="#9b59b6"/>
            <path d="M50 44 L49 49 Q50 50.2 51 49" stroke="#d8c0a8" stroke-width="1" fill="none" stroke-linecap="round"/>
            <path d="M45 53 Q50 56 55 53" stroke="#8a5a7a" stroke-width="1.4" fill="none" stroke-linecap="round"/>
            <path d="M50 12 A4 4 0 1 0 50 4 A3 3 0 1 1 50 12 Z" fill="#ffe066"/>
        </svg>''',
        "greeting": "안녕하신가, 인간이여. 나는 오랜 세월을 살아온 여우니라. 그대의 오늘을 잠시 들여다보겠네.",
        "ask_name": "그대의 이름을 말해보게.",
        "react_name": lambda n: f"{n}이라... 기억해두겠네." if n else "이름은 중요치 않네, 그저 기운을 보면 되니.",
        "ask_year": "태어난 해와 날을 알려주게.",
        "react_birth": lambda z: f"{z}띠의 기운을 타고났군. 곧 알려주겠네.",
        "button_label": "기운을 읽어보겠네 🌙",
        "closing": "오늘의 이야기는 여기까지. 부디 지혜롭게 하루를 걸으시게.",
    },
    "cat_sage": {
        "name": "고양이도사", "emoji": "🐱", "color": "#f4a460",
        "greeting": "냥. 오늘 운세가 궁금해서 온 게냥? 뭐, 어쩔 수 없이 봐주지 냥.",
        "ask_name": "이름이 뭐냥?",
        "react_name": lambda n: f"{n}냥? 흥, 기억해두겠다냥." if n else "이름 안 갈쳐줘도 상관없다냥.",
        "ask_year": "생년월일 대라냥.",
        "react_birth": lambda z: f"{z}띠라니, 흥미롭다냥. 잠깐 기다리라냥.",
        "button_label": "봐주겠다냥 🐱",
        "closing": "흥, 도움 됐으면 다행이다냥. 다음에 또 오라냥.",
    },
    "mz_saju_girl": {
        "name": "MZ 사주소녀", "emoji": "✨", "color": "#ff6b9d",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#ff6b9d"/>
            <path d="M32 100 C34 84 41 74 50 74 C59 74 66 84 68 100 Z" fill="#fff0f5"/>
            <circle cx="36" cy="78" r="2" fill="#ffffff"/>
            <circle cx="64" cy="78" r="2" fill="#ffffff"/>
            <rect x="44" y="55" width="12" height="14" rx="4" fill="#ffdbac"/>
            <circle cx="50" cy="43" r="19" fill="#ffdbac"/>
            <path d="M28 36 Q50 16 72 36 Q70 24 50 20 Q30 24 28 36 Z" fill="#3a2a1a"/>
            <path d="M27 38 Q24 54 29 62 L34 58 Q29 48 30 38 Z" fill="#3a2a1a"/>
            <path d="M73 38 Q76 54 71 62 L66 58 Q71 48 70 38 Z" fill="#3a2a1a"/>
            <circle cx="30" cy="18" r="6" fill="#3a2a1a"/>
            <circle cx="70" cy="18" r="6" fill="#3a2a1a"/>
            <circle cx="30" cy="18" r="6" fill="none" stroke="#ff6b9d" stroke-width="2"/>
            <circle cx="70" cy="18" r="6" fill="none" stroke="#ff6b9d" stroke-width="2"/>
            <circle cx="42" cy="43" r="3.4" fill="#2b1810"/>
            <circle cx="58" cy="43" r="3.4" fill="#2b1810"/>
            <circle cx="43.4" cy="41.4" r="1" fill="#ffffff"/>
            <circle cx="59.4" cy="41.4" r="1" fill="#ffffff"/>
            <path d="M50 45 L49.3 49 Q50 50 50.7 49" stroke="#d8ac86" stroke-width="0.8" fill="none" stroke-linecap="round"/>
            <path d="M45 52 Q50 55 55 52" stroke="#c0526f" stroke-width="1.6" fill="none" stroke-linecap="round"/>
        </svg>''',
        "greeting": "얘들아 나 요즘 사주에 완전 꽂혀서 취미로 봐주고 있엉! 너두 궁금하지? ㅎㅎ",
        "ask_name": "이름 뭐야?? 궁금해!",
        "react_name": lambda n: f"{n}?? 완전 예쁜 이름이잖앙!!" if n else "이름 비밀이어도 오케이!",
        "ask_year": "생년월일 알려줘! 몇 년생이야?",
        "react_birth": lambda z: f"헐 {z}띠야? 완전 대박! 잠깐만!",
        "button_label": "운세 뽑아볼게 ✨",
        "closing": "완전 힐링됐지? 오늘도 화이팅!! 저장하고 또 놀러와~",
    },
    "saju_witch": {
        "name": "사주마녀", "emoji": "🕸", "color": "#5c2a5c",
        "avatar_svg": '''<svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <path d="M14 100 C14 78 30 68 50 68 C70 68 86 78 86 100 Z" fill="#2a1a2e"/>
            <path d="M32 100 C34 84 41 74 50 74 C59 74 66 84 68 100 Z" fill="#5c2a5c"/>
            <rect x="44" y="55" width="12" height="14" rx="4" fill="#f0dede"/>
            <circle cx="50" cy="43" r="18" fill="#f0dede"/>
            <path d="M39 42 Q43 39 47 42" stroke="#2a1a2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
            <path d="M53 42 Q57 39 61 42" stroke="#2a1a2e" stroke-width="1.8" fill="none" stroke-linecap="round"/>
            <ellipse cx="43" cy="43" rx="1.8" ry="2.4" fill="#5c2a5c"/>
            <ellipse cx="57" cy="43" rx="1.8" ry="2.4" fill="#5c2a5c"/>
            <path d="M50 44 L49.3 49 Q50 50 50.7 49" stroke="#c9a8a8" stroke-width="0.9" fill="none" stroke-linecap="round"/>
            <path d="M44 53 Q50 57 56 53 Q50 55 44 53 Z" fill="#4a1a2e"/>
            <path d="M28 30 Q50 -10 72 30 Q50 22 28 30 Z" fill="#2a1a2e"/>
            <ellipse cx="50" cy="32" rx="28" ry="6" fill="#2a1a2e"/>
            <rect x="38" y="24" width="24" height="5" fill="#5c2a5c"/>
            <circle cx="50" cy="26.5" r="2.4" fill="#c9a15a"/>
        </svg>''',
        "greeting": "후후... 마녀의 솥이 오늘도 부글부글 끓고 있군요. 당신의 운명을 한번 저어볼까요?",
        "ask_name": "이름을 말해보세요, 솥에 넣어드리죠.",
        "react_name": lambda n: f"{n}... 흥미로운 이름이군요. 솥에 넣어보죠." if n else "이름이 없어도, 마녀는 다 알아낸답니다.",
        "ask_year": "태어난 날짜를 말해보세요.",
        "react_birth": lambda z: f"{z}띠라... 재미있는 재료가 되겠어요.",
        "button_label": "운명을 저어보겠어요 🕸",
        "closing": "오늘 점괘는 여기까지예요. 방심은 금물, 재미는 필수랍니다.",
    },
}

ZODIAC_ORDER = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
ZODIAC_EMOJI = {
    "쥐": "🐭", "소": "🐮", "호랑이": "🐯", "토끼": "🐰", "용": "🐲", "뱀": "🐍",
    "말": "🐴", "양": "🐑", "원숭이": "🐵", "닭": "🐔", "개": "🐶", "돼지": "🐷",
}


def get_zodiac(year: int) -> str:
    return ZODIAC_ORDER[(year - 1924) % 12]


fortune_pool = {
    "총운": [
        "오전엔 다소 흐릿하던 흐름이 오후 들어 또렷해지며, 미뤄왔던 결정을 내리기 좋은 타이밍이 찾아옵니다.",
        "예상치 못한 곳에서 도움의 손길이 나타나 막혀있던 일이 뜻밖에 술술 풀리는 하루가 될 것입니다.",
        "평소보다 판단력이 예리해지는 날이라, 중요한 선택 앞에서는 직감을 믿어도 좋습니다.",
        "작은 실수 하나가 눈에 밟힐 수 있지만, 크게 번지지 않으니 너무 담아두지 않아도 됩니다.",
        "새로운 시작보다는 지금까지 해온 일을 마무리 짓는 데 집중하면 성취감을 크게 느낄 수 있습니다.",
        "주변 사람의 조언 한마디가 생각보다 큰 힌트가 되는 날이니 흘려듣지 마세요.",
    ],
    "애정운": [
        "솔직한 대화 한 번이 오해를 눈 녹듯 풀어주는 하루입니다. 먼저 다가가면 반응이 좋습니다.",
        "혼자인 분이라면 우연한 만남에서 호감이 싹틀 가능성이 있으니 평소 안 가던 장소도 가볍게 들러보세요.",
        "연인이나 배우자와는 사소한 것으로 다툴 수 있으니, 말투를 조금만 더 부드럽게 다듬는 게 좋습니다.",
        "표현하지 못했던 마음을 오늘은 용기 내어 말해보면 예상보다 좋은 반응을 얻을 수 있어요.",
        "관계에 있어 여유를 갖는 게 오늘의 핵심입니다. 답을 재촉하지 말고 흐름에 맡겨보세요.",
        "그리웠던 사람에게서 먼저 연락이 올 수 있는 날이니 휴대폰을 자주 확인해보는 것도 나쁘지 않습니다.",
    ],
    "재물운": [
        "생각지도 못한 곳에서 작은 수입이 들어오지만, 그만큼 지출도 늘어날 수 있으니 균형을 잡아야 합니다.",
        "충동적인 소비보다는 계획된 지출이 더 큰 만족을 주는 하루입니다.",
        "투자나 큰 결정은 오늘보다 며칠 뒤로 미루는 것이 유리해 보입니다.",
        "저축이나 절약 계획을 세우기에 좋은 흐름입니다. 작은 습관 하나가 큰 차이를 만듭니다.",
        "동료나 지인과의 금전 거래는 이번 주만큼은 신중하게 접근하는 것이 좋겠습니다.",
        "오늘 쓴 돈이 훗날 더 큰 기회로 돌아올 수 있으니, 자기계발에 대한 투자는 긍정적으로 볼 만합니다.",
    ],
    "건강운": [
        "몸보다 마음이 먼저 지쳐있을 수 있는 날입니다. 짧게라도 산책하며 머리를 식혀보세요.",
        "수면의 질이 컨디션을 크게 좌우하는 하루입니다. 평소보다 30분만 일찍 잠자리에 들어보세요.",
        "목이나 어깨 쪽에 긴장이 쌓이기 쉬우니 틈틈이 스트레칭을 해주는 게 좋습니다.",
        "과식이나 카페인 과다 섭취를 조심해야 하는 날입니다. 물을 평소보다 자주 마셔주세요.",
        "몸이 보내는 신호를 무시하지 마세요. 평소보다 피곤함을 느낀다면 무리한 일정은 하루 미루는 게 좋습니다.",
        "가벼운 운동이 오늘따라 유난히 효과가 좋은 날이니, 짧게라도 몸을 움직여보세요.",
    ],
    "인간관계운": [
        "무심코 던진 말 한마디가 예상보다 큰 힘이 되어 상대에게 전해지는 하루입니다.",
        "그룹 안에서 중재자 역할을 맡게 될 수 있는데, 한쪽 편을 들기보다 중립을 지키는 것이 좋습니다.",
        "오랜만에 연락한 사람과의 대화가 뜻밖의 좋은 기회로 이어질 수 있습니다.",
        "새로운 사람과의 만남에서 좋은 인상을 남기기 좋은 날이니, 먼저 인사를 건네보세요.",
        "누군가의 부탁을 거절해야 할 상황이 생기면, 돌려 말하기보다 솔직하게 이유를 설명하는 편이 관계에 도움이 됩니다.",
        "혼자만의 시간을 원한다면 무리해서 약속을 잡기보다 오늘은 스스로를 위한 시간을 가져도 좋습니다.",
    ],
}

lucky_colors = ["보라색", "노란색", "초록색", "하늘색", "주황색", "와인색", "민트색", "골드"]
lucky_items = ["손목시계", "우산", "귀걸이", "머그컵", "볼펜", "향수", "노트", "스니커즈"]
lucky_numbers = list(range(1, 46))
lucky_times = ["오전 9시~11시", "정오~오후 1시", "오후 3시~5시", "저녁 7시~9시", "밤 9시 이후"]

# ------------------------------
# 상태 초기화
# ------------------------------
if "persona_id" not in st.session_state:
    st.session_state.persona_id = "mz_shaman"
if "step" not in st.session_state:
    st.session_state.step = 0
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "birth_year" not in st.session_state:
    st.session_state.birth_year = 1995
if "birth_month" not in st.session_state:
    st.session_state.birth_month = 1
if "birth_day" not in st.session_state:
    st.session_state.birth_day = 1

st.markdown('<div class="main-title">🔮 <span class="title-blue">운세</span> <span class="title-warm">캐릭터관</span></div>', unsafe_allow_html=True)

# 캐릭터 선택 (언제든 변경 가능 -> 바꾸면 처음부터 다시 시작)
new_persona_id = st.selectbox(
    "캐릭터 선택",
    list(PERSONAS.keys()),
    index=list(PERSONAS.keys()).index(st.session_state.persona_id),
    format_func=lambda k: f"{PERSONAS[k]['emoji']} {PERSONAS[k]['name']}",
    label_visibility="collapsed",
)
if new_persona_id != st.session_state.persona_id:
    st.session_state.persona_id = new_persona_id
    st.session_state.step = 0
    st.rerun()

persona = PERSONAS[st.session_state.persona_id]
avatar_content = persona.get("avatar_svg", persona["emoji"])

st.markdown(f"""
<div class="persona-avatar" style="background:{persona['color']}33; border:2px solid {persona['color']};">
    {avatar_content}
</div>
<div class="persona-name">{persona['name']}</div>
""", unsafe_allow_html=True)

TOTAL_STEPS = 5
dots = "".join("●" if i <= st.session_state.step else "○" for i in range(TOTAL_STEPS))
st.markdown(f'<div class="progress-dots">{dots}</div>', unsafe_allow_html=True)

# ------------------------------
# STEP 0: 인사
# ------------------------------
if st.session_state.step == 0:
    st.markdown(f'<div class="speech-bubble">{persona["greeting"]}</div>', unsafe_allow_html=True)
    if st.button("다음 →", use_container_width=True):
        st.session_state.step = 1
        st.rerun()

# ------------------------------
# STEP 1: 이름
# ------------------------------
elif st.session_state.step == 1:
    st.markdown(f'<div class="speech-bubble">{persona["ask_name"]}</div>', unsafe_allow_html=True)
    name_input = st.text_input("이름 (선택)", value=st.session_state.user_name, placeholder="예: 인수", label_visibility="collapsed")
    if st.button("다음 →", use_container_width=True):
        st.session_state.user_name = name_input
        st.session_state.step = 2
        st.rerun()

# ------------------------------
# STEP 2: 생년월일
# ------------------------------
elif st.session_state.step == 2:
    reaction = persona["react_name"](st.session_state.user_name)
    st.markdown(f'<div class="speech-bubble">{reaction}<br><br>{persona["ask_year"]}</div>', unsafe_allow_html=True)

    current_year = date.today().year
    year_options = list(range(current_year, 1929, -1))
    col_y, col_m, col_d = st.columns(3)
    with col_y:
        by = st.selectbox("연도", year_options, index=year_options.index(st.session_state.birth_year))
    with col_m:
        bm = st.selectbox("월", list(range(1, 13)), index=st.session_state.birth_month - 1)
    with col_d:
        bd = st.selectbox("일", list(range(1, 32)), index=st.session_state.birth_day - 1)

    if st.button("다음 →", use_container_width=True):
        try:
            date(by, bm, bd)
        except ValueError:
            st.warning("존재하지 않는 날짜예요. 다시 확인해주세요.")
            st.stop()
        st.session_state.birth_year = by
        st.session_state.birth_month = bm
        st.session_state.birth_day = bd
        st.session_state.step = 3
        st.rerun()

# ------------------------------
# STEP 3: 생년월일 확인 + 운세 뽑기 유도
# ------------------------------
elif st.session_state.step == 3:
    zodiac = get_zodiac(st.session_state.birth_year)
    reaction = persona["react_birth"](zodiac)
    st.markdown(
        f'<div class="speech-bubble">{ZODIAC_EMOJI[zodiac]} {reaction}</div>',
        unsafe_allow_html=True,
    )
    if st.button(persona["button_label"], use_container_width=True):
        st.session_state.step = 4
        st.rerun()

# ------------------------------
# STEP 4: 결과
# ------------------------------
elif st.session_state.step == 4:
    zodiac = get_zodiac(st.session_state.birth_year)
    birth_date = date(st.session_state.birth_year, st.session_state.birth_month, st.session_state.birth_day)
    seed_str = f"{st.session_state.persona_id}-{st.session_state.user_name}-{birth_date}-{date.today()}"
    random.seed(seed_str)

    total_luck = 0
    categories = ["총운", "애정운", "재물운", "건강운", "인간관계운"]
    for cat in categories:
        text = random.choice(fortune_pool[cat])
        score = random.randint(55, 98)
        total_luck += score
        st.markdown(f"""
        <div class="fortune-card">
            <div class="fortune-cat-title">{cat} · {score}점</div>
            <div class="fortune-cat-text">{text}</div>
        </div>
        """, unsafe_allow_html=True)

    avg_luck = round(total_luck / len(categories))
    color = random.choice(lucky_colors)
    item = random.choice(lucky_items)
    number = random.choice(lucky_numbers)
    time_range = random.choice(lucky_times)

    st.markdown(f"""
    <div class="lucky-box">
        <b>🍀 오늘의 평균 운세 지수: {avg_luck}점</b><br><br>
        행운의 색: <b>{color}</b> &nbsp;|&nbsp; 행운의 아이템: <b>{item}</b><br>
        행운의 숫자: <b>{number}</b> &nbsp;|&nbsp; 행운의 시간대: <b>{time_range}</b>
    </div>
    <div class="speech-bubble">{persona['emoji']} {persona['closing']}</div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<h3 style="padding-left:1.4em; text-indent:-1.4em; margin:0.5em 0;">'
        '🎁 오늘의 운세를 더 좋게 만들어줄 아이템</h3>',
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("쿠팡에서 행운템 보기 🛒", COUPANG_LINK, use_container_width=True)
    with col2:
        st.link_button("토스로 용돈 받기 💰", TOSS_LINK, use_container_width=True)

    st.caption("이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받을 수 있습니다.")

    share_url = "https://awesome-fortune.streamlit.app/"
    st.markdown("친구에게 공유하기")
    components.html(f"""
    <div style="display:flex; gap:8px; align-items:center; font-family: sans-serif;">
        <input id="shareUrlPersona" type="text" readonly value="{share_url}"
            style="flex:1; padding:10px 14px; border-radius:20px; border:1px solid rgba(255,255,255,0.2);
                   background:rgba(255,255,255,0.08); color:#f0eaff; font-size:0.9rem; outline:none;">
        <button onclick="copyPersonaLink(event)"
            style="padding:10px 18px; border-radius:20px; border:none;
                   background:linear-gradient(90deg,#f9d976,#c99df0); color:#1c1a1f;
                   font-weight:700; cursor:pointer; white-space:nowrap; font-size:0.9rem;">
            복사
        </button>
    </div>
    <script>
    function copyPersonaLink(event) {{
        var copyText = document.getElementById("shareUrlPersona");
        navigator.clipboard.writeText(copyText.value).then(function() {{
            var btn = event.target;
            var original = btn.innerText;
            btn.innerText = "복사됨!";
            setTimeout(function() {{ btn.innerText = original; }}, 1500);
        }});
    }}
    </script>
    """, height=60)

    if st.button("🔄 처음부터 다시하기", use_container_width=True):
        st.session_state.step = 0
        st.rerun()
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
    @keyframes fadeInUp {
        0% { opacity: 0; transform: translateY(14px) scale(0.96); }
        100% { opacity: 1; transform: translateY(0) scale(1); }
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
        animation: fadeInUp 0.6s ease-out;
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
        animation: fadeInUp 0.6s ease-out 0.1s both;
    }
    .avatar-showcase {
        position: relative;
        width: 130px;
        height: 158px;
        margin: 0 auto 6px auto;
        overflow: hidden;
    }
    .avatar-showcase-layer {
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        opacity: 0;
        animation-name: avatarShowcaseCycle;
        animation-timing-function: ease-in-out;
        animation-iteration-count: infinite;
    }
    .avatar-showcase-icon {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 3.6rem;
    }
    .avatar-showcase-icon svg {
        width: 72px;
        height: 72px;
    }
    .avatar-showcase-name {
        margin-top: 8px;
        font-size: 1rem;
        font-weight: 800;
        color: #f9d976;
    }
    .showcase-caption {
        text-align: center;
        color: #7dd490;
        font-size: 0.85rem;
        margin-bottom: 1rem;
    }
    @keyframes avatarShowcaseCycle {
        0% { opacity: 0; transform: translateX(140px); }
        2% { opacity: 1; transform: translateX(0); }
        8% { opacity: 1; transform: translateX(0); }
        10% { opacity: 0; transform: translateX(-140px); }
        100% { opacity: 0; transform: translateX(140px); }
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
        animation: fadeInUp 0.6s ease-out 0.2s both;
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
    @keyframes pulseButton {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.06); }
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
        -webkit-text-size-adjust: 100% !important;
        text-size-adjust: 100% !important;
        animation: pulseButton 1.6s ease-in-out infinite;
        display: inline-block;
    }
    div[data-testid="stLinkButton"] a * {
        font-size: 1.4rem !important;
        font-weight: 900 !important;
        color: #ffffff !important;
    }
    @media (max-width: 480px) {
        div[data-testid="stLinkButton"] a {
            font-size: 1.35rem !important;
            padding: 10px 8px !important;
            line-height: 1.3 !important;
        }
        div[data-testid="stLinkButton"] a * {
            font-size: 1.35rem !important;
        }
    }
    div[data-testid*="olumn"]:nth-of-type(2) div[data-testid="stLinkButton"] a {
        background: linear-gradient(180deg, #4dabff 0%, #0064ff 100%) !important;
        box-shadow:
            inset 0 1px 0 rgba(255,255,255,0.5),
            inset 0 -3px 6px rgba(0,0,0,0.25),
            0 6px 0 #0047b8,
            0 10px 18px rgba(0,0,0,0.45) !important;
        animation-delay: 0.4s;
    }
    div[data-testid*="olumn"]:nth-of-type(2) div[data-testid="stLinkButton"] a * {
        background: transparent !important;
        box-shadow: none !important;
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
        "greeting": [
            "안뇽! 나 지금 좀 신기 올라와서ㅋㅋ 몇 개만 물어볼게!",
            "어머 오늘 기운이 좀 쎄네? 잠깐 이리 와봐ㅋㅋ",
            "야 타이밍 좋다! 방금 신 내려왔는데ㅋㅋ 딱 물어봐",
            "오늘따라 촉이 남다른데? 몇 개만 체크해볼게ㅋㅋ",
            "안녕! 오늘 컨디션 최고야, 시원하게 봐줄게ㅋㅋ",
        ],
        "ask_name": "너 이름이 뭐야?",
        "react_name": lambda n, _w=[
            "{}?ㅋㅋ 이름 딱 좋다! 느낌 온다ㅋㅋ",
            "오 {} 이름 예쁘다ㅋㅋ 딱 기억해둘게",
            "{}구나! 이름 들으니까 더 잘 보일 것 같은데?ㅋㅋ",
            "{}... 좋아 딱 필 온다ㅋㅋ",
            "오케이 {}! 이제 진짜 시작해볼게ㅋㅋ",
        ], _e=[
            "음... 익명으로 봐줄게ㅋㅋ",
            "비밀이구나ㅋㅋ 그래도 다 보인다 나는",
            "이름 없어도 상관없어ㅋㅋ 기운으로 다 알아",
            "쿨하게 비밀 유지, 인정ㅋㅋ 계속 가볼게",
            "오케이 이름 패스ㅋㅋ 바로 다음으로 가자",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "생년월일도 알려줘! 몇 년생이야?",
        "react_birth": lambda z: f"오 {z}띠구나! 그럼 이제 진짜 신내림 받아볼게~",
        "button_label": "운세 보여줄게 🔮",
        "closing": [
            "이거 완전 찐이니까 믿어봐ㅋㅋ 오늘 대박나길!",
            "오늘 운세 어때, 소름 돋지 않아?ㅋㅋ 잘 챙겨!",
            "이 정도면 거의 신급 정확도야ㅋㅋ 오늘 화이팅!",
            "내 말 믿고 오늘 하루 자신있게 보내ㅋㅋ",
            "촉 진짜 좋았다 오늘ㅋㅋ 좋은 하루 보내!",
        ],
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
        "greeting": [
            "카드가 당신을 기다리고 있습니다. 조용히 마음을 가라앉히고, 오늘의 운명을 들여다보겠습니다.",
            "고요한 침묵 속에서 카드가 말을 걸어오는군요. 함께 들어보시죠.",
            "운명의 실이 오늘 당신 앞에 놓여 있습니다. 천천히 풀어드리겠습니다.",
            "우주의 기운이 심상치 않습니다. 카드로 그 흐름을 읽어드리죠.",
            "당신의 오늘은 이미 카드 안에 쓰여 있습니다. 함께 확인해볼까요.",
        ],
        "ask_name": "성함을 말씀해주시겠습니까?",
        "react_name": lambda n, _w=[
            "{}... 좋은 이름입니다. 카드가 그 이름을 기억하겠군요.",
            "{}님, 카드가 당신의 이름에 반응하고 있습니다.",
            "{}... 흥미로운 울림을 가진 이름이군요.",
            "그 이름, {}, 마음에 새겨두겠습니다.",
            "{}님이시군요. 카드를 이어서 펼치겠습니다.",
        ], _e=[
            "이름을 밝히지 않으셔도 좋습니다. 익명의 기운도 읽을 수 있으니까요.",
            "괜찮습니다. 이름 없이도 카드는 말을 합니다.",
            "익명이라도 카드 앞에서는 숨길 수 없죠.",
            "이름은 형식일 뿐, 본질은 카드가 압니다.",
            "말씀하지 않으셔도 무방합니다. 계속하시죠.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "생년월일을 알려주십시오.",
        "react_birth": lambda z: f"{z}띠의 기운이군요. 카드를 준비하겠습니다.",
        "button_label": "카드를 펼치겠습니다 🃏",
        "closing": [
            "카드는 거짓말을 하지 않습니다. 오늘 하루, 이 흐름을 마음에 새기시길.",
            "오늘 뽑힌 카드는 당신에게 필요한 메시지였습니다.",
            "카드가 전한 이야기, 마음 한켠에 담아두시길 바랍니다.",
            "운명은 정해진 것이 아니라 스스로 만들어가는 것임을 기억하시길.",
            "오늘의 카드는 여기까지입니다. 평안한 하루 되시길 바랍니다.",
        ],
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
        "greeting": [
            "아이고 왔능가~ 할미가 오늘 하루 봐줄 텡께 이리 앉아보소.",
            "어여 오소, 차 한잔 하면서 얘기 좀 해보드라고.",
            "오늘 얼굴이 훤하네~ 뭔 좋은 일 있으려나 한번 봐줄게.",
            "아이고 반갑네, 몸은 괜찮은겨? 오늘 기운 좀 짚어줄게.",
            "이리 와서 앉어, 할미가 다 봐줄 텡께 걱정 붙들어매소.",
        ],
        "ask_name": "이름이 뭐라고 혔지?",
        "react_name": lambda n, _w=[
            "{}이여? 이름도 참 이쁘네.",
            "오메, {}이구먼. 좋은 이름이여.",
            "{}이라... 듣기만 해도 정겹구먼.",
            "{}이구나, 할미가 기억해둘게.",
            "이름이 {}이라 그런가 얼굴이 훤하네.",
        ], _e=[
            "이름 안 갈쳐줘도 괜찮여~",
            "허허, 비밀이구먼. 그래도 다 봐줄겨.",
            "이름 없어도 상관없어, 다 보이는겨.",
            "괜찮혀, 얼굴만 봐도 다 아는겨.",
            "쑥스러운가벼, 그럼 그냥 넘어가세.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "언제 태어났능가? 생년월일 좀 알려주소.",
        "react_birth": lambda z: f"{z}띠구먼. 잠깐만 기다려보소, 할미가 봐줄텡께.",
        "button_label": "어디 한번 봐줄게 🍵",
        "closing": [
            "괜찮혀, 다 잘 될 거여. 오늘 하루도 애썼다잉.",
            "너무 걱정 말어, 다 지나가는 겨. 밥 잘 챙겨묵고.",
            "오늘 하루도 욕봤다잉, 따신 밥 한 끼 챙겨묵어.",
            "다 괜찮을 텡께 어깨 펴고 다녀, 알겄지?",
            "할미 말 믿고 오늘 하루 웃으면서 지내소.",
        ],
    },
    "baby_fox": {
        "name": "말랑말랑 아기여우", "emoji": "🦊", "color": "#ff9662",
        "greeting": [
            "안녕! 나는 숲속 아기여우야! 오늘 네 운세, 내가 콕콕 짚어줄게!",
            "짜잔! 아기여우 등장! 오늘 하루 궁금하지?!",
            "안녕안녕! 오늘따라 코가 간질간질해, 뭔가 좋은 일 있나봐!",
            "헤헤 나 방금 낮잠 자다 왔어! 이제 운세 봐줄 준비 완료!",
            "킁킁, 좋은 냄새가 나! 오늘 운 좋은 냄새인가?!",
        ],
        "ask_name": "너 이름이 뭐야? 알려줘!",
        "react_name": lambda n, _w=[
            "{}! 이름 완전 예쁘다!!",
            "오 {}! 딱 기억할게!!",
            "{}구나! 좋은 이름이야, 헤헤!",
            "우와 {}! 처음 듣는데 완전 좋아!",
            "{}! 이제부터 그렇게 불러줄게!",
        ], _e=[
            "이름 없어도 괜찮아! 그냥 봐줄게!",
            "비밀이야?! 그래도 좋아, 계속 가자!",
            "괜찮아 괜찮아! 이름 몰라도 다 보여!",
            "쑥스러웠구나! 그럼 바로 다음으로!",
            "오케이 비밀 지켜줄게! 시작하자!",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "언제 태어났어? 생년월일 알려줘!",
        "react_birth": lambda z: f"우와 {z}띠야?! 완전 신기하다! 잠깐만 기다려봐!",
        "button_label": "운세 찾아올게 🦊",
        "closing": [
            "히히, 오늘도 럭키하게 보내! 나중에 또 놀러와~",
            "오늘 하루도 콩닥콩닥 기대되지?! 잘 보내고 와!",
            "나중에 또 놀러와, 간식 준비해둘게!",
            "오늘 완전 좋은 일만 가득할 거야, 두고봐!",
            "헤헤 오늘도 폴짝폴짝 기분 좋게 보내!",
        ],
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
        "greeting": [
            "어서 오십시오. 사주를 오래 봐온 사람으로서, 오늘 하루의 기운을 차분히 짚어드리겠습니다.",
            "반갑습니다. 오늘도 성심껏 봐드리겠습니다.",
            "앉으시죠. 사주는 정직합니다, 있는 그대로 말씀드리겠습니다.",
            "오랜 경험으로 오늘 기운을 정확히 짚어드리겠습니다.",
            "어서 오세요. 편하게 여쭤보시면 차근차근 풀어드리겠습니다.",
        ],
        "ask_name": "성함이 어떻게 되십니까?",
        "react_name": lambda n, _w=[
            "{} 님이시군요. 잘 알겠습니다.",
            "{} 님, 반갑습니다.",
            "성함이 {}시군요. 기억해두겠습니다.",
            "{} 님, 편하게 봐드리겠습니다.",
            "{} 님이시군요. 이어서 진행하겠습니다.",
        ], _e=[
            "성함은 말씀 안 하셔도 무방합니다.",
            "괜찮습니다, 성함 없이도 봐드릴 수 있습니다.",
            "말씀 안 하셔도 됩니다. 계속하시죠.",
            "성함이 없어도 사주는 정직합니다.",
            "알겠습니다, 그대로 진행하겠습니다.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "생년월일을 말씀해주시죠.",
        "react_birth": lambda z: f"{z}띠시군요. 사주를 짚어보겠습니다.",
        "button_label": "사주를 풀어드리겠습니다 🎋",
        "closing": [
            "오늘 말씀드린 내용, 참고 삼아 하루를 보내시면 좋겠습니다.",
            "사주는 절대적인 것이 아니니, 참고만 하시길 바랍니다.",
            "오늘 하루, 마음의 여유를 가지고 지내시길 바랍니다.",
            "필요하실 때 언제든 다시 찾아주십시오.",
            "말씀드린 내용 새겨두시고, 평안한 하루 되십시오.",
        ],
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
        "greeting": [
            "나무관세음보살. 그대의 발걸음이 이곳에 닿은 것도 인연이니, 오늘의 기운을 살펴보겠소.",
            "먼 길 오셨구려. 잠시 앉아 마음을 가다듬으시오.",
            "오늘 하늘의 기운이 예사롭지 않소. 함께 살펴봅시다.",
            "인연이란 참으로 신묘한 것이오. 그대의 오늘을 들여다보겠소.",
            "나무아미타불. 조급해 마시고 천천히 여쭤보시오.",
        ],
        "ask_name": "그대의 이름은 무엇이오?",
        "react_name": lambda n, _w=[
            "{}이라, 좋은 이름을 가지셨소.",
            "{}이시구려. 인연이 새삼 깊게 느껴지오.",
            "{}... 마음에 새겨두겠소.",
            "{}이라니, 참으로 좋은 이름이오.",
            "{}이시군요. 계속 살펴보겠소.",
        ], _e=[
            "이름을 밝히지 않아도 무방하오.",
            "괜찮소, 이름 없이도 인연은 이어지는 법이오.",
            "말하지 않아도 좋소. 계속하겠소.",
            "이름은 그저 형식일 뿐이오.",
            "번거로우면 넘어가도 좋소.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "태어난 해와 날을 알려주시오.",
        "react_birth": lambda z: f"{z}띠이시구려. 잠시 기다려보시오.",
        "button_label": "기운을 살펴보겠소 📿",
        "closing": [
            "모든 것은 마음먹기에 달렸소. 부디 평안한 하루 되시오.",
            "나무관세음보살. 오늘 하루도 평안하시길 바라오.",
            "괴로움도 지나가는 것이니, 마음을 편히 가지시오.",
            "오늘 들은 이야기, 마음 한구석에 담아두시오.",
            "부디 자비로운 마음으로 하루를 보내시길 바라오.",
        ],
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
        "greeting": [
            "안녕하신가, 인간이여. 나는 오랜 세월을 살아온 여우니라. 그대의 오늘을 잠시 들여다보겠네.",
            "달빛이 유난히 밝은 밤이군. 그대의 기운을 한번 살펴볼까.",
            "오랜만에 흥미로운 손님이 왔구나. 이리 가까이 오게.",
            "그대에게서 묘한 기운이 느껴지는군. 잠시 들여다보겠네.",
            "천 년을 살아도 인간의 운명은 늘 새롭구나. 오늘을 봐주지.",
        ],
        "ask_name": "그대의 이름을 말해보게.",
        "react_name": lambda n, _w=[
            "{}이라... 기억해두겠네.",
            "{}, 그 이름 마음에 드는군.",
            "{}이시구나. 흥미로운 이름이군.",
            "{}... 오래도록 기억할 이름이군.",
            "{}이라 하였는가. 좋다.",
        ], _e=[
            "이름은 중요치 않네, 그저 기운을 보면 되니.",
            "괜찮네, 이름 없이도 다 보인다네.",
            "숨겨도 좋네, 여우의 눈은 속일 수 없으니.",
            "말하지 않아도 상관없네.",
            "그래, 비밀로 남겨두게.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "태어난 해와 날을 알려주게.",
        "react_birth": lambda z: f"{z}띠의 기운을 타고났군. 곧 알려주겠네.",
        "button_label": "기운을 읽어보겠네 🌙",
        "closing": [
            "오늘의 이야기는 여기까지. 부디 지혜롭게 하루를 걸으시게.",
            "천 년의 지혜를 담아 전했으니, 새겨듣게나.",
            "오늘 밤 달빛 아래 이 이야기를 다시 떠올려보게.",
            "그대의 앞날에 좋은 기운이 함께하길 바라네.",
            "다음에 또 궁금한 것이 있으면 찾아오게나.",
        ],
    },
    "cat_sage": {
        "name": "고양이도사", "emoji": "🐱", "color": "#f4a460",
        "greeting": [
            "냥. 오늘 운세가 궁금해서 온 게냥? 뭐, 어쩔 수 없이 봐주지 냥.",
            "흥, 또 왔구나냥. 오늘은 특별히 봐준다냥.",
            "하암... 낮잠 자다 왔다냥. 뭐 궁금한 게 있다고?",
            "너로구나냥. 마침 심심했는데 잘 왔다냥.",
            "냥? 오늘따라 기운이 요상하다냥. 한번 볼까.",
        ],
        "ask_name": "이름이 뭐냥?",
        "react_name": lambda n, _w=[
            "{}냥? 흥, 기억해두겠다냥.",
            "오 {}냥, 나쁘지 않은 이름이다냥.",
            "{}이라고 했냥? 좋다냥.",
            "흥, {}구나. 기억해주겠다냥.",
            "{}냥... 특별히 기억해두마.",
        ], _e=[
            "이름 안 갈쳐줘도 상관없다냥.",
            "흥, 비밀이구나냥. 그래도 상관없다냥.",
            "말 안 해도 다 안다냥.",
            "쑥스러운 게냥? 그럼 넘어가자냥.",
            "괜찮다냥, 이름 없이도 봐준다냥.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "생년월일 대라냥.",
        "react_birth": lambda z: f"{z}띠라니, 흥미롭다냥. 잠깐 기다리라냥.",
        "button_label": "봐주겠다냥 🐱",
        "closing": [
            "흥, 도움 됐으면 다행이다냥. 다음에 또 오라냥.",
            "냥, 오늘은 이 정도로 봐준다. 잘 챙기라냥.",
            "흥 별거 아니었다냥, 어서 가서 하루 잘 보내라냥.",
            "다음에 또 오면 특별히 더 잘 봐주겠다냥.",
            "냥냥, 오늘 운세 나쁘지 않으니 안심하라냥.",
        ],
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
        "greeting": [
            "얘들아 나 요즘 사주에 완전 꽂혀서 취미로 봐주고 있엉! 너두 궁금하지? ㅎㅎ",
            "오 마침 잘 왔다! 나 방금 사주 공부하고 왔거든ㅎㅎ",
            "얘 오늘 촉 미쳤어 진짜, 빨리 물어봐!",
            "안뇽! 오늘 운세 완전 기대되지 않아? 궁금하지 나도!",
            "짜잔~ 등장! 오늘도 재미로 한번 봐줄게!",
        ],
        "ask_name": "이름 뭐야?? 궁금해!",
        "react_name": lambda n, _w=[
            "{}?? 완전 예쁜 이름이잖앙!!",
            "오 {}! 진짜 잘 어울린다!!",
            "{}구나! 완전 기억할게!!",
            "대박 {}! 이름 센스 좋다!!",
            "{}! 이제부터 그렇게 불러줄게!!",
        ], _e=[
            "이름 비밀이어도 오케이!",
            "괜찮아! 이름 없어도 완전 오케이!",
            "쿨하다 쿨해! 비밀 지켜줄게!",
            "오케이오케이! 바로 다음으로 가자!",
            "비밀이어도 상관없엉! 계속 가보자!",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "생년월일 알려줘! 몇 년생이야?",
        "react_birth": lambda z: f"헐 {z}띠야? 완전 대박! 잠깐만!",
        "button_label": "운세 뽑아볼게 ✨",
        "closing": [
            "완전 힐링됐지? 오늘도 화이팅!! 저장하고 또 놀러와~",
            "오늘 운세 완전 대박이지 않아?! 좋은 하루 보내!",
            "얘 진짜 오늘 운 좋은 듯, 화이팅해!!",
            "완전 만족스럽지?ㅎㅎ 다음에 또 봐주러 올게!",
            "오늘 하루도 완전 럭키하게 보내, 알겠지?!",
        ],
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
        "greeting": [
            "후후... 마녀의 솥이 오늘도 부글부글 끓고 있군요. 당신의 운명을 한번 저어볼까요?",
            "오늘 밤 별자리가 유난히 수상하군요. 함께 들여다보죠.",
            "흥미로운 손님이 오셨네요. 솥 안의 재료들이 벌써 반응하고 있어요.",
            "당신의 운명, 오늘은 어떤 색일까요? 함께 확인해보죠.",
            "마녀의 감이 말하길, 오늘은 특별한 날이라는군요.",
        ],
        "ask_name": "이름을 말해보세요, 솥에 넣어드리죠.",
        "react_name": lambda n, _w=[
            "{}... 흥미로운 이름이군요. 솥에 넣어보죠.",
            "{}, 그 이름 마음에 드는군요.",
            "{}이라... 재미있는 이름이네요.",
            "{}, 기억해두죠. 계속 진행하겠어요.",
            "{}... 솥이 그 이름에 반응하네요.",
        ], _e=[
            "이름이 없어도, 마녀는 다 알아낸답니다.",
            "괜찮아요, 비밀은 마녀의 특기니까요.",
            "숨겨도 소용없어요, 하지만 좋아요.",
            "말하지 않아도 상관없어요, 계속하죠.",
            "흥미롭군요, 비밀스러운 손님이네요.",
        ]: random.choice(_w).format(n) if n else random.choice(_e),
        "ask_year": "태어난 날짜를 말해보세요.",
        "react_birth": lambda z: f"{z}띠라... 재미있는 재료가 되겠어요.",
        "button_label": "운명을 저어보겠어요 🕸",
        "closing": [
            "오늘 점괘는 여기까지예요. 방심은 금물, 재미는 필수랍니다.",
            "솥 안의 재료들이 모두 소진됐네요, 오늘은 여기까지예요.",
            "운명이란 재미있는 장난 같은 거죠. 오늘도 즐기세요.",
            "다음에 또 저의 솥을 찾아주시길 바랄게요.",
            "후후, 오늘 점괘 마음에 드셨길 바라요.",
        ],
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
        "아침에 무심코 튼 라디오에서 흘러나온 노래 한 소절이, 하루 종일 발걸음을 가볍게 만들어줄 거예요. 사소한 우연이 큰 힌트가 되는 날입니다.",
        "엘리베이터에서 마주친 낯선 이의 미소 하나가, 오늘 하루의 분위기를 결정짓습니다. 먼저 웃어 보이는 쪽이 이득이에요.",
        "책상 서랍을 정리하다 우연히 발견한 메모 한 장이, 잊고 있던 중요한 약속이나 아이디어를 떠올리게 할 수 있어요.",
        "평소와 다른 길로 돌아가 본 선택이, 예상 못한 좋은 풍경이나 기회로 이어지는 하루입니다. 가끔은 계획을 벗어나 보세요.",
        "점심시간, 동료가 툭 던진 한마디가 생각보다 오래 마음에 남을 거예요. 그 말 속에 오늘의 실마리가 숨어 있습니다.",
        "저녁 무렵 하루를 되돌아보면, 사소했던 순간 하나가 실은 오늘 가장 값진 장면이었다는 걸 깨닫게 될 거예요.",
    ],
    "애정운": [
        "카톡 창을 켰다 닫았다 망설이던 그 메시지, 오늘은 그냥 보내보세요. 예상보다 빠르고 반가운 답이 올 거예요.",
        "우연히 흘러나온 노래 가사가 마음에 콕 박히는 순간, 누군가의 얼굴이 떠오를 수 있어요. 그 감정을 무시하지 마세요.",
        "다투고 나서 먼저 연락하기 애매했던 그 사람에게서, 뜻밖에 안부 인사가 올 수 있는 하루입니다.",
        "새로운 사람과의 대화 중 예상 못한 공통점을 발견하고, 급속도로 가까워질 수 있는 기회가 찾아와요.",
        "괜히 서운했던 마음, 오늘 솔직하게 한마디만 꺼내면 생각보다 쉽게 풀릴 거예요. 타이밍은 지금입니다.",
        "혼자 보내는 저녁이 오히려 편안하게 느껴지는 날이에요. 조급해하지 않아도 괜찮은 시기입니다.",
    ],
    "재물운": [
        "장바구니에 오래 담아뒀던 물건, 결제 버튼을 누르기 전에 한 번 더 검색해보세요. 예상 밖의 할인 정보를 발견할 수 있어요.",
        "무심코 확인한 계좌에서 잊고 있던 자투리 포인트나 캐시백을 발견하고 기분 좋아질 수 있는 하루예요.",
        "동료나 친구와의 밥값 계산에서, 먼저 계산하려던 마음이 생각보다 더 큰 보답으로 돌아올 수 있는 날입니다.",
        "충동적으로 지르고 싶은 소비 욕구가 스멀스멀 올라오는 날이에요. 장바구니에 담아두고 하루만 묵혀두세요.",
        "예상치 못한 곳에서 작은 용돈이나 환급금이 들어올 수 있어요, 다만 그만큼 나가는 돈도 있으니 균형이 필요합니다.",
        "미뤄뒀던 가계부 정리나 재테크 공부를 오늘 시작해보면, 생각보다 큰 동기부여가 될 거예요.",
    ],
    "건강운": [
        "평소보다 한 정거장 일찍 내려 걸어보는 것만으로도, 오늘 하루의 컨디션이 눈에 띄게 달라질 거예요.",
        "커피 대신 물 한 잔을 먼저 마셔보세요. 오늘따라 몸이 유난히 그 작은 습관에 반응할 거예요.",
        "어깨와 목 뒤가 뻐근하게 느껴진다면, 잠깐의 스트레칭이 오늘 컨디션의 열쇠가 될 수 있어요.",
        "야식의 유혹이 유난히 강한 날이에요. 대신 따뜻한 차 한 잔으로 대체해보면 다음 날이 훨씬 가뿐할 거예요.",
        "충분히 잤다고 생각해도 피로가 남아있다면, 몸이 보내는 신호를 무시하지 말고 오늘은 일찍 쉬어주세요.",
        "가벼운 산책이나 스트레칭 한 번이, 오늘따라 유난히 머리를 맑게 해줄 거예요.",
    ],
    "인간관계운": [
        "단체 채팅방에서 눈에 띄지 않던 메시지 하나에 답장을 해주면, 뜻밖에 좋은 인상을 남기는 하루가 될 거예요.",
        "누군가의 부탁을 거절해야 하는 상황이 생긴다면, 돌려 말하기보다 솔직하게 이유를 말하는 편이 관계에 오히려 도움이 됩니다.",
        "오랜만에 연락한 사람과의 대화가, 예상보다 훨씬 반갑고 즐거운 시간으로 이어질 수 있어요.",
        "회의나 모임에서 무심코 던진 의견이, 생각보다 좋은 반응을 얻으며 존재감을 드러내는 하루가 될 거예요.",
        "괜히 눈치 보였던 사람과의 어색함이, 사소한 계기로 자연스럽게 풀리는 날입니다.",
        "혼자만의 시간이 필요하다면, 무리해서 약속을 잡기보다 오늘은 스스로를 챙기는 편이 더 나은 선택이에요.",
    ],
}

# ------------------------------
# 캐릭터별 전용 운세 소재
# 캐릭터 컨셉(촉/기운, 카드, 달빛, 냥체 등)에 맞춰 각각 다른 스토리로 작성
# ------------------------------
PERSONA_FORTUNE = {
    "mz_shaman": {
        "총운": [
            "아까 눈 뜨자마자 핸드폰 알림 하나에 괜히 심쿵했지? 그거 오늘 하루 시작을 알리는 신호였어. 아침엔 좀 붕 뜬 기분이어도 오후 되면 갑자기 필 꽂히는 순간이 올 거야. 그때 놓치지 말고 딱 잡아, 오늘 흐름 완전 네 편이거든.",
            "누가 갑자기 도와준다고 나서면 살짝 의심부터 들 수도 있는데, 오늘은 그냥 믿어봐. 신기하게 막혀있던 일이 스르륵 풀리는 타이밍이 온다니까. 촉 진짜 좋은 날이야, 이런 날 흔치 않아.",
        ],
        "애정운": [
            "그 사람 프사 몇 번이나 들락날락했지? 오늘은 진짜 그냥 눌러봐, 메시지 하나. 촉이 말해주는데 예상보다 빨리, 그리고 훨씬 반갑게 답 올 거야. 이런 타이밍 자주 안 온다.",
            "혼자인 사람들, 오늘 갑자기 낯선 자리 가고 싶어질 수도 있어. 그 촉 무시하지 마, 거기서 스치는 인연 하나가 예사롭지 않을 예정이거든. 평소 안 가던 데 한번 가봐.",
        ],
        "재물운": [
            "지갑 열 일 하나 생길 것 같은데 너무 걱정 마, 그만큼 다시 채워질 촉이 딱 보여. 돈이 나가고 들어오는 게 균형 맞는 날이라고 보면 돼.",
            "쇼핑앱 켜놓고 장바구니만 채우고 있지? 오늘따라 충동구매 욕구 세게 오는 날이니까, 결제 버튼 누르기 전에 하루만 묵혀둬. 내일 보면 마음 바뀔 수도 있어.",
        ],
        "건강운": [
            "몸은 멀쩡한데 이상하게 축 처지는 느낌 들지? 그거 몸이 아니라 마음이 먼저 지친 거야. 오늘은 그냥 좀 쉬어, 억지로 뭐 하지 말고.",
            "어깨나 목 뒤 뻐근하면 딱 스트레칭 한 번 해줘, 완전 개운해질 촉이 온다. 커피 대신 물 한 잔 먼저 마셔봐, 오늘 몸이 유난히 반응할 거야.",
        ],
        "인간관계운": [
            "단톡방에서 눈팅만 하지 말고 오늘은 한마디 던져봐, 반응 완전 좋을 촉이야. 평소 조용했던 만큼 임팩트도 클 거야.",
            "괜히 서먹했던 그 사람이랑 오늘 자연스럽게 풀릴 촉이 딱 온다. 억지로 안 풀어도 돼, 흐름에 맡겨. 누가 부탁하는데 부담스러우면 편하게 거절해도 되는 날이야.",
        ],
    },
    "tarot_master": {
        "총운": [
            "카드를 펼치자 안개 속에 흐릿한 등불 하나가 보였습니다. 지금 당신도 그렇게, 뭔가 뿌옇게 느껴지는 아침을 보내고 계실지 모르죠. 하지만 안개는 오후가 되면 걷히기 마련입니다. 그때 등불이 선명해지듯, 당신의 길도 또렷해질 것입니다.",
            "이번엔 열려 있는 문이 그려진 카드가 나왔습니다. 지금까지 망설이고 있던 무언가가 있다면, 오늘 그 문이 슬며시 열리는 걸 느끼게 될 거예요. 억지로 밀지 않아도 흐름이 알아서 당신을 이끕니다.",
        ],
        "애정운": [
            "두 개의 잔이 나란히 놓인 카드가 나왔습니다. 이건 마음을 나눌 준비가 되었다는 신호예요. 혼자 담아두던 말이 있다면, 오늘은 그 잔을 살짝 건네보세요. 생각보다 따뜻한 답이 돌아올 겁니다.",
            "닫혀 있던 카드 한 장이 스스로 펼쳐지더군요. 누군가에게 다가가고 싶었지만 망설였던 마음, 오늘은 그 문이 저절로 열리는 걸 느끼실 거예요. 먼저 손 내미는 쪽이 오늘의 승자입니다.",
        ],
        "재물운": [
            "동전 카드가 거꾸로 나왔습니다. 지출과 수입이 동시에 오가는 흐름이라는 뜻이죠. 걱정하지 마세요, 나가는 만큼 채워질 여지도 함께 놓여 있으니까요. 다만 오늘은 충동보다 계획을 앞세우는 게 카드의 조언입니다.",
            "작은 금고가 살짝 열린 카드가 보이는군요. 무심코 지나쳤던 곳에 뜻밖의 것이 숨어있을 수 있습니다. 잊고 있던 포인트나 환급금, 오늘 한 번 확인해보시길 권합니다.",
        ],
        "건강운": [
            "지친 인물이 누워 있는 카드가 나왔습니다. 몸보다 마음이 먼저 신호를 보내고 있다는 뜻이에요. 오늘은 무리하지 마시고, 자신을 다독여주는 시간을 가져보세요.",
            "흐르는 물이 그려진 카드입니다. 오늘 당신의 몸은 유난히 수분과 휴식에 반응할 거예요. 물 한 잔, 이른 잠자리, 그 작은 선택이 내일의 컨디션을 좌우합니다.",
        ],
        "인간관계운": [
            "마주 보는 두 사람의 카드가 나왔습니다. 오늘은 솔직한 말 한마디가 관계의 열쇠가 될 거예요. 돌려 말하기보다 있는 그대로 전해보세요.",
            "오래된 편지가 그려진 카드입니다. 그리운 누군가에게서 소식이 닿을 수 있는 흐름이 보이네요. 혹은 당신이 먼저 그 편지를 써보는 것도 좋겠습니다.",
        ],
    },
    "grandma_shaman": {
        "총운": [
            "아침에 눈 뜨자마자 왜 이렇게 개운치 않냐 싶었지? 그것이 다 몸이 아니라 맘이 먼저 무거운 거여. 근디 걱정 붙들어매소, 오후 되믄 싹 풀릴 거니께. 오늘 누가 슬쩍 도와줄 사람도 나타날 겨.",
            "오늘은 촉이 딱 좋은 날이여. 뭔 결정 할 일 있으면 머리 굴리지 말고 맘 가는 대로 하소. 작은 실수 하나쯤 혀도 큰일 안 나니께 편하게 지내소.",
        ],
        "애정운": [
            "오해 있었으면 오늘 먼저 말 한마디 건네보소. 그게 뭐라고 그렇게 망설였을까 싶을 정도로 싹 풀릴 겨. 부부간에도 곱게 말하면 다 통하는 법이여.",
            "혼자인 사람은 오늘 우연히 좋은 인연 만날 수도 있응께, 집에만 있지 말고 나가보소. 밖에 나가야 인연도 만나는 겨.",
        ],
        "재물운": [
            "오늘 돈 좀 나갈 일 있어도 걱정 마소, 그만큼 또 들어올 텡께. 다만 충동적으로 뭐 사지 말고 하루만 참아보소, 그게 지혜여.",
            "동네 사람이랑 돈 거래는 이번 주만은 조심하소. 대신 저축 습관 오늘부터 들여보소, 작은 게 쌓이면 큰 거 된당께.",
        ],
        "건강운": [
            "몸보다 맘이 먼저 지친 날이여. 억지로 뭐 하려 말고 잠깐이라도 쉬었다 가소. 그게 오늘 제일 잘하는 일이여.",
            "어깨 뭉친 데 있으면 슬슬 풀어주소. 커피보다 물 자주 마시고, 일찍 자면 낼 컨디션이 확 다를 겨.",
        ],
        "인간관계운": [
            "말 한마디가 오늘 누구한테는 큰 힘이 될 겨. 별거 아닌 말이라도 따뜻하게 건네보소.",
            "둘이 다투는 데 끼면 한쪽 편들지 말고 가만있소. 오랜만에 연락 온 사람 있으면 반갑게 받아주고.",
        ],
    },
    "baby_fox": {
        "총운": [
            "아침부터 코가 간질간질한 게, 뭔가 좋은 냄새가 나! 처음엔 왜 이러지 싶었는데, 이게 다 오늘 좋은 일 생긴다는 신호였어! 오후 되면 꼬리가 저절로 살랑살랑할걸?",
            "귀를 쫑긋 세워봐, 오늘 왠지 좋은 소식이 들려올 것 같아! 작은 실수 하나쯤 해도 괜찮아, 금방 다시 방긋 웃을 수 있으니까!",
        ],
        "애정운": [
            "킁킁, 누군가한테 연락하고 싶은 냄새가 솔솔 나는데?! 망설이지 말고 지금 보내봐! 예상보다 훨씬 반가운 답이 올 것 같아!",
            "혼자여도 전혀 걱정 안 해도 돼! 오늘 우연히 만난 친구가 생각보다 특별할 수도 있거든! 평소 안 가던 데 한번 가볼까?",
        ],
        "재물운": [
            "오늘 용돈이나 선물 생길 것 같은 냄새가 솔솔 나! 그래도 사고 싶은 거 있으면 하루만 참아보자, 내일 더 좋은 게 기다릴지도 몰라!",
            "친구랑 돈 문제는 오늘 살짝 조심하는 게 좋을 것 같아. 대신 저금통에 동전 하나씩 모으는 재미, 오늘부터 시작해볼까?!",
        ],
        "건강운": [
            "몸보다 마음이 좀 지쳤나봐, 낮잠 한숨 자고 나면 완전 괜찮아질 거야! 억지로 뭐 안 해도 돼!",
            "물 많이 마시면 오늘 컨디션 최고일 거야! 몸이 뻐근하면 콩콩 뛰면서 풀어줘봐, 완전 시원해!",
        ],
        "인간관계운": [
            "친구들 모인 데서 한마디 하면 완전 인기 많아질 거야! 쑥스러워하지 말고 용기내봐!",
            "어색했던 친구랑 오늘 자연스럽게 풀릴 것 같아! 오랜만에 만나는 친구 있으면 꼬리 흔들며 반겨줘!",
        ],
    },
    "fortune_master40": {
        "총운": [
            "오늘은 목(木)의 기운이 강하게 작용하는 날입니다. 아침에는 다소 흐릿하게 느껴질 수 있으나, 오후로 갈수록 판단력이 또렷해지는 흐름이니 서두르지 않으셔도 됩니다. 사주에 이르길, 귀인이 나타날 조짐도 함께 보입니다.",
            "직감이 예리해지는 날입니다. 중요한 결정을 앞두고 계신다면, 오늘은 논리보다 마음이 이끄는 쪽을 믿으셔도 무방합니다. 작은 구설이 있을 수 있으나 크게 번지지 않을 것이니 마음에 담아두지 마십시오.",
        ],
        "애정운": [
            "오늘은 인연의 기운이 살아나는 흐름입니다. 먼저 다가가는 쪽이 유리하며, 특히 오랜 인연에게 연락을 취해보시길 권합니다. 만남의 기운도 약하게나마 흐르고 있으니 새로운 자리에 나가보시는 것도 좋겠습니다.",
            "가까운 사이일수록 말을 아끼는 것이 오늘의 지혜입니다. 사소한 말 한마디가 오해를 부를 수 있는 날이니, 표현은 신중히, 마음은 따뜻하게 전하시길 바랍니다.",
        ],
        "재물운": [
            "재물운이 들고 나는 흐름이라, 지출과 수입이 함께 움직일 날입니다. 충동적인 소비보다는 계획된 지출이 오늘의 재운에 유리하게 작용할 것입니다.",
            "금전 거래는 신중을 기하시는 것이 좋겠습니다. 다만 작은 재테크 습관을 오늘부터 들이신다면, 훗날 돌아보았을 때 큰 자산의 시작점이 되어 있을 것입니다.",
        ],
        "건강운": [
            "몸보다 마음의 기운이 먼저 지치는 날입니다. 무리한 일정은 피하시고, 충분한 휴식을 취하시길 권합니다. 수면의 질이 오늘 하루의 컨디션을 좌우하는 열쇠가 될 것입니다.",
            "기가 뭉치는 부위가 있을 수 있으니, 틈틈이 몸을 풀어주시길 바랍니다. 과로를 삼가고 몸이 보내는 신호에 귀 기울이시는 것이 오늘의 처방입니다.",
        ],
        "인간관계운": [
            "오늘 건넨 말 한마디가 상대에게 생각보다 큰 힘이 될 것입니다. 중재자의 역할을 맡게 될 흐름도 함께 보이니, 중립을 지키시길 바랍니다.",
            "오랜 인연과의 대화가 뜻밖의 좋은 기회로 이어질 수 있는 날입니다. 혼자만의 시간이 필요하시다면, 무리하게 약속을 잡지 않으셔도 좋겠습니다.",
        ],
    },
    "joseon_monk": {
        "총운": [
            "아침의 안개는 곧 걷히는 법이오. 지금 앞이 흐릿하게 느껴진다 해도 낙심치 마시오. 오후가 되면 길이 절로 선명해질 것이니, 그저 걸음을 늦추지 않으면 될 일이오.",
            "오늘은 직감이 밝아지는 날이오. 마음이 이끄는 대로 하여도 무방하니, 너무 재고 따지지 마시오. 작은 허물은 물처럼 흘려보내도 좋소.",
        ],
        "애정운": [
            "말 한마디가 얼어붙은 마음을 녹이는 법이오. 오늘 먼저 다가가 보시오, 생각보다 따뜻한 답이 돌아올 것이오. 홀로인 이는 뜻밖의 인연을 마주할 수도 있소.",
            "가까운 사이일수록 말을 아끼는 것이 지혜로운 법이오. 그리운 이에게서 소식이 닿을 인연이니, 마음의 문을 열어두시오.",
        ],
        "재물운": [
            "재물은 물과 같아 흐르고 채워지는 법이니 조급해 마시오. 오늘 나가는 것이 있다면 훗날 채워질 것이오. 충동보다 헤아림이 오늘의 재물을 지키는 법이오.",
            "금전의 거래는 신중히 하시오. 작은 절제가 훗날 큰 복이 되어 돌아온다는 것을 잊지 마시오.",
        ],
        "건강운": [
            "몸보다 마음이 먼저 지치는 날이니 잠시 쉬어가시오. 무리한 걸음은 삼가고, 몸이 전하는 소리에 귀 기울이시오.",
            "잠을 청함이 오늘의 기운을 채우는 법이오. 굳은 몸을 풀어주는 것 또한 오늘의 수행이라 여기시오.",
        ],
        "인간관계운": [
            "무심한 말 한마디가 누군가에게 큰 위로가 될 수 있소. 다투는 이들 사이에서는 중심을 지키는 것이 도리요.",
            "오랜 인연과의 대화가 뜻밖의 인연으로 이어질 수 있소. 홀로 있고자 하면 억지로 자리를 만들지 않아도 좋소.",
        ],
    },
    "fox_spirit": {
        "총운": [
            "달빛이 구름에 가려졌다가 다시 드러나듯, 지금 그대의 하루도 흐릿하게 시작되었을 것이네. 허나 오후가 되면 구름이 걷히고, 그 흐름은 선명해질 것이네. 천 년을 산 여우도 오늘만큼은 그대의 직감을 믿으라 하네.",
            "오늘은 그림자 속에서 좋은 인연이 스칠 것이네. 눈을 밝게 하여 지나치는 것들을 잘 살피게. 작은 실수는 달빛 아래 그림자처럼 곧 사라질 것이니 염려치 말게.",
        ],
        "애정운": [
            "달빛 아래 나눈 말 한마디가 마음을 녹이는 법이네. 망설이던 마음이 있다면, 오늘 그 말을 꺼내보게. 그리운 이의 소식도 달빛을 타고 올 것이네.",
            "홀로 걷는 이에게 오늘 뜻밖의 인연이 스칠 수 있네. 가까운 사이일수록 말을 아끼는 것이 지혜라는 것도 잊지 말게.",
        ],
        "재물운": [
            "재물은 달의 차고 이지러짐과 같아, 오늘은 나가고 들어옴이 함께하는 흐름이네. 충동보다 헤아림이 오늘의 재물을 지키는 법이네.",
            "금전의 거래는 신중히 임하게. 작은 절제가 훗날 큰 복으로 돌아올 것이니, 오늘의 인내를 잊지 말게.",
        ],
        "건강운": [
            "몸보다 마음이 먼저 지치는 날이니 잠시 쉬어가게. 달이 차오르듯 일찍 잠들면 그대의 기운도 함께 채워질 것이네.",
            "굳은 몸을 풀어주는 것이 오늘의 처방이네. 몸이 보내는 신호에 귀 기울이게, 무리하지 말게나.",
        ],
        "인간관계운": [
            "무심한 말 한마디가 누군가에게 큰 힘이 될 수 있네. 다투는 이들 사이에서는 중심을 지키는 것이 지혜라네.",
            "오랜 인연과의 대화가 뜻밖의 좋은 흐름으로 이어질 수 있네. 홀로 있고자 하면 억지로 자리를 만들지 않아도 좋네.",
        ],
    },
    "cat_sage": {
        "총운": [
            "냥, 아침부터 왠지 나른한 기분 들지 않았냥? 그거 오전엔 다 그렇다냥, 오후 되면 싹 다 보인다냥. 오늘 누가 도와줄 것 같은 기분도 든다냥, 기대해도 좋다냥.",
            "촉이 좋은 날이다냥. 뭔가 결정할 일 있으면 마음 가는 대로 해도 된다냥. 작은 실수는 신경 쓰지 말라냥, 별거 아니다냥.",
        ],
        "애정운": [
            "먼저 말 걸어보라냥, 반응 나쁘지 않을 거다냥. 혼자여도 괜찮다냥, 오늘 우연한 만남이 있을 수도 있다냥.",
            "다퉈도 금방 풀릴 거다냥, 걱정 말라냥. 그리운 사람한테 연락 올 것 같다냥, 기다려보라냥.",
        ],
        "재물운": [
            "오늘 돈 좀 나갈 수 있다냥, 그만큼 들어올 거다냥. 사고 싶은 거 있어도 하루만 참으라냥.",
            "돈 거래는 이번엔 조심하라냥. 저축 습관 오늘부터 들이라냥, 나중에 도움 된다냥.",
        ],
        "건강운": [
            "몸보다 마음이 지친 것 같다냥, 좀 쉬라냥. 일찍 자면 컨디션 좋아질 거다냥.",
            "몸 뻐근하면 스트레칭하라냥. 물 좀 자주 마시라냥, 커피는 줄이라냥.",
        ],
        "인간관계운": [
            "말 한마디가 누군가에게 힘이 될 거다냥. 다투는 사람들 사이에선 중립 지키라냥.",
            "오랜만에 연락 온 사람 있으면 반갑게 받으라냥. 혼자 있고 싶으면 억지로 나가지 않아도 된다냥.",
        ],
    },
    "mz_saju_girl": {
        "총운": [
            "아침부터 뭔가 미묘한 기분 들었지? 그거 오전 한정 텐션이고, 오후 되면 완전 달라질 예정이야! 귀인 만날 각도 보이니까 주변 잘 살펴봐!",
            "오늘 직감 대로 가도 되는 날이야, 믿고 가! 실수해도 노상관, 금방 다 괜찮아질 거야, 리얼로!",
        ],
        "애정운": [
            "썸이면 오늘 먼저 연락해봐, 완전 좋은 타이밍이라니까! 혼자여도 오늘 우연한 만남 있을 수도 있어, 기대해봐!",
            "투닥거려도 금방 화해각이야, 걱정 노노! 그리운 사람한테 연락 올 것 같은 느낌적 느낌이 딱 온다!",
        ],
        "재물운": [
            "오늘 돈 좀 쓸 수도 있는데 다시 들어올 각이야! 사고 싶은 거 있으면 하루만 참아봐, 더 좋은 딜 있을지도 몰라!",
            "돈 거래는 오늘만 좀 조심해! 저축 습관 오늘부터 시작해봐, 완전 뿌듯할 듯!",
        ],
        "건강운": [
            "몸보다 마음이 좀 지쳤나봐, 오늘은 쉬어가자! 일찍 자면 낼 컨디션 미쳐, 진짜!",
            "어깨 뭉쳤으면 스트레칭 좀 해줘! 물 많이 마셔, 커피는 오늘만 좀 줄이고!",
        ],
        "인간관계운": [
            "단톡방에서 한마디 하면 완전 인기 많아질 듯! 어색했던 사람이랑 오늘 자연스럽게 풀릴 각이야!",
            "오랜만에 연락 온 사람 있으면 반갑게 받아줘! 혼자 있고 싶으면 억지로 약속 안 잡아도 돼!",
        ],
    },
    "saju_witch": {
        "총운": [
            "솥 속의 안개가 스멀스멀 걷히는군요. 지금은 흐릿하게 느껴질지 몰라도, 오후엔 흐름이 선명해질 거예요. 오늘은 귀한 인연이 스칠 흐름도 함께 보이니, 놓치지 마세요.",
            "직감의 별이 유난히 밝게 빛나는 날이에요. 믿고 움직여도 좋아요. 작은 실수는 솥 안에서 금방 녹아 사라질 테니 염려 마세요.",
        ],
        "애정운": [
            "촛불 두 개가 나란히 놓인 걸 보니, 오늘은 마음을 나눌 때예요. 혼자인 분이라면 뜻밖의 인연이 스칠 수도 있답니다.",
            "가까운 사이일수록 말을 아끼는 것이 마녀의 지혜죠. 그리운 이의 소식이 바람을 타고 올 수 있으니, 기다려보세요.",
        ],
        "재물운": [
            "솥 안의 금화가 오늘은 들고 나는 흐름이에요. 충동보다 헤아림이 오늘의 재물을 지키는 주문이랍니다.",
            "금전 거래는 신중히, 이건 마녀의 조언이에요. 작은 절제가 훗날 큰 보물이 되어 돌아올 거예요.",
        ],
        "건강운": [
            "몸보다 마음이 먼저 지치는 날이에요. 잠시 쉬어가세요, 일찍 잠드는 것이 오늘의 회복 주문이랍니다.",
            "굳은 몸을 풀어주는 것이 오늘의 처방이에요. 몸이 보내는 신호를 무시하지 마세요, 무리는 금물이랍니다.",
        ],
        "인간관계운": [
            "무심한 말 한마디가 누군가에게 큰 힘이 될 거예요. 다투는 이들 사이에서는 중심을 지키는 것이 지혜랍니다.",
            "오랜 인연과의 대화가 뜻밖의 좋은 흐름으로 이어질 수 있어요. 홀로 있고 싶다면 억지로 자리를 만들지 않아도 괜찮아요.",
        ],
    },
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
if "persona_selected_once" not in st.session_state:
    st.session_state.persona_selected_once = False
if "persona_locked" not in st.session_state:
    st.session_state.persona_locked = False
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

st.markdown('<div class="main-title" style="margin-left:-16px;">🔮 <span class="title-blue">운세</span> <span class="title-warm">캐릭터관</span></div>', unsafe_allow_html=True)

# 캐릭터 선택 (언제든 변경 가능 -> 바꾸면 처음부터 다시 시작)
# 처음엔 아무것도 선택되지 않은 상태로 시작해서, 기본값(MZ 여자무당)을 고르더라도
# "선택했다"는 동작이 확실히 감지되도록 합니다.
select_index = (
    list(PERSONAS.keys()).index(st.session_state.persona_id)
    if st.session_state.persona_selected_once else None
)
new_persona_id = st.selectbox(
    "캐릭터 선택",
    list(PERSONAS.keys()),
    index=select_index,
    format_func=lambda k: f"{PERSONAS[k]['emoji']} {PERSONAS[k]['name']}",
    placeholder="👆 캐릭터를 선택해보세요",
    label_visibility="collapsed",
)
if new_persona_id is not None and (
    not st.session_state.persona_selected_once or new_persona_id != st.session_state.persona_id
):
    st.session_state.persona_id = new_persona_id
    st.session_state.persona_selected_once = True
    st.session_state.persona_locked = True
    st.session_state.current_greeting = random.choice(PERSONAS[new_persona_id]["greeting"])
    st.session_state.step = 0
    st.rerun()

persona = PERSONAS[st.session_state.persona_id]
avatar_content = persona.get("avatar_svg", persona["emoji"])

if st.session_state.step == 0 and not st.session_state.persona_locked:
    # 아직 캐릭터를 직접 고르지 않은 상태에서만 10명이 자동으로 순서대로 바뀌며 보여지는 미리보기
    interval = 3.5
    persona_items = list(PERSONAS.items())
    n = len(persona_items)
    duration = n * interval
    layers_html = ""
    for i, (pid, p) in enumerate(persona_items):
        p_avatar = p.get("avatar_svg", p["emoji"])
        delay = -(i * interval)
        layers_html += f'''
        <div class="avatar-showcase-layer" style="animation-duration:{duration}s; animation-delay:{delay}s;">
            <div class="avatar-showcase-icon" style="background:{p['color']}33; border:2px solid {p['color']};">
                {p_avatar}
            </div>
            <div class="avatar-showcase-name">{p['name']}</div>
        </div>'''
    st.markdown(f'<div class="avatar-showcase">{layers_html}</div>', unsafe_allow_html=True)
    st.markdown('<div class="showcase-caption">✨ 10명의 캐릭터가 기다리고 있어요 · 캐릭터를 고르면 멈춰요 ✨</div>', unsafe_allow_html=True)
else:
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
    if st.session_state.persona_locked:
        st.markdown(f'<div class="speech-bubble">{st.session_state.get("current_greeting", random.choice(persona["greeting"]))}</div>', unsafe_allow_html=True)
        if st.button("다음 →", use_container_width=True):
            st.session_state.step = 1
            st.rerun()
    else:
        if st.button("시작하기 →", use_container_width=True):
            st.session_state.persona_locked = True
            st.session_state.persona_selected_once = True
            st.session_state.current_greeting = random.choice(persona["greeting"])
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
    if st.button("← 이전", use_container_width=True):
        st.session_state.user_name = name_input
        st.session_state.step = 0
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
    if st.button("← 이전", use_container_width=True):
        st.session_state.birth_year = by
        st.session_state.birth_month = bm
        st.session_state.birth_day = bd
        st.session_state.step = 1
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
    if st.button("← 이전", use_container_width=True):
        st.session_state.step = 2
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
    active_pool = PERSONA_FORTUNE.get(st.session_state.persona_id, fortune_pool)
    for cat in categories:
        text = random.choice(active_pool[cat])
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

    closing_text = random.choice(persona["closing"])
    st.markdown(f"""
    <div class="lucky-box">
        <b>🍀 오늘의 평균 운세 지수: {avg_luck}점</b><br><br>
        행운의 색: <b>{color}</b> &nbsp;|&nbsp; 행운의 아이템: <b>{item}</b><br>
        행운의 숫자: <b>{number}</b> &nbsp;|&nbsp; 행운의 시간대: <b>{time_range}</b>
    </div>
    <div class="speech-bubble">{persona['emoji']} {closing_text}</div>
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
        st.session_state.persona_locked = False
        st.session_state.persona_selected_once = False
        st.rerun()
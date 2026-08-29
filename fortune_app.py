import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import date

# ------------------------------
# 설정: 여기에 본인 제휴 링크를 넣으세요
# ------------------------------
COUPANG_LINK = "https://link.coupang.com/a/gATwbtGIIS"
TOSS_LINK = "https://toss.me/여기에_본인_토스_쉐어링크"

st.set_page_config(page_title="오늘의 운세", page_icon="🔮", layout="centered")
# 참고: page_icon(브라우저 탭 아이콘)은 이모지만 지원되어 기기별로 다르게 보일 수 있어요.
# 본문 제목의 아이콘은 아래에서 SVG로 직접 그려서 기기와 무관하게 항상 동일하게 표시됩니다.

# ------------------------------
# 커스텀 스타일
# ------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #4f46e5 0%, #4338ca 100%);
    }
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #6ba3c9, #4a7fa5);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
        letter-spacing: -0.5px;
    }
    .sub-caption {
        text-align: center;
        color: #7a94a3;
        margin-bottom: 1.5rem;
        letter-spacing: 0.5px;
    }
    .zodiac-badge {
        text-align: center;
        font-size: 1.05rem;
        color: #4a7fa5;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .fortune-card {
        background: #ffffff;
        border: 1px solid #d5e6f0;
        box-shadow: 0 2px 16px rgba(60, 50, 40, 0.06);
        border-radius: 18px;
        padding: 24px;
        margin-top: 14px;
        margin-bottom: 14px;
    }
    .fortune-cat-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #4a7fa5;
        margin-bottom: 6px;
        letter-spacing: -0.2px;
    }
    .fortune-cat-text {
        font-size: 1rem;
        color: #3a4a56;
        line-height: 1.65;
        margin-bottom: 4px;
    }
    .lucky-box {
        background: #f4f9fc;
        border: 1px solid #d5e6f0;
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        color: #3a4a56;
        font-weight: 500;
        margin-bottom: 18px;
        line-height: 1.8;
    }
    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #6ba3c9, #4a7fa5);
        color: #ffffff;
        font-weight: 700;
        border-radius: 30px;
        border: none;
        padding: 10px 0;
        width: 100%;
        letter-spacing: 0.3px;
    }
    div[data-testid="stLinkButton"] a {
        border-radius: 30px !important;
        font-weight: 600 !important;
    }
    [data-testid="stCaptionContainer"] p,
    .stCaption {
        color: #7a94a3 !important;
        opacity: 1 !important;
    }
    label, .stSlider label {
        color: #7a94a3 !important;
        font-weight: 500;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
    .stMarkdown p {
        color: #2e3d47 !important;
        opacity: 1 !important;
    }
    div[data-testid="stTextInput"] input {
        background: #ffffff !important;
        color: #2e3d47 !important;
        border: 1px solid #d5e6f0 !important;
        border-radius: 12px !important;
    }
    div[data-baseweb="select"] {
        border-radius: 12px !important;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 띠(십이지) 계산
# 1924년 = 쥐띠 기준으로 12년 주기 계산
# ------------------------------
ZODIAC_ORDER = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]

ZODIAC_INFO = {
    "쥐":   {"emoji": "🐭", "trait": "영리하고 순발력이 뛰어난"},
    "소":   {"emoji": "🐮", "trait": "성실하고 우직하게 밀고 나가는"},
    "호랑이": {"emoji": "🐯", "trait": "용맹하고 추진력이 강한"},
    "토끼": {"emoji": "🐰", "trait": "섬세하고 배려심이 깊은"},
    "용":   {"emoji": "🐲", "trait": "카리스마 있고 자신감 넘치는"},
    "뱀":   {"emoji": "🐍", "trait": "지혜롭고 통찰력이 뛰어난"},
    "말":   {"emoji": "🐴", "trait": "활동적이고 자유로운 영혼을 가진"},
    "양":   {"emoji": "🐑", "trait": "온화하고 예술적 감각이 뛰어난"},
    "원숭이": {"emoji": "🐵", "trait": "재치있고 임기응변에 강한"},
    "닭":   {"emoji": "🐔", "trait": "꼼꼼하고 계획적인"},
    "개":   {"emoji": "🐶", "trait": "의리있고 신뢰할 수 있는"},
    "돼지": {"emoji": "🐷", "trait": "너그럽고 복이 많은"},
}


def get_zodiac(year: int) -> str:
    idx = (year - 1924) % 12
    return ZODIAC_ORDER[idx]


# ------------------------------
# 카테고리별 상세 운세 문구 풀
# ------------------------------
fortune_pool = {
    "총운": [
        "오전엔 다소 흐릿하던 흐름이 오후 들어 또렷해지며, 그동안 미뤄왔던 결정을 내리기 좋은 타이밍이 찾아옵니다.",
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
        "충동적인 소비보다는 계획된 지출이 더 큰 만족을 주는 하루입니다. 장바구니에 며칠 담아두는 습관이 도움이 됩니다.",
        "투자나 큰 결정은 오늘보다 며칠 뒤로 미루는 것이 유리해 보입니다. 서두르면 손해를 볼 수 있어요.",
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

st.markdown("""
<div class="main-title" style="display:flex; align-items:center; justify-content:center; gap:12px;">
    <svg width="48" height="48" viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg">
        <defs>
            <radialGradient id="ballGrad" cx="35%" cy="30%" r="70%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="45%" stop-color="#bfe0f0"/>
                <stop offset="100%" stop-color="#4a7fa5"/>
            </radialGradient>
            <linearGradient id="standGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#6ba3c9"/>
                <stop offset="100%" stop-color="#3d6d94"/>
            </linearGradient>
        </defs>
        <circle cx="32" cy="27" r="20" fill="url(#ballGrad)" stroke="#6ba3c9" stroke-width="1.5"/>
        <ellipse cx="25" cy="19" rx="6" ry="4" fill="#ffffff" opacity="0.7"/>
        <path d="M16 50 Q32 42 48 50 L52 58 Q32 52 12 58 Z" fill="url(#standGrad)"/>
        <path d="M8 8 l2.2 5.2 L15.4 15.4 l-5.2 2.2 L8 22.8 l-2.2-5.2 L0.6 15.4 l5.2-2.2 Z" fill="#6ba3c9"/>
        <path d="M53 6 l1.6 3.8 3.8 1.6 -3.8 1.6 -1.6 3.8 -1.6-3.8 -3.8-1.6 3.8-1.6 Z" fill="#4a7fa5"/>
    </svg>
    <span>오늘의 운세</span>
</div>
""", unsafe_allow_html=True)
st.markdown(f'<div class="sub-caption">{date.today().strftime("%Y년 %m월 %d일")} 기준</div>', unsafe_allow_html=True)

name = st.text_input("이름 (선택)", placeholder="예: 인수")

current_year = date.today().year
year_options = list(range(current_year, 1929, -1))  # 최근 연도부터 1930년까지
col_y, col_m, col_d = st.columns(3)
with col_y:
    birth_year = st.selectbox("출생연도", year_options, index=year_options.index(1995))
with col_m:
    birth_month = st.selectbox("출생월", list(range(1, 13)), index=0)
with col_d:
    birth_day = st.selectbox("출생일", list(range(1, 32)), index=0)

try:
    birth_date = date(birth_year, birth_month, birth_day)
except ValueError:
    st.warning("존재하지 않는 날짜예요. 날짜를 다시 확인해주세요 (예: 2월 30일 X)")
    st.stop()

zodiac = get_zodiac(birth_date.year)
zinfo = ZODIAC_INFO[zodiac]
st.markdown(
    f'<div class="zodiac-badge">{zinfo["emoji"]} {birth_date.year}년생 · <b>{zodiac}띠</b> ({zinfo["trait"]} 기운)</div>',
    unsafe_allow_html=True,
)

if st.button("오늘의 상세 운세 보기 ✨"):
    # 이름 + 생년월일 + 오늘 날짜로 시드 고정 → 같은 사람은 하루 동안 같은 결과
    seed_str = f"{name}-{birth_date}-{date.today()}"
    random.seed(seed_str)

    st.markdown(f"#### {name + '님, ' if name else ''}{zodiac}띠의 오늘 이야기")
    st.write(
        f"{zinfo['trait']} {zodiac}띠답게, 오늘은 자신의 강점이 유독 잘 발휘되는 하루가 될 것입니다."
    )

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
        st.progress(score / 100)

    avg_luck = round(total_luck / len(categories))

    color = random.choice(lucky_colors)
    item = random.choice(lucky_items)
    number = random.choice(lucky_numbers)
    time_range = random.choice(lucky_times)

    st.markdown(f"""
    <div class="lucky-box">
        <b>🍀 오늘의 평균 운세 지수: {avg_luck}점</b><br><br>
        행운의 색: <b>{color}</b> &nbsp;|&nbsp;
        행운의 아이템: <b>{item}</b><br>
        행운의 숫자: <b>{number}</b> &nbsp;|&nbsp;
        행운의 시간대: <b>{time_range}</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎁 오늘의 운세를 더 좋게 만들어줄 아이템")

    col1, col2 = st.columns(2)
    with col1:
        st.link_button("쿠팡에서 행운템 보기 🛒", COUPANG_LINK, use_container_width=True)
    with col2:
        st.link_button("토스로 용돈 받기 💰", TOSS_LINK, use_container_width=True)

    st.caption(
        "ℹ️ 이 포스팅은 쿠팡 파트너스 활동의 일환으로, "
        "이에 따른 일정액의 수수료를 제공받을 수 있습니다."
    )

    share_url = "https://mysowoon-fortune.streamlit.app/"
    st.markdown("👇 **친구에게 공유하기**")
    components.html(f"""
    <div style="display:flex; gap:8px; align-items:center; font-family: sans-serif;">
        <input id="shareUrlFortune" type="text" readonly value="{share_url}"
            style="flex:1; padding:10px 14px; border-radius:20px; border:1px solid rgba(255,255,255,0.2);
                   background:rgba(255,255,255,0.08); color:#f0eaff; font-size:0.9rem; outline:none;">
        <button onclick="copyFortuneLink(event)"
            style="padding:10px 18px; border-radius:20px; border:none;
                   background:linear-gradient(90deg,#f9d976,#c99df0); color:#1a1030;
                   font-weight:700; cursor:pointer; white-space:nowrap; font-size:0.9rem;">
            복사 📋
        </button>
    </div>
    <script>
    function copyFortuneLink(event) {{
        var copyText = document.getElementById("shareUrlFortune");
        navigator.clipboard.writeText(copyText.value).then(function() {{
            var btn = event.target;
            var original = btn.innerText;
            btn.innerText = "복사됨! ✅";
            setTimeout(function() {{ btn.innerText = original; }}, 1500);
        }});
    }}
    </script>
    """, height=60)

else:
    st.info("생년월일을 확인하고 버튼을 눌러 오늘의 상세 운세를 확인해보세요!")
import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import date

# ------------------------------
# 설정: 여기에 본인 제휴 링크를 넣으세요
# ------------------------------
COUPANG_LINK = "https://link.coupang.com/a/gATwbtGIIS"
TOSS_LINK = "https://toss.me/여기에_본인_토스_쉐어링크"

st.set_page_config(page_title="운세 캐릭터관", page_icon="🔮", layout="centered")

# ------------------------------
# 커스텀 스타일 (차분한 차콜 + 웜 골드 톤, 어떤 캐릭터를 골라도 무난하게 어울림)
# ------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #1c1a1f 0%, #2a2630 50%, #1c1a1f 100%);
    }
    .main-title {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 800;
        background: linear-gradient(90deg, #f9d976, #f39f86, #c99df0);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-caption {
        text-align: center;
        color: #cbb8d8;
        margin-bottom: 1.6rem;
    }
    .persona-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 22px;
        padding: 26px;
        text-align: center;
        margin-bottom: 1.2rem;
    }
    .persona-avatar {
        font-size: 3.2rem;
        width: 88px;
        height: 88px;
        line-height: 88px;
        border-radius: 50%;
        margin: 0 auto 12px auto;
    }
    .persona-name {
        font-size: 1.3rem;
        font-weight: 800;
        color: #f9d976;
        margin-bottom: 2px;
    }
    .persona-subtitle {
        font-size: 0.85rem;
        color: #a89bb5;
        margin-bottom: 14px;
    }
    .persona-speech {
        background: rgba(255,255,255,0.06);
        border-radius: 16px;
        padding: 16px 18px;
        font-size: 1rem;
        color: #f0eaff;
        line-height: 1.6;
        text-align: left;
    }
    .fortune-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 24px;
        margin-top: 14px;
        margin-bottom: 14px;
    }
    .fortune-cat-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #f9d976;
        margin-bottom: 6px;
    }
    .fortune-cat-text {
        font-size: 1rem;
        color: #f0eaff;
        line-height: 1.6;
    }
    .closing-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        padding: 18px;
        text-align: center;
        color: #f5f0ff;
        font-style: italic;
        margin: 18px 0;
    }
    .lucky-box {
        background: rgba(255,255,255,0.06);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 16px;
        padding: 16px;
        text-align: center;
        color: #f5f0ff;
        margin-bottom: 18px;
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
        font-weight: 600 !important;
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
# ------------------------------
PERSONAS = {
    "mz_shaman": {
        "name": "MZ 여자무당", "emoji": "🔮", "color": "#ff6ec7",
        "subtitle": "반말 + 텐션 폭발, 신기 충만",
        "greeting": "안뇽! 나 지금 좀 신기 올라와서ㅋㅋ 몇 개만 물어볼게!",
        "button_label": "운세 보여줄게 🔮",
        "closing": "이거 완전 찐이니까 믿어봐ㅋㅋ 오늘 대박나길!",
    },
    "tarot_master": {
        "name": "신비로운 타로 마스터", "emoji": "🃏", "color": "#7b5ea7",
        "subtitle": "진중하고 묘한 존댓말",
        "greeting": "카드가 당신을 기다리고 있습니다. 조용히 마음을 가라앉히고, 오늘의 운명을 들여다보겠습니다.",
        "button_label": "카드를 펼치겠습니다 🃏",
        "closing": "카드는 거짓말을 하지 않습니다. 오늘 하루, 이 흐름을 마음에 새기시길.",
    },
    "grandma_shaman": {
        "name": "따뜻한 할머니 무당", "emoji": "🍵", "color": "#d98e5f",
        "subtitle": "포근한 사투리, 정겨움",
        "greeting": "아이고 왔능가~ 할미가 오늘 하루 봐줄 텡께 이리 앉아보소.",
        "button_label": "어디 한번 봐줄게 🍵",
        "closing": "괜찮혀, 다 잘 될 거여. 오늘 하루도 애썼다잉.",
    },
    "baby_fox": {
        "name": "말랑말랑 아기여우", "emoji": "🦊", "color": "#ff9662",
        "subtitle": "귀엽고 발랄한 반말",
        "greeting": "안녕! 나는 숲속 아기여우야! 오늘 네 운세, 내가 콕콕 짚어줄게!",
        "button_label": "운세 찾아올게 🦊",
        "closing": "히히, 오늘도 럭키하게 보내! 나중에 또 놀러와~",
    },
    "fortune_master40": {
        "name": "40대 역술인", "emoji": "🎋", "color": "#4a6fa5",
        "subtitle": "진중하고 신뢰감 있는 존댓말",
        "greeting": "어서 오십시오. 사주를 오래 봐온 사람으로서, 오늘 하루의 기운을 차분히 짚어드리겠습니다.",
        "button_label": "사주를 풀어드리겠습니다 🎋",
        "closing": "오늘 말씀드린 내용, 참고 삼아 하루를 보내시면 좋겠습니다.",
    },
    "joseon_monk": {
        "name": "조선시대 승려", "emoji": "📿", "color": "#8a7355",
        "subtitle": "고풍스러운 말투, 지혜로움",
        "greeting": "나무관세음보살. 그대의 발걸음이 이곳에 닿은 것도 인연이니, 오늘의 기운을 살펴보겠소.",
        "button_label": "기운을 살펴보겠소 📿",
        "closing": "모든 것은 마음먹기에 달렸소. 부디 평안한 하루 되시오.",
    },
    "fox_spirit": {
        "name": "여우신령", "emoji": "🌙", "color": "#9b59b6",
        "subtitle": "신비롭고 우아한 존댓말",
        "greeting": "안녕하신가, 인간이여. 나는 오랜 세월을 살아온 여우니라. 그대의 오늘을 잠시 들여다보겠네.",
        "button_label": "기운을 읽어보겠네 🌙",
        "closing": "오늘의 이야기는 여기까지. 부디 지혜롭게 하루를 걸으시게.",
    },
    "cat_sage": {
        "name": "고양이도사", "emoji": "🐱", "color": "#f4a460",
        "subtitle": "새침하지만 다 알고 있는 반말",
        "greeting": "냥. 오늘 운세가 궁금해서 온 게냥? 뭐, 어쩔 수 없이 봐주지 냥.",
        "button_label": "봐주겠다냥 🐱",
        "closing": "흥, 도움 됐으면 다행이다냥. 다음에 또 오라냥.",
    },
    "mz_saju_girl": {
        "name": "MZ 사주소녀", "emoji": "✨", "color": "#ff6b9d",
        "subtitle": "트렌디하고 발랄한 반말",
        "greeting": "얘들아 나 요즘 사주에 완전 꽂혀서 취미로 봐주고 있엉! 너두 궁금하지? ㅎㅎ",
        "button_label": "운세 뽑아볼게 ✨",
        "closing": "완전 힐링됐지? 오늘도 화이팅!! 저장하고 또 놀러와~",
    },
    "saju_witch": {
        "name": "사주마녀", "emoji": "🕸", "color": "#5c2a5c",
        "subtitle": "드라마틱하고 능청스러운 말투",
        "greeting": "후후... 마녀의 솥이 오늘도 부글부글 끓고 있군요. 당신의 운명을 한번 저어볼까요?",
        "button_label": "운명을 저어보겠어요 🕸",
        "closing": "오늘 점괘는 여기까지예요. 방심은 금물, 재미는 필수랍니다.",
    },
}

# ------------------------------
# 띠(십이지) 계산
# ------------------------------
ZODIAC_ORDER = ["쥐", "소", "호랑이", "토끼", "용", "뱀", "말", "양", "원숭이", "닭", "개", "돼지"]
ZODIAC_EMOJI = {
    "쥐": "🐭", "소": "🐮", "호랑이": "🐯", "토끼": "🐰", "용": "🐲", "뱀": "🐍",
    "말": "🐴", "양": "🐑", "원숭이": "🐵", "닭": "🐔", "개": "🐶", "돼지": "🐷",
}


def get_zodiac(year: int) -> str:
    return ZODIAC_ORDER[(year - 1924) % 12]


# ------------------------------
# 카테고리별 운세 문구 풀
# ------------------------------
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
# 화면 구성
# ------------------------------
st.markdown('<div class="main-title">🔮 운세 캐릭터관</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-caption">{date.today().strftime("%Y년 %m월 %d일")} · 원하는 캐릭터를 골라보세요</div>', unsafe_allow_html=True)

persona_id = st.selectbox(
    "캐릭터 선택",
    list(PERSONAS.keys()),
    format_func=lambda k: f"{PERSONAS[k]['emoji']} {PERSONAS[k]['name']}",
    label_visibility="collapsed",
)
persona = PERSONAS[persona_id]

st.markdown(f"""
<div class="persona-card">
    <div class="persona-avatar" style="background:{persona['color']}33; border:2px solid {persona['color']};">
        {persona['emoji']}
    </div>
    <div class="persona-name">{persona['name']}</div>
    <div class="persona-subtitle">{persona['subtitle']}</div>
    <div class="persona-speech">{persona['greeting']}</div>
</div>
""", unsafe_allow_html=True)

name = st.text_input("이름 (선택)", placeholder="예: 인수")

current_year = date.today().year
year_options = list(range(current_year, 1929, -1))
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

zodiac = get_zodiac(birth_year)
st.markdown(
    f'<div class="sub-caption">{ZODIAC_EMOJI[zodiac]} {birth_year}년생 · <b>{zodiac}띠</b></div>',
    unsafe_allow_html=True,
)

if st.button(persona["button_label"], use_container_width=True):
    seed_str = f"{persona_id}-{name}-{birth_date}-{date.today()}"
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
    <div class="closing-box">{persona['emoji']} {persona['closing']}</div>
    """, unsafe_allow_html=True)

    st.markdown("### 🎁 오늘의 운세를 더 좋게 만들어줄 아이템")
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("쿠팡에서 행운템 보기 🛒", COUPANG_LINK, use_container_width=True)
    with col2:
        st.link_button("토스로 용돈 받기 💰", TOSS_LINK, use_container_width=True)

    st.caption("이 포스팅은 쿠팡 파트너스 활동의 일환으로, 이에 따른 일정액의 수수료를 제공받을 수 있습니다.")

    share_url = "여기에_배포_후_생긴_URL을_적어주세요"
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

else:
    st.info(f"{persona['emoji']} 정보를 입력하고 버튼을 눌러 {persona['name']}의 운세를 확인해보세요!")

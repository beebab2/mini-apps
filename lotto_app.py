import streamlit as st
import streamlit.components.v1 as components
import random
from datetime import date

# ------------------------------
# 설정: 여기에 본인 제휴 링크를 넣으세요
# ------------------------------
COUPANG_LINK = "https://link.coupang.com/여기에_본인_쿠팡파트너스_링크"
TOSS_LINK = "https://toss.me/여기에_본인_토스_쉐어링크"

st.set_page_config(page_title="행운의 로또 번호", page_icon="🍀", layout="centered")

# ------------------------------
# 커스텀 스타일
# ------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
    }
    .main-title {
        text-align: center;
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, #a8ff78, #78ffd6, #fff9a8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    .sub-caption {
        text-align: center;
        color: #b8e0e8;
        margin-bottom: 1.5rem;
    }
    .results-container {
        display: flex;
        flex-direction: column;
        width: 100%;
    }
    .set-row {
        position: relative;
        width: 100%;
        min-height: 54px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 18px;
    }
    .ball-row {
        display: flex;
        justify-content: center;
        gap: 10px;
        flex-wrap: wrap;
    }
    .set-label {
        position: absolute;
        left: 48px;
        top: 50%;
        transform: translateY(-50%);
        font-weight: 700;
        color: #eafffb;
        font-size: 1.05rem;
        white-space: nowrap;
    }
    .ball {
        width: 54px;
        height: 54px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: 800;
        font-size: 1.2rem;
        color: white;
        box-shadow: 0 3px 8px rgba(0,0,0,0.35);
    }
    div[data-testid="stButton"] button {
        background: linear-gradient(90deg, #78ffd6, #a8ff78);
        color: #0f2027;
        font-weight: 700;
        border-radius: 30px;
        border: none;
        padding: 10px 0;
        width: 100%;
    }
    div[data-testid="stLinkButton"] a {
        border-radius: 30px !important;
        font-weight: 600 !important;
    }
    /* 캡션/보조 텍스트 대비 개선 */
    [data-testid="stCaptionContainer"] p,
    .stCaption {
        color: #d8f0ee !important;
        opacity: 1 !important;
    }
    label, .stSlider label {
        color: #d8f0ee !important;
    }
    /* 마크다운 제목(###) 및 일반 본문 텍스트 대비 개선 */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3,
    .stMarkdown h4, .stMarkdown h5, .stMarkdown h6,
    .stMarkdown p {
        color: #eafffb !important;
        opacity: 1 !important;
    }
</style>
""", unsafe_allow_html=True)


def ball_color(n: int) -> str:
    # 실제 로또 공 색상 규칙과 유사하게
    if n <= 10:
        return "#fbc400"  # 노랑
    elif n <= 20:
        return "#69c8f2"  # 파랑
    elif n <= 30:
        return "#ff7272"  # 빨강
    elif n <= 40:
        return "#aaaaaa"  # 회색
    else:
        return "#b0d840"  # 초록


def parse_excluded(text: str):
    """'4, 13, 27' 같은 문자열을 파싱해서 (제외숫자 set, 잘못된 입력 목록)을 반환"""
    excluded = set()
    invalid = []
    for token in text.split(","):
        token = token.strip()
        if not token:
            continue
        if token.isdigit() and 1 <= int(token) <= 45:
            excluded.add(int(token))
        else:
            invalid.append(token)
    return excluded, invalid


def draw_sets(n_sets: int, excluded: set):
    pool = [n for n in range(1, 46) if n not in excluded]
    results = []
    for _ in range(n_sets):
        results.append(sorted(random.sample(pool, 6)))
    return results


st.markdown('<div class="main-title">🍀 행운의 로또 번호</div>', unsafe_allow_html=True)
st.markdown(f'<div class="sub-caption">{date.today().strftime("%Y년 %m월 %d일")} 추천 번호</div>', unsafe_allow_html=True)

exclude_text = st.text_input(
    "제외하고 싶은 번호 (쉼표로 구분)",
    placeholder="예: 4, 13, 27",
    label_visibility="collapsed",
)
n_sets = st.slider("몇 세트를 뽑을까요?", min_value=1, max_value=5, value=1)

excluded_numbers, invalid_tokens = parse_excluded(exclude_text)

if invalid_tokens:
    st.warning(f"이 값은 무시했어요 (1~45 사이 숫자만 가능): {', '.join(invalid_tokens)}")

pool_size = 45 - len(excluded_numbers)
if pool_size < 6:
    st.error("제외한 번호가 너무 많아요. 최대 39개까지만 제외할 수 있습니다.")
    can_draw = False
else:
    can_draw = True

if "lotto_results" not in st.session_state:
    st.session_state.lotto_results = None

button_label = "번호 뽑기 🎱" if st.session_state.lotto_results is None else "다시 뽑기 🔄"

if can_draw and st.button(button_label, use_container_width=True):
    st.session_state.lotto_results = draw_sets(n_sets, excluded_numbers)
    st.rerun()

if st.session_state.lotto_results:
    all_rows_html = '<div class="results-container">'
    for i, numbers in enumerate(st.session_state.lotto_results):
        row_html = '<div class="set-row">'
        if len(st.session_state.lotto_results) > 1:
            row_html += f'<div class="set-label">{i + 1}세트</div>'

        row_html += '<div class="ball-row">'
        for n in numbers:
            color = ball_color(n)
            row_html += f'<div class="ball" style="background:{color};">{n}</div>'
        row_html += "</div></div>"
        all_rows_html += row_html
    all_rows_html += "</div>"
    st.markdown(all_rows_html, unsafe_allow_html=True)

    st.markdown("### 🎁 오늘의 번호로 행운을 더 끌어올리고 싶다면")

    col1, col2 = st.columns(2)
    with col1:
        st.link_button("쿠팡에서 행운템 보기 🛒", COUPANG_LINK, use_container_width=True)
    with col2:
        st.link_button("토스로 용돈 받기 💰", TOSS_LINK, use_container_width=True)

    st.caption(
        "ℹ️ 이 포스팅은 쿠팡 파트너스 활동의 일환으로, "
        "이에 따른 일정액의 수수료를 제공받을 수 있습니다."
    )
    st.caption("※ 본 서비스는 재미로 보는 참고용이며, 당첨을 보장하지 않습니다.")

    share_url = "https://autolotto.streamlit.app/"
    st.markdown("👇 **친구에게 공유하기**")
    components.html(f"""
    <div style="display:flex; gap:8px; align-items:center; font-family: sans-serif;">
        <input id="shareUrlLotto" type="text" readonly value="{share_url}"
            style="flex:1; padding:10px 14px; border-radius:20px; border:1px solid rgba(255,255,255,0.2);
                   background:rgba(255,255,255,0.08); color:#eafffb; font-size:0.9rem; outline:none;">
        <button onclick="copyLottoLink(event)"
            style="padding:10px 18px; border-radius:20px; border:none;
                   background:linear-gradient(90deg,#78ffd6,#a8ff78); color:#0f2027;
                   font-weight:700; cursor:pointer; white-space:nowrap; font-size:0.9rem;">
            복사 📋
        </button>
    </div>
    <script>
    function copyLottoLink(event) {{
        var copyText = document.getElementById("shareUrlLotto");
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
    st.info("제외할 번호가 있다면 입력하고, 버튼을 눌러 오늘의 행운 번호를 뽑아보세요!")
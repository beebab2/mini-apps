# -*- coding: utf-8 -*-
import streamlit as st
import random
from datetime import date, datetime
from missions_data import MISSIONS, CATEGORY_ICONS

# ------------------------------
# 기본 설정
# ------------------------------
st.set_page_config(
    page_title="오늘 딱 하나",
    page_icon="✅",
    layout="centered",
)

# 기존 앱들과 통일된 다크 네이비 + 민트 팔레트 (공용 config.toml과 무관하게 완전히 자체 지정)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #0f2027 0%, #16323d 100%) !important;
    }

    /* 기본 텍스트/제목 색상을 명시적으로 고정 (공용 테마와 무관하게 항상 동일하게) */
    h1, h2, h3, p, span, label, .stMarkdown, .stCaption, div[data-testid="stExpander"] summary {
        color: #eafffb !important;
    }

    .block-container {
        padding-top: 2.5rem;
        max-width: 640px;
    }

    .app-title {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        color: #78ffd6 !important;
        margin-bottom: 4px;
        letter-spacing: -0.3px;
    }

    .app-subtitle {
        text-align: center;
        color: #9fd8cf !important;
        font-size: 14px;
        margin-bottom: 24px;
        line-height: 1.6;
    }

    .main-card {
        background: linear-gradient(135deg, #0fb9b1 0%, #14b8a6 55%, #2dd4bf 100%);
        border-radius: 28px;
        padding: 48px 28px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 16px 36px rgba(15, 185, 177, 0.35);
        border: 1px solid rgba(255,255,255,0.2);
    }
    .main-card .mission-emoji,
    .main-card .mission-text {
        color: #06282a !important;
    }
    .mission-emoji {
        font-size: 56px;
        margin-bottom: 18px;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.12));
    }
    .mission-text {
        font-size: 21px;
        font-weight: 700;
        line-height: 1.6;
        letter-spacing: -0.2px;
    }
    .streak-badge {
        display: inline-block;
        background-color: rgba(120, 255, 214, 0.12);
        color: #78ffd6 !important;
        padding: 7px 18px;
        border-radius: 20px;
        font-weight: 700;
        font-size: 14px;
        margin-top: 4px;
        border: 1px solid rgba(120, 255, 214, 0.35);
    }
    .category-chip {
        display: inline-block;
        background-color: rgba(120, 255, 214, 0.1);
        color: #78ffd6 !important;
        padding: 6px 16px;
        border-radius: 14px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 14px;
        border: 1px solid rgba(120, 255, 214, 0.3);
    }
    .info-box {
        background-color: rgba(120, 255, 214, 0.08);
        border: 1px solid rgba(120, 255, 214, 0.3);
        border-radius: 16px;
        padding: 14px 18px;
        color: #d7fff3 !important;
        font-size: 14.5px;
        margin: 16px 0 10px 0;
    }
    .success-box {
        background-color: rgba(134, 239, 172, 0.1);
        border: 1px solid rgba(134, 239, 172, 0.35);
        border-radius: 16px;
        padding: 14px 18px;
        color: #bbf7d0 !important;
        font-size: 14.5px;
        margin: 16px 0 10px 0;
    }
    .cta-card {
        display: block;
        background-color: rgba(253, 186, 116, 0.1);
        border: 1.5px solid rgba(253, 186, 116, 0.5);
        border-radius: 18px;
        padding: 18px;
        margin-top: 6px;
        text-align: center;
        text-decoration: none;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .cta-card:hover {
        transform: translateY(-2px);
        background-color: rgba(253, 186, 116, 0.16);
    }
    .cta-card span {
        font-size: 15.5px;
        color: #fdba74 !important;
        font-weight: 700;
    }
    .footnote {
        text-align: center;
        color: #6b8f8a !important;
        font-size: 12px;
        margin-top: 6px;
    }

    div.stButton > button {
        border-radius: 14px;
        height: 52px;
        font-weight: 700;
        font-size: 16px;
        border: none;
        transition: transform 0.12s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-1px);
    }
    div.stButton > button[kind="primary"] {
        background-color: #0fb9b1;
        color: #06282a !important;
    }
    div.stButton > button[kind="secondary"] {
        background-color: rgba(255,255,255,0.05);
        color: #eafffb !important;
        border: 1.5px solid rgba(120, 255, 214, 0.35) !important;
    }

    div[data-testid="stExpander"] {
        border-radius: 16px;
        border: 1px solid rgba(120, 255, 214, 0.25);
        background-color: rgba(255,255,255,0.03);
    }

    div[data-testid="stCheckbox"] label p {
        color: #eafffb !important;
        font-size: 15px;
    }

    div[data-testid="stTextArea"] textarea {
        background-color: rgba(255,255,255,0.05) !important;
        color: #eafffb !important;
        border: 1px solid rgba(120, 255, 214, 0.25) !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# 세션 상태 초기화
# ------------------------------
if "selected_categories" not in st.session_state:
    st.session_state.selected_categories = []
if "onboarded" not in st.session_state:
    st.session_state.onboarded = False
if "today_result" not in st.session_state:
    st.session_state.today_result = None
if "action_taken" not in st.session_state:  # None, "done", "skip"
    st.session_state.action_taken = None
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "last_done_date" not in st.session_state:
    st.session_state.last_done_date = None


def pick_today_mission():
    """오늘 날짜를 시드로 사용해 선택된 카테고리 중 하나의 미션을 고정 랜덤으로 뽑음"""
    categories = st.session_state.selected_categories
    if not categories:
        categories = list(MISSIONS.keys())

    today_str = date.today().isoformat()
    seed_str = today_str + "".join(sorted(categories))
    rng = random.Random(seed_str)

    chosen_category = rng.choice(categories)
    chosen_mission = rng.choice(MISSIONS[chosen_category])
    return chosen_category, chosen_mission


# ------------------------------
# 1) 온보딩 화면 (최초 1회)
# ------------------------------
if not st.session_state.onboarded:
    st.markdown("<div class='app-title'>✅ 오늘 딱 하나</div>", unsafe_allow_html=True)
    st.markdown(
        "<div class='app-subtitle'>매일 미루던 작은 일, 딱 하나만 콕 집어 알려드릴게요.<br>"
        "번거로운 목록 관리는 필요 없어요.</div>",
        unsafe_allow_html=True
    )
    st.write("")
    st.markdown("**관심 있는 카테고리를 선택해주세요** (복수 선택 가능)")

    cols = st.columns(2)
    picked = []
    for i, cat in enumerate(MISSIONS.keys()):
        with cols[i % 2]:
            icon = CATEGORY_ICONS.get(cat, "🔹")
            if st.checkbox(f"{icon} {cat}", key=f"cb_{cat}"):
                picked.append(cat)

    st.write("")
    if st.button("시작하기", type="primary", use_container_width=True):
        if not picked:
            st.warning("최소 1개 이상 선택해주세요!")
        else:
            st.session_state.selected_categories = picked
            st.session_state.onboarded = True
            st.rerun()

# ------------------------------
# 2) 메인 화면 - 오늘의 미션
# ------------------------------
else:
    if st.session_state.today_result is None:
        st.session_state.today_result = pick_today_mission()

    category, mission = st.session_state.today_result

    st.markdown("<div class='app-title' style='font-size:26px;'>✅ 오늘 딱 하나</div>", unsafe_allow_html=True)

    icon = CATEGORY_ICONS.get(category, "🔹")
    st.markdown(f"<div style='text-align:center;'><span class='category-chip'>{icon} {category}</span></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="main-card">
        <div class="mission-emoji">{mission['emoji']}</div>
        <div class="mission-text">{mission['text']}</div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.streak > 0:
        st.markdown(
            f"<div style='text-align:center;'><span class='streak-badge'>🔥 연속 {st.session_state.streak}일째</span></div>",
            unsafe_allow_html=True
        )
        st.write("")

    # 아직 오늘 액션을 안 한 경우
    if st.session_state.action_taken is None:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("했어요 ✅", type="primary", use_container_width=True):
                st.session_state.action_taken = "done"
                today = date.today()
                if st.session_state.last_done_date is None:
                    st.session_state.streak = 1
                else:
                    st.session_state.streak += 1
                st.session_state.last_done_date = today
                st.rerun()
        with col2:
            if st.button("귀찮아요, 시킬래요 🛒", use_container_width=True):
                st.session_state.action_taken = "skip"
                st.rerun()

    # "했어요" 선택 후
    elif st.session_state.action_taken == "done":
        st.markdown(
            "<div class='success-box'>잘하셨어요! 작은 실천이 쌓이면 큰 변화가 돼요 🎉</div>",
            unsafe_allow_html=True
        )
        st.balloons()

        share_text = f"오늘의 미션: {mission['emoji']} {mission['text']} — 다 끝냈어요! 너도 확인해봐 👉"
        st.text_area("친구에게 공유하기", value=share_text, height=80)

    # "귀찮아요" 선택 후 - 제휴 링크 노출
    elif st.session_state.action_taken == "skip":
        st.markdown(
            "<div class='info-box'>괜찮아요! 미리 하나 시켜두면 이제 신경 안 써도 돼요 😊</div>",
            unsafe_allow_html=True
        )

        # ⚠️ 실제 쿠팡 파트너스 링크로 교체 필요
        coupang_search_url = f"https://www.coupang.com/np/search?q={mission['keyword']}"

        st.markdown(f"""
        <a href="{coupang_search_url}" target="_blank" class="cta-card">
            <span>🛒 '{mission['keyword']}' 지금 확인하러 가기</span>
        </a>
        """, unsafe_allow_html=True)

        st.markdown("<div class='footnote'>이 링크를 통해 구매 시 일정 수수료를 받을 수 있습니다.</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    with st.expander("⚙️ 카테고리 다시 선택하기"):
        st.write("현재 선택된 카테고리:", ", ".join(st.session_state.selected_categories))
        if st.button("카테고리 재설정"):
            st.session_state.onboarded = False
            st.session_state.selected_categories = []
            st.session_state.today_result = None
            st.session_state.action_taken = None
            st.rerun()

import streamlit as st
import math

# 페이지 설정
st.set_page_config(
    page_title="BMI 계산기 🏃‍♀️",
    page_icon="💪",
    layout="centered"
)

# 커스텀 CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF6B6B 0%, #FFE66D 100%);
        color: white;
        font-size: 20px;
        font-weight: bold;
        padding: 15px;
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .result-box {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        margin: 20px 0;
        text-align: center;
    }
    .character {
        font-size: 100px;
        animation: bounce 2s infinite;
    }
    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
    }
    .metric-card {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# BMI 계산 함수
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

# BMI 분류 및 조언
def get_bmi_category(bmi):
    if bmi < 18.5:
        return {
            'category': '저체중',
            'character': '🥺',
            'color': '#4ECDC4',
            'advice': '조금 더 드시는 게 좋겠어요! 영양가 있는 음식으로 건강하게 체중을 늘려보세요.',
            'tips': [
                '🍗 단백질이 풍부한 음식 섭취하기',
                '🥜 견과류로 건강한 칼로리 보충하기',
                '🏋️‍♀️ 근력 운동으로 근육량 늘리기',
                '😴 충분한 휴식 취하기'
            ],
            'emoji_bg': '🌱🌿🍀'
        }
    elif 18.5 <= bmi < 23:
        return {
            'category': '정상',
            'character': '🥳',
            'color': '#95E1D3',
            'advice': '완벽해요! 지금 상태를 잘 유지하세요. 건강한 생활습관을 계속 이어가세요!',
            'tips': [
                '🥗 균형 잡힌 식사 유지하기',
                '🏃‍♀️ 주 3-4회 규칙적인 운동하기',
                '💧 하루 2L 물 마시기',
                '😊 스트레스 관리 잘하기'
            ],
            'emoji_bg': '⭐✨💫'
        }
    elif 23 <= bmi < 25:
        return {
            'category': '과체중',
            'character': '😅',
            'color': '#FFB6B9',
            'advice': '살짝 주의가 필요해요. 가벼운 운동과 식단 조절로 건강을 지켜보세요!',
            'tips': [
                '🥗 야채와 과일 섭취 늘리기',
                '🚶‍♀️ 하루 30분 걷기 습관들이기',
                '🚫 야식과 간식 줄이기',
                '📱 식사 일기 쓰기'
            ],
            'emoji_bg': '💪🔥💫'
        }
    else:
        return {
            'category': '비만',
            'character': '😰',
            'color': '#FF6B9D',
            'advice': '다이어트를 시작해볼까요? 천천히, 건강하게 체중을 감량하는 것이 중요해요!',
            'tips': [
                '🏃‍♂️ 유산소 운동 주 5회 이상',
                '🥗 채소 위주의 식단으로 변경',
                '💧 물 많이 마시기 (하루 2L 이상)',
                '👨‍⚕️ 전문가 상담 고려하기',
                '😴 충분한 수면 (7-8시간)',
                '📉 작은 목표부터 시작하기'
            ],
            'emoji_bg': '🔥💪🎯'
        }

# 헤더
st.markdown("<h1 style='text-align: center; color: white; font-size: 48px;'>💪 BMI 계산기 🏃‍♀️</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>당신의 건강 상태를 확인해보세요!</h3>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# 입력 폼
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### 🔢 키 (cm)")
    height = st.number_input("키를 입력하세요", min_value=100, max_value=250, value=170, step=1, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("### ⚖️ 몸무게 (kg)")
    weight = st.number_input("몸무게를 입력하세요", min_value=30, max_value=200, value=65, step=1, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 계산 버튼
if st.button("🎯 BMI 계산하기!", use_container_width=True):
    # BMI 계산
    bmi = calculate_bmi(weight, height)
    result = get_bmi_category(bmi)
    
    # 결과 저장
    st.session_state.bmi = bmi
    st.session_state.result = result

# 결과 표시
if 'bmi' in st.session_state and 'result' in st.session_state:
    bmi = st.session_state.bmi
    result = st.session_state.result
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 결과 박스
    st.markdown(f"""
    <div class='result-box' style='border: 5px solid {result["color"]}; background: linear-gradient(135deg, white 0%, {result["color"]}22 100%);'>
        <div class='character'>{result['character']}</div>
        <h1 style='color: {result["color"]}; margin: 20px 0;'>BMI: {bmi}</h1>
        <h2 style='color: {result["color"]}; margin: 10px 0;'>{result['category']}</h2>
        <p style='font-size: 18px; color: #333; margin: 20px 0; line-height: 1.6;'>{result['advice']}</p>
        <div style='font-size: 30px; margin: 20px 0;'>{result['emoji_bg']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # BMI 차트
    st.markdown("### 📊 BMI 범위 차트")
    
    # 컬러풀한 BMI 막대
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        status = "🎯" if bmi < 18.5 else ""
        st.markdown(f"""
        <div style='background: #4ECDC4; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
            <h3>저체중</h3>
            <p>< 18.5</p>
            <div style='font-size: 30px;'>{status}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        status = "🎯" if 18.5 <= bmi < 23 else ""
        st.markdown(f"""
        <div style='background: #95E1D3; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
            <h3>정상</h3>
            <p>18.5-22.9</p>
            <div style='font-size: 30px;'>{status}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        status = "🎯" if 23 <= bmi < 25 else ""
        st.markdown(f"""
        <div style='background: #FFB6B9; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
            <h3>과체중</h3>
            <p>23-24.9</p>
            <div style='font-size: 30px;'>{status}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        status = "🎯" if bmi >= 25 else ""
        st.markdown(f"""
        <div style='background: #FF6B9D; padding: 20px; border-radius: 10px; text-align: center; color: white;'>
            <h3>비만</h3>
            <p>≥ 25</p>
            <div style='font-size: 30px;'>{status}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 맞춤 조언
    st.markdown(f"### 💡 {result['category']}인 당신을 위한 맞춤 조언")
    
    for tip in result['tips']:
        st.markdown(f"""
        <div style='background: white; padding: 15px; margin: 10px 0; border-radius: 10px; 
                    border-left: 5px solid {result["color"]}; box-shadow: 0 2px 5px rgba(0,0,0,0.1);'>
            <p style='margin: 0; font-size: 16px; color: #333;'>{tip}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # 격려 메시지
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style='background: linear-gradient(90deg, {result["color"]} 0%, {result["color"]}88 100%); 
                padding: 20px; border-radius: 15px; text-align: center; color: white;'>
        <h3>🌟 작은 변화가 큰 차이를 만듭니다! 🌟</h3>
        <p style='font-size: 16px;'>건강한 당신을 응원합니다! 💪</p>
    </div>
    """, unsafe_allow_html=True)

# 사이드바 정보
with st.sidebar:
    st.markdown("### 📖 BMI란?")
    st.info("""
    **BMI (Body Mass Index)**는 체질량지수로,
    키와 몸무게를 이용해 비만도를 측정하는 지표입니다.
    
    **계산식:**
    BMI = 체중(kg) ÷ 키(m)²
    
    **기준 (한국 기준):**
    - 저체중: 18.5 미만
    - 정상: 18.5~22.9
    - 과체중: 23~24.9
    - 비만: 25 이상
    """)
    
    st.markdown("### 🎯 건강 팁")
    st.success("""
    💧 물 많이 마시기
    🥗 채소와 과일 섭취
    🏃‍♀️ 규칙적인 운동
    😴 충분한 수면
    😊 스트레스 관리
    """)
    
    st.markdown("### 💪 Made with Love")
    st.markdown("다이어트 전문가 & 프로그래머")

# 푸터
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align: center; color: white; padding: 20px;'>
    <p>⚠️ 이 BMI 계산기는 참고용이며, 정확한 건강 상태는 전문의와 상담하세요.</p>
    <p style='font-size: 12px; opacity: 0.7;'>© 2024 BMI Calculator | Made with ❤️ by Diet Expert</p>
</div>
""", unsafe_allow_html=True)

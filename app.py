import streamlit as st
from streamlit_chat import message
from agent import graph  # Import graph từ file agent.py của bạn

# 1. Cấu hình trang & Style (Màu xanh dương chủ đạo)
st.set_page_config(page_title="TravelBuddy AI by My", page_icon="✈️")

st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stTextInput font { color: #1E3A8A; }
    div.stButton > button:first-child {
        background-color: #2563EB;
        color: white;
        border-radius: 10px;
        border: none;
        px: 20px;
    }
    .sidebar .sidebar-content { background-color: #1E3A8A; color: white; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_allow_html=True)

# 2. Khởi tạo Session State (Bộ nhớ giao diện)
if "messages" not in st.session_state:
    st.session_state.messages = []
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user_streamlit_1"

# 3. Sidebar (Thanh bên trái)
with st.sidebar:
    st.title("✈️ TravelBuddy")
    st.info("Trợ lý du lịch thông minh sử dụng LangGraph & GPT-4o.")
    if st.button("Xóa lịch sử chat"):
        st.session_state.messages = []
        st.rerun()

st.title("🌏 Lên kế hoạch du lịch")
st.caption("Hãy cho mình biết điểm đến và ngân sách của bạn!")

# 4. Hiển thị lịch sử chat
chat_container = st.container()
with chat_container:
    for i, msg in enumerate(st.session_state.messages):
        if msg["role"] == "user":
            message(msg["content"], is_user=True, key=f"{i}_user", avatar_style="adventurer")
        else:
            message(msg["content"], is_user=False, key=f"{i}_bot", avatar_style="bottts")

# 5. Xử lý Input từ người dùng
user_input = st.chat_input("Nhập tin nhắn...")

if user_input:
    # 1. Lưu tin nhắn người dùng
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    input_data = {"messages": [("user", user_input)]}
    
    with st.spinner("TravelBuddy đang thực thi..."):
        # 2. Chạy stream để bắt các sự kiện gọi tool
        for event in graph.stream(input_data, config=config):
            for node_name, value in event.items():
                last_msg = value["messages"][-1]
                
                # NẾU CÓ GỌI TOOL: Lưu log vào lịch sử chat ngay lập tức
                if hasattr(last_msg, "tool_calls") and last_msg.tool_calls:
                    for tc in last_msg.tool_calls:
                        log_content = f"🛠️ **Action:** `{tc['name']}`\n📦 **Args:** `{tc['args']}`"
                        st.session_state.messages.append({"role": "log", "content": log_content})
                
                # NẾU LÀ PHẢN HỒI CUỐI CÙNG CỦA AGENT
                if node_name == "agent" and last_msg.content:
                    st.session_state.messages.append({"role": "assistant", "content": last_msg.content})
    
    st.rerun()
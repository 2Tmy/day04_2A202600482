# day04_2A202600482
Xây dựng AI Agent với Lang-Graph
## 🌟 Tính năng nổi bật
- **Tra cứu chuyến bay:** Tự động truy xuất danh sách chuyến bay giữa các thành phố lớn dựa trên điểm đi và điểm đến.
- **Gợi ý khách sạn:** Tìm kiếm nơi lưu trú phù hợp với túi tiền, sắp xếp theo xếp hạng (Rating) và khu vực cụ thể.
- **Quản lý ngân sách:** Tự động tính toán chi phí còn lại từ tổng ngân sách ban đầu sau khi trừ các khoản chi dự kiến.
- **Giao diện hiện đại:** Sử dụng Streamlit với tông màu xanh dương chủ đạo, tích hợp nhật ký hệ thống (System Log) để theo dõi quá trình gọi Tool của Agent.

## 📂 Cấu trúc thư mục
```text
lab4_agent/
├── .env                # Lưu trữ OPENAI_API_KEY
├── system_prompt.txt   # Định nghĩa Persona, Rules và Constraints của Agent
├── tools.py            # Chứa Mock Data và định nghĩa các Python Function (@tool)
├── agent.py            # Xây dựng luồng Graph (Nodes, Edges) và logic xử lý
└── app.py              # File chạy ứng dụng web giao diện Streamlit

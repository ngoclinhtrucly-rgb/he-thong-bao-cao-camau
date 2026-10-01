from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Khởi tạo Cơ sở dữ liệu tạm thời (In-memory/SQLite)
def init_db():
    conn = sqlite3.connect('camau_edu.db')
    c = conn.cursor()
    # Bảng Đơn vị và Báo cáo
    c.execute('''CREATE TABLE IF NOT EXISTS units (id INTEGER PRIMARY KEY, name TEXT, type TEXT, parent_id INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, unit_id INTEGER, status TEXT, submitted_at TEXT)''')
    
    # Dữ liệu giả lập ban đầu (Dựa trên file phân tích)
    c.execute("INSERT OR IGNORE INTO units (id, name, type) VALUES (1, 'Sở GDĐT Cà Mau', 'SO')")
    c.execute("INSERT OR IGNORE INTO units (id, name, type, parent_id) VALUES (2, 'Phường An Xuyên', 'XA', 1)")
    c.execute("INSERT OR IGNORE INTO units (id, name, type, parent_id) VALUES (3, 'Tiểu học Phường An Xuyên', 'TRUONG', 2)")
    
    # Giả lập trạng thái nộp báo cáo
    c.execute("INSERT OR IGNORE INTO reports (id, unit_id, status) VALUES (1, 3, 'DA_GUI')")
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def dashboard():
    # Phục vụ giao diện Dashboard cho Quản trị Sở
    return render_template('index.html')

@app.route('/api/stats')
def get_stats():
    # API cung cấp số liệu tổng quan toàn tỉnh
    return jsonify({
        "tong_so_truong": 148,
        "tong_xa_phuong": 65,
        "da_nop": 85,
        "chua_nop": 50,
        "co_loi": 13,
        "tyle_hoanthanh": "57.4%"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
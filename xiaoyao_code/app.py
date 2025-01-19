from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# 数据库连接配置
def get_db_connection():
    conn = mysql.connector.connect(
        host="43.139.231.65",
        user="root",
        password="xdXYpm.123456",  # 替换为你的数据库密码
        database="scraper_data"
)        
    return conn

@app.route('/')
def home():
    # 从数据库中获取数据
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 假设数据存储在 web_data 表中
    cursor.execute("SELECT title, paragraph FROM web_data")
    data = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 将数据传递给模板进行渲染
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

import mysql.connector

# 数据库连接配置
db = mysql.connector.connect(
    host="43.139.231.65",
    user="root",
    password="xdXYpm.123456",  # 替换为你的数据库密码
    database="scraper_data"
)

cursor = db.cursor()

# 示例数据
title = "Example Title"
paragraph = "This is an example paragraph."

# 插入数据
sql = "INSERT INTO web_data (title, paragraph) VALUES (%s, %s)"
values = (title, paragraph)
cursor.execute(sql, values)

# 提交事务
db.commit()
print(f"Inserted {cursor.rowcount} row(s) into the database.")

# 关闭连接
cursor.close()
db.close()

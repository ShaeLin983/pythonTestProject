import pymysql

try:
    # 1.链接数据库，连接对象connect()
    conn = pymysql.Connect(
        host="localhost",
        port=3306,
        db='database',
        user='root',
        passwd='admin',
        charset='utf8'
    )
    # 2.创建游标对象cursor()
    cur = conn.cursor()

    # 增加
    insert = 'insert into subjects values(0,"go语言") '
    result = cur.execute(insert)
    print(result)

    # 修改
    update = 'update subjects set title="区块链" where id=7'
    result = cur.execute(update)

    # 删除
    delete = 'delete from subjects where id=3'
    result = cur.execute(delete)

    # 提交事务
    conn.commit()
    # 关闭游标
    cur.close()
    # 关闭链接
    conn.close()
except Exception as e:
    print(e)

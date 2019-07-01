import pymongo

try:

    # 1.链接mongoDB服务
    mongo = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

    # 2.建库和表
    collection = mongo.database.stu

    """
    建立了一个database数据库和表stu，也可以分步骤进行。
    db = mongo['six']
    collection = db['stu']
    加中括号这种写法也能识别
    collection = mongo['six']['stu']
    """

    # 3.插入数据
    one = {"name": "张三", "age": 50}
    collection.insert_one(one)
    for i in collection.find():
        print(i)

except Exception as e:
    print(e)

finally:
    # 关闭数据库
    mongo.close()

"""
显示 error：10061 由于目标计算机积极拒绝，无法连接。解决方法：
打开cmd ,输入 mongodb bin路径+mongod.exe --config E:\mongo.config
"""

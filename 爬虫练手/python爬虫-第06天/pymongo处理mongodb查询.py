import pymongo
client = pymongo.MongoClient()
stu = pymongo.MongoClient().test.stu
stu.find()
cursor = stu.find()
for item in cursor:
    print(item)

list(stu.find())
list(stu.find().skip(3).limit(2))
list(stu.find({"age" : {"$gte" : 18}}).skip(3).limit(2))
list(stu.find({"age" : {"$gte" : 18}}))

list(stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}))

stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}, sort={"age" : 1})
stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}, sort=[("age", 1)])
list(stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}, sort=[("age", 1)]))
list(stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}, sort=[("age", 1), ("name" : -1)]))
list(stu.find({"age" : {"$gte" : 18}}, {"name" : 1, "age" : 1}, sort=[("age", 1), ("name",-1)]))


sorted(item_list, key=lambda x : x['age'], reverse=True)


stu.count()
stu.count({"age" : {"$gte" : 18}})
stu.find()
stu.find().count()
stu.distinct("hometown")
stu.distinct("hometown", {"age" : {"$gte" : 20}})

%hist -f pymongo处理mongodb查询.py

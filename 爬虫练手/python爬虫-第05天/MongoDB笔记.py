


SQL：（MySQL、Oracle、SQL Server、DB2）
1. 高度事务性的场景，银行、会计、贸易、库管，需要大量原子性操作
2. 数据存储要求有规范的多表结构设计，预定义明确的字段
3. 数据价值高，对安全和稳定性要求高
4. 需要持久化存储的 "冷数据"（不需要经常读写的数据）
5. 需要通过SQL语句支持的存储场景


NoSQL：
    Redis   key:value(string、list、hash、set、zset)
    MongoDB  {key1 : value1, key2 : value2}, {key1 : value1}
1. 高度伸缩性场景，更容易扩展，支持集群
2. 灵活的数据结构，不需要事先设计数据库数据表字段，即用即存，社交网络、热点资讯
3. 处理 "热数据"（需要经常读写的数据），NoSQL大部分操作都是和内存交互，读写效率极高
4. 不需要SQL语句支持，学习成本低



32bit:  内存最大的寻址范围 2^32



MySQL 3306
Redis 6379
MongoDB 27017

127.0.0.1

MongoDB 服务和客户端 命令：

1. 开启数据库服务： sudo mongod
2. 开始shell客户端： mongo
3. 关闭 shell客户端 和 数据库服务， ctrl + c
4. 在admin数据库下，通过 db.shutdownServer() 来关闭服务


MongoDB数据库操作的常用命令：

1. 表示当前所在的数据库
> db

2. 查看所有的数据库
> show dbs

3. 切换到指定数据库
> use mydb

4. 查看当前数据库下的所有集合（相当于SQL的表）
> show collections

5. 查看当前数据库下 指定集合 的所有文档（相当于 每一条数据）
> db.mycollection.find()

6. 删除当前数据库的 指定集合
> db.mycollection.drop()

7. 删库
> db.dropDatabase()


不要把 生产环境 当成 测试环境。


MongoDB 的 用户权限：
1. 第一次进入到MongoDB没有用户，所以是root权限，
    需要先创建一个有root权限的用户:
    > use admin
    > db.createUser()

    在使用这个用户创建其他用户
    > db.auth()

2. 第二次开启MongoDB服务，要通过 --auth 启动用户权限模式，才可以让用户权限生效。
    > use admin
    > db.auth()





------------------  MongoDB 增加数据 ： insert

1. insert() 接收一个文档 参数

> db.stu.insert({ "_id" : 1, "name" : "诸葛亮", "age" : 40, "hometown" : "蜀" })

2. 构建空文档，添加字段，再写入

> data = {}
> data._id = 2
> data.name = "刘备"
> data.age = 48
> data.hometown = "蜀"

db.stu.insert(data)



------------------  MongoDB 删除数据 ： remove

1. 删除所有符合条件的文档,也可以同时指定多个条件
> db.stu.remove({"age" : 18})
> db.stu.remove({"age" : 18, "hometown" : "蜀"})

2. 只删除第一个符合条件的文档，通过添加第二个参数 {justOne : true}

> db.stu.remove({"age" : 18}, {justOne : true})

3. 不添加任何条件，则删除全部文档
> db.stu.remove()
> db.stu.drop()


------------------  MongoDB 修改数据 ： update

update() 至少需要两个参数，第一个参数为匹配条件，第二个参数为修改内容（可添加第三个参数表示是否全部匹配）

1.  将第一个符合条件的文档，替换为 第二个参数对应的文档（整个文档替换）
# 将第一个 age 为48的文档，替换为 {age : 49}， 但是 _id 保持不变
> db.stu.update({age : 48}, {age : 49})


2. 如果只修改特定字段，通过 $set 修饰符处理          （局部文档修改）
# 将第一个age为48的文档，修改age为49，其他字段保持不变
> db.stu.update({age : 48}, {$set : {age : 49}})
# 将第一个age为48的文档，修改age为49，并添加gender字段，其他字段保持不变
> db.stu.update({age : 48}, {$set : {age : 49, gender : true}})


3. 默认只处理第一条符合条件的文档，通过第三个参数 {multi : true} 表示全部处理 （修改所有文档）
# 将所有age为48的文档，修改age为49，其他字典不变
> db.stu.update({age : 48}, {$set : {age : 49}}, {multi : true})



------------------  MongoDB 新增+修改数据 ： save

save() 需要一个文档参数，根据文档的 _id 来处理，

1. 如果_id 存在，则修改数据，
> db.stu.save({_id : 1, name : "马超", age : 36, hometown : "蜀"})

2. 如果_id 不存在则新增
db.stu.save({_id : 5, name : "黄忠", age : 56, hometown : "蜀"})


insert() 如果_id存在则报错， save则修改数据
update() 修改数据可以指定字段修改，save则全部替换。



# pip install pymongo
import pymongo

client = pymongo.MongoClient(host='127.0.0.1', port=27017)
client.test.stu.insert({})
client.test.stu.insert([{}, {}, {}])
client.test.stu.find({})



------------------  MongoDB 查询数据 ： find()

1. find()  和  findOne()
find() 查询所有符合条件的文档
findOne() 查询第一个符合条件的文档

> db.stu.find({age : 18, hometown : "桃花岛"})
> db.stu.findOne({age : 18})




2. 比较运算符（通常用于比较数据，如果是字符串则比较字节码）

默认是 等于
$gt  大于
$gte 大于等于
$lt  小于
$lte 小于等于
$ne  不等于

> db.stu.find({age : 18})
> db.stu.find({age : {$gt : 18}})



3. 逻辑运算符（用于表示多个 独立条件的逻辑关系）

$and  和 $or  用来修饰多个条件的 数组

> db.stu.find({age : 18, hometown : "桃花岛"})

> db.stu.find( {$or : [{age : 18}, {hometown : "桃花岛"}]})

> db.stu.find( {$or : [ {$and : [{age : 18}, {hometown : "桃花岛"}]}, {gender : true}]})


4. 范围运算符

$in 在
$nin 不在

# 查找age 不是 16 18 20 的文档信息
db.stu.find({age : {$nin : [16, 18, 20]}})

# 查找age 是 16 18 20 ， 同时 hometown 是 蒙古 或 大理
db.stu.find({age : {$in : [16, 18, 20]}, hometown : {$in : ["蒙古", "大理"]}})


5. 正则表达式

# 按正则表达式匹配文档， / / 内写的正则表达式匹配文本
db.stu.find({name : /^黄/})

# 通过 $regex修饰 启动正则匹配文本
db.stu.find({name : {$regex : "^黄"}})

# 通过 $options 启动正则修饰 ,如 $i 表示 忽略英文大小写
db.stu.find({name : {$regex : "^Big", $options : "$i"}})



6. 自定义函数查询  $where (了解)
db.stu.find({$where : function() { return this.age != 20 }

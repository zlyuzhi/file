


----------- 对find() 查询结果的处理：

1. limit() 和 skip()

limit() 表示开始显示多少个
> db.stu.find().limit(3)

skip() 表示跳过多少个开始显示
> db.stu.find().skip(3)

如果 limit()和 skip()组合使用，执行结果一定是先 执行 skip() 再执行 limit()
> db.stu.find().skip(3).limit(3)


2. 投影显示
当find() 添加第二个参数，表示启用投影，可以指定字段显示

-1. 通过 1 和 true 指定显示字段，默认其他字段不显示
> db.stu.find({}, {name : 1, age : true})

-2. 通过 0 和 false 指定不显示字段，默认其他字段显示
> db.stu.find({}, {name : 0, hometown: false})

默认情况下，_id 是一定显示的，除非手动指定不显示
> db.stu.find({}, {name : 0, hometown: false, _id : 0})


3. sort() 排序

sort() 指定任意字段排序，1 为升序， -1 为降序，通常对数字排序，如果是字符串则按首字母的ascii值排序

-1. 单个排序
# 按年龄进行升序排序
> db.stu.find().sort({age : 1})

-2 多个排序：先执行第一个排序，如果出现重复值，再按第二个排序处理
# 先按age进行升序排序，如果有age相同的文档，再按 gender 降序排序
> db.stu.find().sort({age : 1, gender : -1})


4. count() 统计个数

-1. 在find()后添加 count() 统计文档个数
> db.stu.find({age : {$gte : 18}}).count()

-2. 代替find() 直接统计个数
> db.stu.count()
> db.stu.count({age : {$gte : 18}})


5. distinct() 去重显示

-1. 直接显示指定字段去重后的 数组
> db.stu.distinct("hometown")


-2. 配合查询条件，显示符合条件的文档中 指定字段的值
> db.stu.distinct("hometown", {age : {$gte : 18}})



数据分析：统计+概率

----------- MongoDB 的聚合运算

aggregate([ {$match}, {$group}, {}   ])


1. $group 分组统计

对所有文档按 gender进行分组，再分别统计每组 age 的总和

-1 $sum 求和统计计算


-2 $sum : 1 统计个数


-3 $avg : 统计平均数


-4 $max 和 $min  求最大值和最小值


-5 $first 和 $last 求第一个和最后一个



db.stu.aggregate([
    {
        $group : {
            # 表示分组依据
            _id : "$gender",
            # 统计 文档个数
            count : {$sum : 1},
            # 统计 age 总和
            sum_age : {$sum : "$age"},
            # 统计 age 平均数
            avg_age : {$avg : "$age"},
            # 统计 age 最大值
            max_age : {$max : "$age"},
            # 统计 age 最小值
            min_age : {$min : "$age"},
            # 统计 第一个 name
            first_name : {$first : "$name"},
            # 统计 最后一个 name
            last_name : {$last : "$name"},
            # 统计所有hometown 并保存在数组中
            all_hometown : {$push : "$hometown"}
        }
    },
    {

    }
])


2. $match 文档条件匹配（通过配合$group做预处理，将符合条件的文档再通过group分组统计）

db.stu.aggregate([
    # 先找出所有 hometown 不为 汉 文档
    {$match : {"hometown" : {$nin : ["汉"]}}},
    # 在match匹配结果里，按 gender进行分组，再统计所有文档的 name
    {$group : {_id : "$gender", all_name : {$push : "$name"}}}
])

3. $project 投影显示


db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$project : {_id : 0, max_age : 1}}])




4. $sort 排序处理

db.stu.aggregate([
    {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}},
    {$sort : {min_age : 1, max_age : -1}}
])



5. $limit 和 $skip
> db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$sort : {min_age : 1, max_age : -1}}, {$limit : 3}, {$skip : 2}])
{ "_id" : "蒙古", "max_age" : 20, "min_age" : 18 }
>
> db.stu.aggregate([ {$group : {_id : "$hometown", max_age : {$max : "$age"}, min_age : {$min : "$age"}}}, {$sort : {min_age : 1, max_age : -1}}, {$skip : 2}, {$limit : 3}])


# Python代码用法：
stu.aggregate([ {"$group" : {"_id" : "$hometown", "max_age" : {"$max" : "$age"}, "min_age" : {"$min" : "$age"}}}, {"$sort" : {"min_age" : 1, "max_age" : -1}}, {"$skip" : 2}, {"$limit" : 3}])

6. $unwind
db.stu.aggregate([ {$group : {_id : "$hometown", all_name : {$push : "$name"}}}, {$unwind : "$all_name"} ])




----------  MongoDB的索引操作 （索引是在集合为单位）

for(i=0;i<100000;i++)
{
    db.data.insert({_id : i, name : "name"+i, age : i+10})
}

0. 查看find() 执行状态

> db.data.find({_id : 10240}).explain("executionStats")


1. 查看索引，每个索引对应 一个name 索引名
> db.data.getIndexes()


2. 创建索引
> db.data.ensureIndex({name : 1})


3. 删除索引 （根据索引名删除，通过getIndexes()查看）
> db.data.dropIndex("name_1")




------------  MongoDB 的集合数据 导出 和 导入 （以集合为单位）


1. 将指定数据库 指定集合 的数据 导出为 json 或 csv
# 默认输出为json
sudo mongoexport -d test -c stu -o ./stu.json
# 通过--type指定导出为csv文件，并通过 -f 添加字段
sudo mongoexport -d test -c stu -o ./stu.csv --type csv -f "_id,name,age,hometown,gender"


2. 将json文件导入到 mongodb 指定的数据库 指定的集合里
sudo mongoimport -d test -c stu --file ./stu.json


--------------  MongoDB 数据库的 备份和恢复（以数据库为单位）


1. 数据库的备份

# 将 -h 指定的MongoDB服务器 的 -d 指定的数据库，备份到-o指定的目录中
$ sudo mongodump -h 192.168.37.80  -d test -o ./mongo_data/

2. 数据库的恢复
# 将 --dir 指定的数据库目录里的文件，恢复到 -h 指定的MongoDB服务器 的 -d指定的数据库里
$ sudo mongorestore -h 192.168.37.90 -d test --dir ./mongo_data/test


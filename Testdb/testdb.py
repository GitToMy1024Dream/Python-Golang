# -*- coding: utf-8 -*-
from django.http import HttpResponse
from TestModel.models import Test

# 1.添加数据insert
def testdb(request):
    test1 = Test(name='wenyang')
    test2 = Test(name='yangmi')
    test1.save()
    test2.save()
    return HttpResponse("<p>数据添加成功</p>")

# 2.获取数据
def testdb(request):
    # 初始化
    response = ""
    response1 = ""

    # 通过objects模型管理器的all()获得所有行，相当于select* from
    list = Test.objects.all()

    # filter相当于sql中的where
    response2 = Test.objects.filter(id=5)

    # 获得单个对象
    response3 = Test.objects.get(id=6)


    #限制返回的数据，相当于sql的offser 0 limit 2
    Test.objects.order_by('name')[0:2]

    # 数据排序
    Test.objects.order_by("name")

    Test.objects.filter(name="wenyang").order_by("id")

    # 输出所有数据
    for x in list:
        response1 += x.name + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")


# 3.更新数据

def testdb(request):
    # 修改其中一个id=1的name字段，再save，相当于SQL中的UPDATE
    # test1 = Test.objects.get(id=4)
    # test1.name = '西瓜'
    # test1.save()
    # 另一种
    Test.objects.filter(id=4).update(name='橘子')

    # 修改所有的列
    Test.objects.all().update(name="严尚香")

    return HttpResponse("<p>修改成功</p>")



# 4.删除数据

def testdb(request):
    # 删除id=4的数据
    # test1 = Test.objects.get(id=4)
    # test1.delete()
    # 另一种方式
    Test.objects.filter(id=5).delete()

    # 删除所有数据
    # Test.objects.all().delete()

    return HttpResponse("<p>删除数据成功</p>")










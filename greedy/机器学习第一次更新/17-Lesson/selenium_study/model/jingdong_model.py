from orm.field import Field
from orm.mysql_orm import Model

__author__ = "zhou"
__date__ = "2019-06-01 21:56"

class Goods(Model):
    computer_part_name = Field('computer_part_name', 'varchar(200)')
    computer_info = Field("computer_info", "text")


goods = Goods()
r = goods.select(["computer_part_name","computer_info"], ["computer_part_name='主体'"])
print(r)
r = goods.insert(['computer_part_name','computer_info'],["'我的组件名字1'","'我的组件信息1'"])
print(r)









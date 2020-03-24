
__author__ = "zhou"
__date__ = "2019-06-11 21:08"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER


# 声明一个数据库的映射

Base = declarative_base()
metadata = Base.metadata

def to_dict(self):
    return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


Base.to_dict = to_dict


class UserDict(Base):
    __tablename__ = "user"

    user_id = Column(INTEGER(11),primary_key=True)
    # user_id = Column()
    date = Column(String(100), nullable=False)
    user_name = Column(String(100), nullable=False)
    user_address = Column(String(100), nullable=False)







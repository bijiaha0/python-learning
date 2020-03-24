from crm.shared.db import db
from crm.shared.models import UserDict

__author__ = "zhou"
__date__ = "2019-06-11 21:17"

from flask import jsonify
from flask_restful import Resource, reqparse


# 解析用户输入的数据，尽量做到多种格式的兼容
parse = reqparse.RequestParser()
parse.add_argument('user_id', type=int)
parse.add_argument('date', type=str)
parse.add_argument('user_name', type=str)
parse.add_argument('user_address', type=str)
parse.add_argument('limit', type=int)
parse.add_argument('skip', type=int)


class User(Resource):

    # 创建用户的一个逻辑
    def post(self):
        args = parse.parse_args()
        date = args["date"]
        user_name = args["user_name"]
        user_address = args["user_address"]

        #数据格式转换
        user_info = UserDict(
            date=date,
            user_name=user_name,
            user_address=user_address
        )

        db.session.add(user_info)
        db.session.commit()
        return user_info.user_id, 201


    def get(self):
        args = parse.parse_args()
        user_name = args["user_name"]
        # 查询数据库
        user_info = db.session.query(UserDict.user_name,UserDict.user_address,UserDict.date).filter(
            UserDict.user_name == user_name
        ).first()

        result = {"user_name":user_info[0],"user_address":user_info[1],"date":user_info[2]}

        return jsonify(result)


class UserList(Resource):
    def get(self):
        args = parse.parse_args()
        limit = args['limit']
        skip = args['skip']

        user_filter = db.session.query(UserDict.user_name,UserDict.user_address,UserDict.date).filter()


        if limit and skip:
            user_filter = user_filter.limit(limit).offset(skip)

        users = user_filter.all()

        total_count = user_filter.count()

        # 拼接结果
        result = {
            "data": list(
                map(lambda user_info:{
                    "user_name": user_info[0],
                    "user_address": user_info[1],
                    "date": user_info[2]
                }, users)
            ),
            "totalCount": total_count
        }
        return jsonify(result)









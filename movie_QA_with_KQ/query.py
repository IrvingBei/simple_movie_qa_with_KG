#-*- coding: UTF-8 -*-
# @Time    : 2019/4/12 19:53
# @Author  : xiongzongyang
# @Site    : 
# @File    : query.py
# @Software: PyCharm

from py2neo import Graph,Node,Relationship,NodeMatcher

class Query():
    def __init__(self):
        self.graph=Graph("http://localhost:7474", username="neo4j",password="123456")

    # 问题类型0，查询电影得分
    def run(self,cql):
        # find_rela  = test_graph.run("match (n:Person{name:'张学友'})-[actedin]-(m:Movie) return m.title")
        result=[]
        find_rela = self.graph.run(cql)
        for i in find_rela:
            result.append(i.items()[0][1])
        return result




# if __name__ == '__main__':
#     SQL=Query()
#     result=SQL.run("match (m:Movie)-[]->() where m.title='卧虎藏龙' return m.rating")
#     print(result)
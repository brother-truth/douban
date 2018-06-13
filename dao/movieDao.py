# -*- coding: UTF-8 -*-

from utils.DBUtils import DBUtils
from utils.AlgorithmUtils import findAllJson2, getRecommendations
import random


host = 'localhost'
user = 'python'
password = 'python'
db = 'movie'
port = 3306


def getMovieList():
    dbutils = DBUtils(host, user, password, db, port)
    sql = 'select * from movie'
    result = dbutils.query(sql)
    movie_list = []
    for item in result:
        movie_item = {}
        movie_item['id'] = item[0]
        movie_item['movieName'] = item[1].strip()
        movie_item['src'] = item[7]
        movie_item['averating'] = item[9].strip()
        movie_list.append(movie_item)
    dbutils.close()
    return movie_list


def getHistoryList(uid):
    dbutils = DBUtils(host, user, password, db, port)
    sql = 'select distinct m.id,m.movieName,m.movieType,m.director,m.star,m.release,m.language,m.coverUrl,m.playPage,m.averageScore,' \
          'm.fileName,m.year from movie as m join history ' \
          'as h where h.uid=%d and m.id = h.mid;' % int(uid)
    result = dbutils.query(sql)
    movie_list = []
    for item in result:
        movie_item = {}
        movie_item['id'] = item[0]
        movie_item['movieName'] = item[1]
        movie_item['src'] = item[7]
        movie_item['averating'] = item[9]
        movie_list.append(movie_item)
    dbutils.close()
    return movie_list


def getMovieById(id):
    dbutils = DBUtils(host, user, password, db, port)
    sql = 'select * from movie where id=%d' % id
    result = dbutils.query(sql)
    movie = {}
    for item in result:
        movie['id'] = item[0]
        movie['name'] = item[1].strip()
        movie['src'] = item[7].strip()
        movie['averating'] = item[9].strip()
        movie['year'] = item[11]
        movie['director'] = item[3].strip()
        movie['star'] = item[4].strip()
        movie['type'] = item[2].strip()
        movie['language'] = item[6].strip()
        movie['release'] = item[5].strip()
        movie['playPage'] = item[8]
        movie['fileName'] = item[10]
    dbutils.close()
    return movie


def recordScore(uid, score, movieId):
    dbutils = DBUtils(host, user, password, db, port)
    sql = 'insert into history (uid,mid,score,dt) values (%d,%d,%d,now())' % (int(uid), int(score), int(movieId))
    dbutils.insert(sql)
    dbutils.close()


def getRecommend(uid):
    result = findAllJson2()
    recomm = getRecommendations(result, uid)
    resultjson = ''
    list1 = []
    dbutils = DBUtils(host, user, password, db, port)
    movie_list = []
    if recomm[0][1]:
        print(recomm[0][1])
        for i in range(5):
            redc = recomm[i][1]
            list1.append(redc)
        for item in list1:
            movie_item = getMovieByName(dbutils, item)
            movie_list.append(movie_item)
    else:
        sql = 'select * from movie where id<6'
        result = dbutils.query(sql)
        for item in result:
            movie_item = {}
            movie_item['id'] = item[0]
            movie_item['movieName'] = item[1].strip()
            movie_item['src'] = item[7]
            movie_item['averating'] = item[9].strip()
            movie_item['playPage'] = item[8]
            movie_item['fileName'] = item[10]
            movie_list.append(movie_item)
    dbutils.close()
    print(movie_list)
    return movie_list


def getMovieByName(dbutils, movieName):
    sql = 'select * from movie where movieName=\'%s\'' % str(movieName)
    result = dbutils.query(sql)
    movie_item = {}
    for item in result:
        movie_item['id'] = item[0]
        movie_item['movieName'] = item[1].strip()
        movie_item['src'] = item[7]
        movie_item['averating'] = item[9]
        movie_item['playPage'] = item[8]
        movie_item['fileName'] = item[10]
    return movie_item


if __name__ == '__main__':
    # host = 'localhost'
    # user = 'python'
    # password = 'python'
    # db = 'movie'
    # port = 3306
    # dbutils = DBUtils(host, user, password, db, port)
    # dbutils.getConn()
    # cursor = dbutils.cursor
    # for i in range(1, 3000):
    #     sql = 'insert into history (uid,mid,score,dt) values (%d,%d,%d,now())' % (
    #         random.randint(1, 200), random.randint(1, 50), random.randint(1, 10))
    #     cursor.execute(sql)
    # dbutils.conn.commit()
    # dbutils.close()
    getRecommend(21)

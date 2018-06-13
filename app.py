# -*- coding: UTF-8 -*-

from flask import Flask, request, render_template
import dao.movieDao as movieDao

app = Flask(__name__, static_folder='', static_url_path='')


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'hello'


@app.route('/index', methods=['get', 'POST'])
def get_item():
    username = 'micheal'
    uid = 21
    movie_list = movieDao.getMovieList()
    return render_template('index.html', movie_list=movie_list, username=username, uid=uid)


@app.route('/toIndex', methods=['get', 'POST'])
def toIndex():
    username = request.args.get('username')
    uid = request.args.get('uid')
    movie_list = movieDao.getMovieList()
    return render_template('index.html', movie_list=movie_list, username=username, uid=uid)


@app.route('/history', methods=['get', 'POST'])
def history():
    username = request.args.get('username')
    uid = request.args.get('uid')
    movie_list = movieDao.getHistoryList(uid)
    return render_template('history.html', movie_list=movie_list, username=username, uid=uid)


@app.route('/info', methods=['get', 'POST'])
def info():
    id = request.args.get('id')
    username = request.args.get('username')
    uid = request.args.get('uid')
    movie = movieDao.getMovieById(int(id))
    return render_template('info.html', movie=movie, username=username, uid=uid)


@app.route('/login', methods=['get', 'POST'])
def login():
    username = request.args.get('Name')
    uid = request.args.get('ID')
    movie_list = movieDao.getMovieList()
    return render_template('index.html', movie_list=movie_list, username=username, uid=uid)


@app.route('/play', methods=['get', 'POST'])
def play():
    username = request.args.get('username')
    uid = request.args.get('uid')
    id = request.args.get('id')
    palyPage = request.args.get('palyPage')
    fileName = request.args.get('fileName')
    return render_template('play.html', id=id, username=username, uid=uid, palyPage=palyPage, fileName=fileName)


@app.route('/recommend', methods=['get', 'POST'])
def recommend():
    username = request.args.get('username')
    uid = request.args.get('uid')
    movieId = request.args.get('movieId')
    score = request.args.get('score')
    movieDao.recordScore(uid, score, movieId)
    movie_list = movieDao.getRecommend(int(uid))
    return render_template('recommend.html', username=username, uid=uid, movie_list=movie_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

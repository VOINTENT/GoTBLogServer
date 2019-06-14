from app import app, db
from app.models import create_tables
from app.models import User, Post, Comment, Subscriber
from flask import jsonify, request
import json

# ===========================================================================

@app.route('/user', methods = ['GET'])
def user_get_all():
    try:
        data_list = []
        for user in db.session.query(User):
            data_list.append(user.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/user/<int:id>', methods = ['GET'])
def user_get_by_id(id):
    try:
        user = db.session.query(User).filter_by(id = id).first()
        if user == None:
            return 'Failed'
    except:
        return 'Failed'
    return json.dumps(user.to_dict(), ensure_ascii = False)

@app.route('/user', methods = ['POST'])
def user_create():
    try:
        data = json.loads(request.get_data())
        user = User(data['login'], data['hash_password'])
        db.session.add(user)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(user.to_dict(), ensure_ascii = False)

@app.route('/user/<int:id>', methods = ['DELETE'])
def user_delete(id):
    try:
        user = db.session.query(User).filter_by(id = id).first()
        db.session.delete(user)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(user.to_dict(), ensure_ascii = False)

@app.route('/user/<int:id>', methods = ['PUT'])
def user_update(id):
    try:
        data = json.loads(request.get_data())
        user = db.session.query(User).filter_by(id = id).first()
        user.login = data['login']
        user.hash_password = data['hash_password']
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(user.to_dict(), ensure_ascii = False)

# ===========================================================================

@app.route('/post', methods = ['GET'])
def post_get_all():
    try:
        data_list = []
        for post in db.session.query(Post):
            data_list.append(post.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/post/<int:id>', methods = ['GET'])
def post_get_by_id(id):
    try:
        post = db.session.query(Post).filter_by(id = id).first()
        if post == None:
            return 'Failed'
    except:
        return 'Failed'
    return json.dumps(post.to_dict(), ensure_ascii = False)

@app.route('/post', methods = ['POST'])
def post_create():
    try:
        data = json.loads(request.get_data())
        post = Post(data['user_id'], data['title'], data['body'], data['publication_date'])
        db.session.add(post)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(post.to_dict(), ensure_ascii = False)

@app.route('/post/<int:id>', methods = ['DELETE'])
def post_delete(id):
    try:
        post = db.session.query(Post).filter_by(id = id).first()
        db.session.delete(post)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(post.to_dict(), ensure_ascii = False)

@app.route('/post/<int:id>', methods = ['PUT'])
def post_update(id):
    try:
        data = json.loads(request.get_data())
        post = db.session.query(Post).filter_by(id = id).first()
        post.user_id = data['user_id']
        post.title = data['title']
        post.body = data['body']
        post.publication_date = data['publication_date']
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(post.to_dict(), ensure_ascii = False)

# ===========================================================================

@app.route('/comment', methods = ['GET'])
def comment_get_all():
    try:
        data_list = []
        for comment in db.session.query(Comment):
            data_list.append(comment.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/comment/<int:id>', methods = ['GET'])
def comment_get_by_id(id):
    try:
        comment = db.session.query(Comment).filter_by(id = id).first()
        if comment == None:
            return 'Failed'
    except:
        return 'Failed'
    return json.dumps(comment.to_dict(), ensure_ascii = False)

@app.route('/comment', methods = ['POST'])
def comment_create():
    try:
        data = json.loads(request.get_data())
        comment = Comment(data['user_id'], data['post_id'], data['body'], data['publication_date'])
        db.session.add(comment)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(comment.to_dict(), ensure_ascii = False)

@app.route('/comment/<int:id>', methods = ['DELETE'])
def comment_delete(id):
    try:
        comment = db.session.query(Comment).filter_by(id = id).first()
        db.session.delete(comment)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(comment.to_dict(), ensure_ascii = False)

@app.route('/comment/<int:id>', methods = ['PUT'])
def comment_update(id):
    try:
        data = json.loads(request.get_data())
        comment = db.session.query(Comment).filter_by(id = id).first()
        comment.user_id = data['user_id']
        comment.post_id = data['post_id']
        comment.body = data['body']
        comment.publication_date = data['publication_date']
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(comment.to_dict(), ensure_ascii = False)

# ===========================================================================

@app.route('/subscriber', methods = ['GET'])
def subscriber_get_all():
    try:
        data_list = []
        for subscriber in db.session.query(Subscriber):
            data_list.append(subscriber.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/subscriber/<int:id>', methods = ['GET'])
def subscriber_get_by_id(id):
    try:
        subscriber = db.session.query(Subscriber).filter_by(id = id).first()
        if subscriber == None:
            return 'Failed'
    except:
        return 'Failed'
    return json.dumps(subscriber.to_dict(), ensure_ascii = False)

@app.route('/subscriber', methods = ['POST'])
def subscriber_create():
    try:
        data = json.loads(request.get_data())
        subscriber = Subscriber(data['user_id'], data['subscriber_id'])
        db.session.add(subscriber)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(subscriber.to_dict(), ensure_ascii = False)

@app.route('/subscriber/<int:id>', methods = ['DELETE'])
def subscriber_delete(id):
    try:
        subscriber = db.session.query(Subscriber).filter_by(id = id).first()
        db.session.delete(subscriber)
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(subscriber.to_dict(), ensure_ascii = False)

@app.route('/subscriber/<int:id>', methods = ['PUT'])
def subscriber_update(id):
    try:
        data = json.loads(request.get_data())
        subscriber = db.session.query(Subscriber).filter_by(id = id).first()
        subscriber.user_id = data['user_id']
        subscriber.subscriber_id = data['subscriber_id']
        db.session.commit()
    except:
        return 'Failed'
    return json.dumps(subscriber.to_dict(), ensure_ascii = False)

# ===========================================================================

@app.route('/post?user_id=<int:id>', methods = ['GET'])
def post_by_user(id):
    try:
        data_list = []
        for post in db.session.query(Post).filter_by(user_id = id):
            data_list.append(post.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/subscriber?user_id=<int:id>', methods = ['GET'])
def subscriber_by_user(id):
    try:
        data_list = []
        for subscriber in db.session.query(Subscriber).filter_by(user_id = id):
            user = db.session.query(User).filter_by(id = subscriber.subscriber_id).first()
            data_list.append(user.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

@app.route('/comment?post_id=<int:id>', methods = ['GET'])
def comment_by_post(id):
    try:
        data_list = []
        for comment in db.session.query(Comment).filter_by(post_id = id):
            data_list.append(comment.to_dict())
    except:
        return 'Failed'
    return json.dumps(data_list, ensure_ascii = False)

from flask import request, jsonify
from . import bp
from app.models import Post, User
from app.blueprint.api.helpers import token_required

# recieve all posts
@bp.get('/posts')
@token_required
def api_posts():
    result = []
    posts = Post.query.all()
    for post in posts:
        result.append ({
                        'id':post.id,
                        'body':post.body,
                        'timestamp':post.timestamp,
                        'author':post.user_id
                        })
    return jsonify(result), 200
 


# recieve Posts from single User
@bp.get('/posts/<username>')
def user_posts(user,username):
    user = User.query.filter_by(user_name=username).first()
    if user:
        return jsonify([{
                'id':post.id,
                'body':post.body,
                'timestamp':post.timestamp,
                'author':post.user_id
                } for post in user.posts]), 200
    return jsonify([{'message':'Invalid Username'}]), 404
    

# ability to Make a request for one specific post(when using primary key  we use (.get)) sending single post
@bp.get('/post/<post_id>')
@token_required
def get_post(user,post_id):
    try:
        post = Post.query.get(post_id)
        return jsonify([{
                'id':post.id,
                'body':post.body,
                'timestamp':post.timestamp,
                'author':post.user_id
                }])
    except:
        return jsonify([{'message':'Invalid Post Id'}]),404


#  ability to let a user sign in 
@bp.post('/post')
@token_required
def make_post(user):
    try:
# recieve their post  data 
        content = request.json
# create a post instance or entry
        post = Post(body = content.get('body'),user_id =user.user_id)
# add foreign key to user id
        post.commit()
# commit our post
        return jsonify([{"message":'Post Created', 'body':post.body}])
    except:
        jsonify([[{'message': 'Invalid form data'}]]), 401
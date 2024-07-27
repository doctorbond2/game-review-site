from app.controllers import review as controller
from flask import request
from app.routes.blueprints import review_bp as review
from endpoints import Review_ENV as path

@review.route(path.post_one_review, methods=['POST'])
def index():
    new_review = request.get_json()
    print(new_review)
    return 'tbd'
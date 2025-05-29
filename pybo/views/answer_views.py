from datetime import datetime

from pybo import db
from flask import Blueprint, render_template, url_for, request, redirect
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

@bp.route('/create/<int:question_id>', methods=['POST'])
def create(question_id):
    # 질문 아이디에 대한 질문 객체를 얻는다
    question = Question.query.get_or_404(question_id)
    #답변글 내용을 얻는다
    content = request.form['content']
    #답변글 객체를 생성한다
    answer = Answer(question=question, content=content, create_date=datetime.now())
    #질문 글에 답변 객체를 추가한다
    question.answer_set.append(answer)
    #데이터 베이스를 저장한다
    db.session.commit()
    #상세 보기 화면으로 이동하다
    return redirect( url_for('question.detail', question_id=question.id))


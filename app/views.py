"""
Handle requests.

Authors:
Majeed Malik
"""

from flask import render_template, request
from app import const
import validators
from app.handleRequest import process_url

def index():
    """Render Startpage."""
    return render_template(
        'index.html',
        title=const.TITLE
    )

def read_article():
    """Handles the sended url"""
    url_sended = request.form['url']
    params = list(request.form.keys())
    params.remove('url')
    if (validators.url(url_sended) and params):
        article_info = process_url(url_sended, params)
        return show_article(article_info)

    else:
        error_message = const.NO_SELECTION
        if params:
            error_message = const.INVALID_URL
        return render_template(
            'index.html',
            title=const.TITLE,
            invalid_url = True,
            error_message = error_message
        )

def show_article(article_info):
    return render_template(
        'article.html',
        title=const.TITLE,
        show_article = True,
        article_info = article_info
    )
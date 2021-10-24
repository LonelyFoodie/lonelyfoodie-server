import json
import uuid

from pytest import fixture, yield_fixture
from app import create_app
from flask import url_for


def url(app, name, data=''):
    return url_for(app, name, data)


@fixture(scope="session", autouse=True)
def f_db():
    pass


@fixture
def f_wsgi(f_init_db):
    app = create_app()
    app.config.update(PROPAGATE_EXCEPTIONS=True)
    return app


class Client:
    def __init__(self, app, client):
        self.wsgi = app
        self.client = client

    def get(self, name, data={}):
        res = self.client.get(
            url(self.app, name, **data),
            content_type='application/json'
        )
        return self.response(res)

    def post(self, name, data={}):
        res = self.client.post(
            url(self.wsgi, name),
            data=json.dumps(data),
            content_type='application/json'
        )
        return self.response(res)

    def post_upload(self, name, data={}):
        res = self.client.post(
            url(self.wsgi, name),
            data=data,
            content_type='multipart/form-data'
        )
        return self.response(res)

    def put(self, name, data={}):
        res = self.client.put(
            url(self.wsgi, name),
            data=json.dumps(data),
            content_type='application/json'
        )
        return self.response(res)

    def delete(self, name, data={}):
        res = self.client.delete(
            url(self.wsgi, name, **data),
            content_type='application/json'
        )
        return self.response(res)

    def response(self, res):
        if res.content_type == 'application/json':
            return res.status_code, json.loads(res.data.decode('utf-8'))
        if res.status_code in [301, 302]:
            return res.status_code, dict(res.headers)['Location']
        return res.status_code, None


# client 강제 생성
def _make_client(app, is_admin=False):
    client = app.test_client()  # 실제 서버 생성 안하고 가상 객체 만듬

    return Client(app, client)


@fixture
def f_user(f_app):
    client = _make_client(f_app)
    return client


@fixture
def f_admin(f_app):
    return _make_client(f_app, True)
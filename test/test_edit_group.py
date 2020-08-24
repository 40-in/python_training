# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="1flsdjfl", header="2dhk", footer="3vdjd"))
    app.session.logout()
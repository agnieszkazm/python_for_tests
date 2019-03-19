# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("test_name", "test_header", "test_footer"))
    app.session.logout()


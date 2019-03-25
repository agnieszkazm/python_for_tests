# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group("test_name", "test_header", "test_footer"))


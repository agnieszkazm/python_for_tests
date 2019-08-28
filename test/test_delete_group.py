# -*- coding: utf-8 -*-
from model.group import Group

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first()
    new_groups = app.group.get_group_list()
    assert len(new_groups)+1 == len(old_groups)
    assert old_groups[1:] == new_groups


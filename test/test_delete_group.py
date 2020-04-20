# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group("test"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    app.group.delete_random_group(index)
    new_groups = app.group.get_group_list()
    assert len(new_groups)+1 == len(old_groups)
    old_groups[index: index+1] = []
    assert old_groups == new_groups


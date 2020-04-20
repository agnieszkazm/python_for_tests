from model.group import Group
import random

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="test_name_modify")
    group.id = old_groups[index].id
    app.group.modify_random_group(index, group)
    new_groups = app.group.get_group_list()
    assert len(new_groups) == len(old_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test", header="header"))
#     app.group.modify_first(Group(header="test_header"))

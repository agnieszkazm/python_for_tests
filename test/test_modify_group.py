from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first(Group(name="test_name_modify"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header"))
    app.group.modify_first(Group(header="test_header"))

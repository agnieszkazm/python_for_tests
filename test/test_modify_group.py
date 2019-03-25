from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name = "test_name_modify"))

def test_modify_group_header(app):
    app.group.modify_first(Group(header="test_header"))

from model.group import Group


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.modify(Group("test_name_modify", "test_header", "test_footer"))
    app.session.logout()

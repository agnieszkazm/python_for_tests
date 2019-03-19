# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Testname", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test", "www.example.com"))
    app.session.logout()





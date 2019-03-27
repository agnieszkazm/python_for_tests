# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    app.contact.modify(Contact("Testname_modify", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test", "www.example.com"))

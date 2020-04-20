# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test tester"))
    old_contact = app.contact.get_contacts_list()
    index = random.randrange(len(old_contact))
    contact = Contact("Testname_modify", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test", "www.example.com")
    contact.id = old_contact[index].id
    app.contact.modify_random(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(new_contacts) == len(old_contact)
    old_contact[index] = contact
    assert old_contact == new_contacts


# def test_modify_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="test"))
#     app.contact.modify(
#         Contact("Testname_modify", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test",
#                 "www.example.com"))

# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.delete_first()
    new_contacts = app.contact.get_contacts_list()
    print(new_contacts)
    print(old_contacts)
    assert len(new_contacts) + 1 == len(old_contacts)
    assert old_contacts[1:] == new_contacts

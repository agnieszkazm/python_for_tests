# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="test"))
    old_contacts = app.contact.get_contacts_list()
    index = random.randrange(len(old_contacts))
    app.contact.delete_random(index)
    new_contacts = app.contact.get_contacts_list()
    print(new_contacts)
    print(old_contacts)
    assert len(new_contacts) + 1 == len(old_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
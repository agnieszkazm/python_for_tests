# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Testname", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test", "www.example.com"))
    app.session.logout()





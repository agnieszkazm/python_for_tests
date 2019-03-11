# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Testname", "Testname2", "Testlastname", "test", "555", "666", "777", "888", "test", "www.example.com"))
    app.logout()





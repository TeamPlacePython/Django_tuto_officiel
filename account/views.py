from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash


class IndexView:
    ...


class LoginView:
    ...


def add():
    # ajouter:user.has_perm('foo.add_bar')
    pass


def change():
    # changement:user.has_perm('foo.change_bar')
    pass


def delete():
    # supprimer:user.has_perm('foo.delete_bar')
    pass


def display():
    # voir:user.has_perm('foo.view_bar')
    pass

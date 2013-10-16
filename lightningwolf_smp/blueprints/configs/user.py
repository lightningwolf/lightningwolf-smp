#!/usr/bin/env python
# coding=utf8
from flask_lwadmin.config import ConfigParser
from lightningwolf_smp.models.user import get_user_filters
from lightningwolf_smp.forms.user import (
    FormUsernameFilter,
    FormUserBatchActions
)

filter_data = get_user_filters()

configuration = {
    'list': {
        'title': 'Users List',
        'display': [
            {'key': 'id', 'label': 'Id'},
            {'key': 'username', 'label': 'Username', 'icon': 'icon-user'},
            {'key': 'email', 'label': 'E-mail', 'icon': 'icon-envelope'}
        ],
        'actions': [
            {
                'key': 'new',
                'label': 'New',
                'url': 'user.user_create',
                'type': ConfigParser.URL_INTERNAL,
                'class': 'btn btn-primary'
            }
        ],
        'object_actions': [
            {
                'key': 'edit',
                'label': 'Edit',
                'icon': 'icon-edit',
                'call': 'set_edit_button'
            },
            {
                'key': 'delete',
                'label': 'Delete',
                'icon': 'icon-trash icon-white',
                'confirm': True,
                'confirm_message': 'Are you sure?',
                'class': 'btn btn-small btn-danger',
                'call': 'set_del_button'
            }
        ],
        'batch': {
            'url': 'user.user_batch',
            'type': ConfigParser.URL_INTERNAL,
            'form': FormUserBatchActions()
        },
        'filter': {
            'url': 'user.user_filter',
            'type': ConfigParser.URL_INTERNAL,
            'form': FormUsernameFilter(**filter_data)
        }
    }
}

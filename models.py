"""
This file defines the database models
"""

import datetime
from .common import db, Field, auth, T
from pydal.validators import *


def get_user_email():
    return auth.current_user.get('email') if auth.current_user else None

def get_time():
    return datetime.datetime.utcnow()


### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later

# py4web reads table declarations when it starts up
# table declarations read: default values are set
# get_user_email vs get_user_email(): user may not be logged in at start of py4web
# every time a new value is inserted, py4web calls get_user_email() and inserts it into the field
db.define_table(
    'product',
    Field('product_name', requires=IS_NOT_EMPTY),
    Field('product_quantity', 'integer', default=0, requires=IS_INT_IN_RANGE(0, 1e6)),
    Field('product_price', 'float', default=0., requires=IS_FLOAT_IN_RANGE(0, 1e6)),
    Field('mail_order', 'boolean', default=True),
    Field('created_by', default=get_user_email),            # diagnostic
    Field('creation_date', 'datetime', default=get_time),   # diagnostic
)


# can also declare Validators outside field declarations like so:
# db.product.name.requires = IS_NOT_EMPTY()

# Visibility field: (every table has an ID field automatically added)
# db.product.id.readable = False
# db.product.created_by.readable = False
# db.product.creation_date.readable = False

# T translation: translation to whatever site (wherever)
# db.product.product_quantity.label = T('Quantity')
# db.product.product_price.label = T('Price')

db.commit()

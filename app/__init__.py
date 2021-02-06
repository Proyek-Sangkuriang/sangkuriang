# -*- encoding: utf-8 -*-
"""
Copyright (c) 2021 - present Sangkuriang Project
"""

import yaml

with open("../config.yaml","r") as config_file:
	config = yaml.safe_load(config_file)

"""
Copyright (c) 2019 - present AppSeed.us
"""

# import Flask 
from flask import Flask

# Inject Flask magic
app = Flask(__name__)

# App Config - the minimal footprint
app.config['TESTING'   ] = config['TESTING']
app.config['SECRET_KEY'] = config['SECRET']

# Import routing to render the pages
from app import views



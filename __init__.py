###########################################################################################
# raceresultswebapp - package
#
#       Date            Author          Reason
#       ----            ------          ------
#       03/28/14        Lou King        Create
#
#   Copyright 2014 Lou King
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
###########################################################################################

# standard
import os

# pypi
import flask

# homegrown
from app import app

# configure app
DEBUG = False
if DEBUG:
    SECRET_KEY = 'flask development key'
else:
    SECRET_KEY = os.urandom(24)
app.config.from_object(__name__)

# tell jinja to remove linebreaks
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# import all views
import hello


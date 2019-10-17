import os

basedir=os.path.abspath(os.path.dirname(__file__)) # BASE_DIR is pointing to the parent directory of PROJECT_ROOT.
                                                    # simply removes the last segment of a path.
                                                    # storing the full path to the directory the module lives in in PROJECT_ROOT.

class Config(object):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \ 'sqlite:///'+os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATION=False
    

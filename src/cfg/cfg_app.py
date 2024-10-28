import os

import toml

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Connect the path with your '.env' file name
cfg_file= os.path.join(BASEDIR, 'config.toml')
config=None
with open(cfg_file, 'r') as f:   #C:\Users\Public\py_dev\fastapi\test_SQLModel\src\config.toml
    config = toml.load(f)

# Access values from the config
print(config['data']['data_folder'])
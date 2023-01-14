# Build and setup application

```bash
apt get install python3.11
apt get install pip
pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
venv/bin/pip3 install -r requirements.txt
flask db init
flask db upgrade
```

# View dependencies
````bash
venv/bin/pip3 freeze
````

# Build and setup application
```bash
sudo su
apt get install python3.11
apt get install pip
exit
pip install virtualenv
virtualenv -p python3 venv
. venv/bin/activate
venv/bin/pip3 install -r requirements.txt
```

# Dependencies
````bash
venv/bin/pip3 freeze
````
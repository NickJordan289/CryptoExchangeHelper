### Running the server (Pipenv)
```
// don't forget to place the .env file in the folder
pipenv install -r requirements.txt
pipenv run python main.py
```

### Configurations
In the __init\__.py be sure to change the mail_config to your own server  

### .env file requirements
Token: API token for exchange.coinjar.com
Email_pass: Password to the email that will be sending out alerts
```
TOKEN=...
EMAIL_PASS=...
```																							

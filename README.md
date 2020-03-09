# testFlask

This is a test webApp that calculates vendor rates based on user input using fake data

Get the URL from the Clone / Download link in this project

In Pycharm's top navigation bar, click VCS -> Checkout From Version Control -> Git

Paste the URL into the prompt and clone the repo

After importing the project, make sure you have all requirements installed:
- If you need to configure the project's python interpreter again, just add a new Virtualenv Environment to the project
  - Preferences -> Project Interpreter -> Settings Wheel -> Add -> OK
- If you expand the 'Terminal' tab on the bottom of the pycharm editor, you should see (venv)
  - If you don't, make sure you are in the testFlask directory and run -> source ./venv/bin/activate
  - In the virtual environment, run -> pip install -r stable-req.txt

Run WebApp.py

Open a browser window and navigate to:

http://localhost:5000/

Currently:
Only the following Vendors are configured and will return results:
- LB+MOR
- MOR-Only

Only the following languages are configured and will return results:
- ARAR
- ZHCN

Only the following outputs are dynamic:
- newWordCost
- reviewCost
- lowFuzziesCost

The webapp will NOT validate integer values - This functionality needs to be added

The rest are hard-coded to calculate based off of [rate] * 1 - Check the TODO in WebApp.py Line 38

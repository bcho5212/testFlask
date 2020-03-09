# testFlask

This is a test webApp that calculates vendor rates based on user input using fake data

After importing the project, make sure you have all requirements installed:
- In the virtual environment, run -> pip install -r stable-req.txt

Run WebApp.py

Open a browser window and navigate to:

http://localhost:5000/

Currently - Only the following Vendors are configured and will return results:
- LB+MOR
- MOR-Only

Only the following languages are configured and will return results:
- ARAR
- ZHCN

Only the following outputs are dynamic:
- newWordCost
- reviewCost

The rest are hard-coded to calculate based off of [rate] * 1 - Check the TODO in WebApp.py Line 38

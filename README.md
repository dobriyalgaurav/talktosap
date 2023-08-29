# talktosap
Communicate with SAP Gigya Console to retrieve various elements.

This repo has 2 sub repos - 
- websdk -> To load screensets via web sdk
- serversidesdk/python -> To fetch screensets via server side sdk.

# Prerequisites
- API & Secret key from Gigya Console.

# Web SDK
Loads the widgets via client side web sdk.
- navigate to the directory -> websdk
- run the command in terminal (only first time) -> npm install
- run the project via command -> npm run dev

# Server Side SDK
Fetch the widgets via server side sdk.
- navigate to the directory -> serversidesdk/python
- run the command -> python3 getScreenSets.py

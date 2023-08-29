from GSSDK import *

# Define the API and Secret key (the keys can be obtained from your site setup page in the Gigya console).
apiKey = "PUT_API_KEY_HERE"
secretKey = "PUT_SECRET_KEY_HERE"

# Step 1 - Defining the request and adding parameters
method = "accounts.getScreenSets"
params = {
    "screenSetIDs": "PoC-RegistrationLogin",
    "include": "screenSetID, html"
}
request = GSRequest(apiKey, secretKey, method, params)

# Step 2 - Sending the request
response = request.send()

# Step 3 - handling the request's response.
if (response.getErrorCode() == 0):
    # SUCCESS! response status = OK
    print("Success in accounts.getScreenSets operation.")
    print("Response: " + str(response.getResponseText()))
else:
    # Error
    print("Got error on accounts.getScreenSets: " +
          response.getErrorMessage())
    # You may also log the response: response.getLog()

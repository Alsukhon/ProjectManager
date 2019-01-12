from upwork import client

#Instantiating a client without an auth token
client = upwork.Client(public_key, secret_key)

print "Get to this URL (authorize the app if necessary):"
print client.auth.get_authorize_url()
print "After that you should be redirected back to your app URL with " + \
      "additional ?oauth_verifier= parameter"

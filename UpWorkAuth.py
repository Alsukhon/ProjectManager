from upwork import Client

def Connect(public_key, secret_key):
    #Instantiating a client without an auth token
    client = upwork.Client(public_key, secret_key)
    return client.auth.get_authorize_url()
    

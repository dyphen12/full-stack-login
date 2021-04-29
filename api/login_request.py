import database as datb

#### REQUESTS #####

def login(user,passw):

    auth, ssid = datb.user_validation(user,passw)

    return auth, ssid

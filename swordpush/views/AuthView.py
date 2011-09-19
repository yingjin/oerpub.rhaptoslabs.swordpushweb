import swordcnx
from languages import languages

def AuthView(request):
    """
    Handle authentication (login) requests.
    """
    # TODO: check credentials against Connexions and ask for login
    # again if failed.

    swordServer = request.params['server']
    if swordServer.find("://") == -1:
        swordServer = "http://" + swordServer
    if swordServer[-1] == "/":
        swordServer = swordServer[:-1]

    # Encode authentication information
    import base64
    username = request.params['username']
    password = request.params['password']
    digest = base64.b64encode(username + ':' + password)

    # Authenticate to Connexions
    conn = swordcnx.Connection(swordServer + "/sword",
                               user_name=username,
                               user_pass=password,
                               download_service_document=True)

    # Get available collections from SWORD service document
    swordCollections = swordcnx.parse_service_document(conn.sd)

    return {
        'swordServer': swordServer,
        'credentials': digest,
        'swordCollections': swordCollections,
        'url': '',
        'title': '',
        'keepTitle': False,
        'summary': '',
        'keepSummary': False,
        'keywords': '',
        'keepKeywords': True,
        'languages': languages,
        'language': 'en',
    }

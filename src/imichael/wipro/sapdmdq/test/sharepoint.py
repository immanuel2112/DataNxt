import requests
import shareplum

config = dict()
config['sp_user'] = 'partner.immanuel.michael@philips.com'
config['sp_password'] = 'Mar@2020'
config['sp_base_path'] = 'https://share.philips.com'
config['sp_site_name'] = 'STS20121025134501'
config['sp_doc_library'] = '07. DM Tools'

# get data from configuration
username = config['sp_user']
password = config['sp_password']
site_name = config['sp_site_name']
base_path = config['sp_base_path']
doc_library = config['sp_doc_library']

file_name = "Pic1.JPG"

# Obtain auth cookie
authcookie = shareplum.Office365(base_path, username=username, password=password).GetCookies()
session = requests.Session()
session.cookies = authcookie
session.headers.update({'user-agent': 'python_bite/v1'})
session.headers.update({'accept': 'application/json;odata=verbose'})

# dirty workaround.... I'm getting the X-RequestDigest from the first failed call
session.headers.update({'X-RequestDigest': 'FormDigestValue'})
response = session.post( url=base_path + "/sites/" + site_name + "/_api/web/GetFolderByServerRelativeUrl('" + doc_library + "')/Files/add(url='a.txt',overwrite=true)",
                         data="")
session.headers.update({'X-RequestDigest': response.headers['X-RequestDigest']})

# perform the actual upload
with open( file_name, 'rb') as file_input:
    try:
        response = session.post(
            url=base_path + "/sites/" + site_name + "/_api/web/GetFolderByServerRelativeUrl('" + doc_library + "')/Files/add(url='"
                + file_name + "',overwrite=true)",
            data=file_input)
    except Exception as err:
        print("Some error occurred: " + str(err))
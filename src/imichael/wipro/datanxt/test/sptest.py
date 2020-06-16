from sharepoint import SharePointSite, basic_auth_opener

server_url = "https://share.philips.com/"
site_url = server_url + "sites/STS20121025134501"

opener = basic_auth_opener(server_url, "code1/320027644", "Mar@2020")

site = SharePointSite(site_url, opener)

print(site)
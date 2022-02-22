# Récupération de l'URL

import urllib.request
sock = urllib.request.urlopen("https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr")  # urllib.urlopen("https://www.iso.org/obp/ui/#iso:std:iso:19101:-2:ed-1:v1:fr")
htmlSource=sock.read()
sock.close()
print(htmlSource)
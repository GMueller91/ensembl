import requests

# url = "http://rest.ensembl.org/overlap/id/ENSG00000157764.json?feature=variation"

url = "http://rest.ensembl.org/sequence/id/ENSP00000439902.json"

r=requests.get(url)

if not r.status_code==200:
    raise Exception("Bad response")
    
print(r.json())

# print(len(r.json()))
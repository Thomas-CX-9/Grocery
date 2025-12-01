import requests
url = 'https://img.genially.com/68b97418ded987001575b0ad/04eee00e-c382-4c0e-bdb1-5c4b6ea2c6a6.jpeg'
hearders = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
filetype = input('filetype:')
with open(fileName := input('filename:') + filetype,'wb') as f:
    f.write(requests.get(url,headers=hearders).content)
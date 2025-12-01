import requests
url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCuBRP9YJZ231K_UTwEps6QcResT7lrdTv_A&s'
hearders = {'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}
filetype = input('filetype:')
with open(fileName := input('filename:') + '.' + filetype,'wb') as f:
    print(requests.get(url,headers=hearders))
    f.write(requests.get(url,headers=hearders).content)
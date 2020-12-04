import github3
def fun():
    #gh = github3.login(username='gowri-gs',token='144882279b1e8e85ab11cb095fba3badfadf0470')
    gh = github3.login(username='gowri-gs',token='38eff242e2ec14fe92f371974c1a167e04d73862')
    repository = gh.repository('Zephyrs3', 'Sentiment_analysis')
    #file_info = 'optweet.csv'
    files_to_upload = ["optweet.csv","docemo.csv","catop.csv"]
    message = "Updated"
    for file_info in files_to_upload:
        with open(file_info, 'rb') as fd:
            contents = fd.read()
        contents_object = repository.file_contents(file_info)
        contents_object.update(message, contents)
import requests

for i in range(1, 81):
    print(i)
    x = requests.get('https://rc.majlis.ir/fa/legal_draft/search?lu_period_no=35&from='+str(i))

    # get posts list
    posts = x.text.split('href="https://rc.majlis.ir/fa/legal_draft/show/')[1:]

    for post in posts :
        number = post.split('"')[0]
        print(number)

        postHtml = requests.get('https://rc.majlis.ir/fa/legal_draft/show/'+number)

        #extract title
        title = postHtml.text.split('<title>')[1].split('</title>')[0]
        fileLink = postHtml.text.split('<a href="https://rc.majlis.ir/fa/legal_draft/state_popup/')[1].split('"')[0].replace('amp;','')

        #download file
        print('https://rc.majlis.ir/fa/legal_draft/state_popup/'+fileLink)
        response = requests.get('https://rc.majlis.ir/fa/legal_draft/state_popup/'+fileLink, allow_redirects=True)

        #store file
        open(title+".pdf", "wb").write(response.content)

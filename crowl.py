import requests



for i in range(1, 81):
    print(i)
    x = requests.get('https://rc.majlis.ir/fa/legal_draft/search?lu_period_no=35&from='+str(i))
    posts = x.text.split('href="https://rc.majlis.ir/fa/legal_draft/show/')[1:]
    for post in posts :
        print(post.split('"')[0])
        postHtml = requests.get('https://rc.majlis.ir/fa/legal_draft/show/'+post.split('"')[0])
        title = postHtml.text.split('<title>')[1].split('</title>')[0]
        link = postHtml.text.split('<a href="https://rc.majlis.ir/fa/legal_draft/state_popup/')[1].split('"')[0]
        print('https://rc.majlis.ir/fa/legal_draft/state_popup/'+link.replace('amp;',''))
        response = requests.get('https://rc.majlis.ir/fa/legal_draft/state_popup/'+link.replace('amp;',''))
        open(title+".pdf", "wb").write(response.content)

import urllib.request

number_of_webpages = input ("Number of pages to download: ")
number_of_webpages = int(number_of_webpages)

i=0
while i < number_of_webpages:
    url = str(input('URL: '))
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    webContent = response.read()
    f = open(str(i) + '.html','w')
    f.write(str(webContent))
    f.close
    print('Done!')
    i = i + 1

from libs.crawler import crawl
url = "https://www.instagram.com/explore/tags/%EC%84%9C%EC%9A%B8/?hl=ko"

pageString = crawl(url)
print(pageString)

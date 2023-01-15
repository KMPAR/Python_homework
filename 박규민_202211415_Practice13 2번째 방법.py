import bs4
import urllib.request as req

def crawler():
    html_text = ''
    with req.urlopen(url) as response:
        html_text = response.read().decode('utf-8')

    soup = bs4.BeautifulSoup(html_text, 'html5lib')
    soup.prettify()

    nodes = soup.find_all('td')

    papers = []
    papers1 = []

    for node in nodes:
        papers.append(node.text)


    for paper in papers:   
        paper = paper.strip()
        papers1.append(paper)

    n = 5
    result = [papers1[i * n:(i + 1) * n] for i in range((len(papers1) + n - 1) // n )] 


    return result

url = 'http://www.konkuk.ac.kr/jsp/Coll/coll_01_04_05_01_tab01.jsp'
print(crawler())
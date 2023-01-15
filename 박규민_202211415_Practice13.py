# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

import bs4
import urllib.request as req

def crawler(url):
    html_text = ''
    with req.urlopen(url) as response:
        html_text = response.read().decode('utf-8')

    soup = bs4.BeautifulSoup(html_text, 'html5lib')
    soup.prettify()

    nodes = soup.find_all('td')

    papers = []

    for node in nodes:
        papers.append(node.text)

    search1 = '\n\t\t\t\t\t  \n                      '
    search2 = '\n\t\t\t\t\t\t\n\t\t\t\t\t\t\t'

    papers = [paper.strip(search1) for paper in papers]
    papers = [paper.strip(search2) for paper in papers]
    
    def list_chunk(lst, n):
        return [lst[i:i+n] for i in range(0, len(lst), n)]

    papers = list_chunk(papers, 5)
    
    return papers

a = 'http://www.konkuk.ac.kr/jsp/Coll/coll_01_04_05_01_tab01.jsp'
print(crawler(a))

# 나는 본 실습과제물 작성에 있어 다른 수강생의 코드를 참고하지 않고 스스로 모든 코드를 작성하였습니다.
# 나는 본 실습과제물 결과를 수강생 누구에게도 배포하지 않았습니다.
# 나는 모든 제출 주의사항(제출 양식)을 준수하였습니다.
# 그렇지 않을 경우 어떠한 페널티도 감수하겠습니다.
# 산업공학과_202211415_박규민

from selenium import webdriver
import time

def get_fame(url):
    driver = webdriver.PhantomJS('/Users/bubgyu_0209/opt/phantomjs-2.1.1-macosx/bin/phantomjs')
    driver.get(url)

    papers1 = []
    nodes = driver.find_elements_by_tag_name('small')
    for node in nodes:
        print(node.text)
        papers1.append(node.text)
    del papers1[-1]

    dic1 = []
    dic2 = []
    dic3 = []
    dic4 = []
    dic5 = []
    dic6 = []
    dic1.append(papers1[0:2])
    dic2.append(papers1[2:8])
    dic3.append(papers1[8:12])
    dic4.append(papers1[12:16])
    dic5.append(papers1[16:19])
    dic6.append(papers1[19:20])

    papers3 = []
    papers3.append(dic1)
    papers3.append(dic2)
    papers3.append(dic3)
    papers3.append(dic4)
    papers3.append(dic5)
    papers3.append(dic6)
    # print(papers3)

    papers2 = []
    nodes = driver.find_elements_by_tag_name('p')
    for node in nodes:
        # print(node.text)
        papers2.append(node.text)
    del papers2[6:]
    # print(papers2)

    dictionary = dict(zip(papers2, papers3))

    time.sleep(3)
    driver.quit()

    return dictionary

print(get_fame('https://sites.google.com/view/kkbizintelligence/lecture'))
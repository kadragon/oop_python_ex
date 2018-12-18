import requests
import json
import urllib


def getLastCommitDate(owners, repos):
    r = requests.get(
        "https://api.github.com/repos/%s/%s/commits" % (owners, repos))
    r.elapsed.total_seconds()
    responce = r.json()

    return responce[0]['commit']['committer']['date']


def getReadme(owners, repos):
    r = requests.get(
        "https://api.github.com/repos/%s/%s/contents/README.md" % (owners, repos))
    r.elapsed.total_seconds()
    responce = r.json()

    downloadUrl = responce['download_url']

    data = requests.get(downloadUrl)
    data.elapsed.total_seconds()

    person = data.text.split('\n')[1]

    person = person.replace('구성원: ', '')
    person = person.split('|')

    # 구성원 반 이름 순으로 정렬
    personTrim = []
    for i in person:
        personTrim.append(i.strip())

    if len(person) == 2:
        person.append('9-9 홍길동')

    # 재 조합
    personTrim.sort()
    person = ' | '.join(personTrim)

    return person


def getForksList():
    getList = []

    r = requests.get(
        'https://api.github.com/repos/kadragon/oop_project_ex/forks')
    r.elapsed.total_seconds()
    responce = r.json()

    for i in responce:
        if i['name'] == 'oop_project_ex':
            continue

        getList.append((i['owner']['login'], i['name']))

    return getList


projectList = getForksList()

for i in projectList:
    a, b = i
    print("%s | %s" % (getReadme(a, b), getLastCommitDate(a, b)))

import random
import time

ban = []

ban.append("박해준 김단은 박혜준 김연우 김이룸 정영근 조현준 권정준 방준형 지명금 유현아 이준홍".split())
ban.append("배민열 박정완 박지원 유지호 황창환 윤준하 이은석 이준모".split())
ban.append("연제호 윤성민 정려빈 최호영 강태원 최정담 황서영 이유환 경다녕 배상우 오은제 장영웅".split())

ban_input = int(input("조 편성을 하고 싶은 반을 입력하세요(1~3): "))-1

random.shuffle(ban[ban_input])

group = 1
cnt = 0
print("\n[발표합니다 | 다시~ 는 없어요!]\n")
for i in ban[ban_input]:
    time.sleep(2)
    print("GROUP %d | %s" % (group, i))
    cnt += 1
    if cnt == 3:
        print("[GROUP %d 선정 완료]\n" % group)
        cnt = 0
        group += 1

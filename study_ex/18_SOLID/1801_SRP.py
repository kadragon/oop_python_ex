class StudentScoreAndCourseManager:
    def __init__(self):
        scores = {}
        courses = {}

    # 성적 확인 기능
    def get_score(self, student_name, course):
        pass

    # 수강 결과 기능
    def get_courses(self, student_name):
        pass


# 각각의 책임을 한개로 줄여서, 각각 수정이 다른 것에 영향을 미치지 않도록 함
class ScoreManager(object):
    def __init__(self):
        scores = {}

    def get_score(self, student_name, course):
        pass


class CourseManager(object):
    def __init__(self):
        courses = {}

    def get_courses(self, student_name):
        pass

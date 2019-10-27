class BubbleSort:
    # def bubble_sort(self):
    def sort(self):
        # sorting algorithm
        pass


# 새로운 정렬 방식이 들어온다면?..
class QuickSort:
    def sort(self):
        # sorting algorithm
        pass


class SortManager:
    def __init__(self, sort_method):
        self.sort_method = sort_method

    def begin_sort(self):
        # self.sort_method.bubble_sort()
        self.sort_method.sort()


s = SortManager(QuickSort())
s.begin_sort()

class BubbleSort:
    # def bubble_sort(self):
    def sort(self):
        # sorting algorithm
        pass


class SortManager:
    def __init__(self):
        self.sort_method = BubbleSort()

    def begin_sort(self):
        # self.sort_method.bubble_sort()
        self.sort_method.sort()


s = SortManager()
s.begin_sort()

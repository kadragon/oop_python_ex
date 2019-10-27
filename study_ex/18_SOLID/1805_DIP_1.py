class BubbleSort:
    def bubble_sort(self):
        # sorting algorithm
        pass


class SortManager:
    def __init__(self):
        self.sort_method = BubbleSort()

    def begin_sort(self):
        self.sort_method.bubble_sort()


s = SortManager()
s.begin_sort()

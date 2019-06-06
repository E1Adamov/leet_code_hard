class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
        self.top = False
        self.left = False
        self.topLeft_bottomRight = False
        self.topRight_bottomLeft = False

    def __eq__(self, other):
        return (int(self.x), int(self.y)) == other

    def __str__(self):
        attr = [i for i in dir(self)if not i.startswith('__') and not callable(i) and getattr(self, i) is True]
        if not attr:
            attr = ''
        return f'({self.x}, {self.y}) {attr}'


class Solution:
    def __init__(self):
        self.board = None

    def _get_longer_line(self, attribute, x_incr, y_incr):
        longest = 1
        for point in self.board:
            if getattr(point, attribute) is True:
                longest = self._get_length(point, x_incr, y_incr)
        return longest

    def _get_length(self, point, x_incr, y_incr, length=1):
        target_point = Point(point.x + x_incr, point.y + y_incr)
        if target_point in self.board:
            length += 1
            return self._get_length(target_point, x_incr, y_incr, length)

        return length

    def get_the_longest_line(self):
        longest_vertical = self._get_longer_line('top', 0, -1)
        longest_horizontal = self._get_longer_line('left', 1, 0)
        longest_left_right = self._get_longer_line('topLeft_bottomRight', 1, -1)
        longest_right_left = self._get_longer_line('topRight_bottomLeft', -1, -1)
        return max(longest_vertical, longest_horizontal, longest_left_right, longest_right_left)

    @staticmethod
    def make_board(points):
        # remove duplicates
        points_ = [list(tupl) for tupl in {tuple(item) for item in points}]
        return [Point(point[0], point[1]) for point in points_]

    def _is_end(self, point, incr_x, incr_y):
        empty_cell = Point(point.x - incr_x, point.y - incr_y)
        for pnt in self.board:
            if pnt == empty_cell:
                return False

        return True

    def _has_continuation(self, point, incr_x, incr_y):
        target_cell = Point(point.x + incr_x, point.y + incr_y)
        for pnt in self.board:
            if pnt != point and pnt == target_cell:
                return True

    def _verify_points(self, incr_x, incr_y, attribute):
        for point in self.board:
            if self._is_end(point, incr_x, incr_y):
                # print(f'point {point} is an end')
                if self._has_continuation(point, incr_x, incr_y):
                    setattr(point, attribute, True)
                    # print(f'point {point} is end and has continuation')

    def process_points(self):
        self._verify_points(0, -1, 'top')
        self._verify_points(1, 0, 'left')
        self._verify_points(1, -1, 'topLeft_bottomRight')
        self._verify_points(-1, -1, 'topRight_bottomLeft')

    def maxPoints(self, points):
        # make a list of object-points
        self.board = self.make_board(points)

        # analyze the points and set their attributes
        self.process_points()

        # calculate the lines and return the longest one
        return self.get_the_longest_line()

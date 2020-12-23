import unittest
from btc_close_2017 import draw_line


class TestDrawLine(unittest.TestCase):

    def setUp(self):
        self.x_datas = [1, 1, 2, 2, 3, 3]
        self.y_datas = [10, 20, 20, 30, 30, 40]
        self.title = "测试_吃葡萄不吐葡萄皮"
        self.y_legend = "just for test"

    def test_draw_line_for_single_data(self):
        line_chart = draw_line([self.x_datas[0]], self.y_datas[:1], self.title, self.y_legend)
        self.assertTrue(line_chart.x_labels == [1])

    def test_draw_line_for_multiple_data(self):
        line_chart = draw_line(self.x_datas, self.y_datas, self.title, self.y_legend)
        self.assertTrue(line_chart.x_labels == [1, 2, 3])


unittest.main()
# 注意运行要点击上方的Run来选择正确的运行文件


import pytest


class Test_demo1 ():
    def test_01(self):
        print('pytest测试')


if __name__ == '__main__':
    pytest.main('-q', 'test_01.py')
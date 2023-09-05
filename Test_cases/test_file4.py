import pytest


class Test_04:
    # @pytest.mark.group1
    # @pytest.mark.skip
    def test_07(self):
        x = 7
        y = 5
        mul = x * y

        if mul == 35:
            assert True
        else:
            assert False
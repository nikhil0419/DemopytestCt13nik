import pytest


class Test_02:
    # @pytest.mark.Sanity
    # @pytest.mark.skip
    def test_sum_04(self):
        a = 3
        b = 4

        sum = a + b
        print(sum)

        if sum == 7:
            assert True
        else:
            assert False


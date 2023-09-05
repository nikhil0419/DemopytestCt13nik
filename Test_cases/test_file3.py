import pytest


class Test_03:
    # def text_sum_05(self):
    #     a = 3
    #     b = 4
    #
    #     sum = a + b
    #     print(sum)
    #
    #     if sum == 7:
    #         assert True
    #     else:
    #         assert False

    # This will not run because [def text_sum_05(self):] is written. It should be[def test_sum_05(self):].
    # ------------------------------------------------
    # @pytest.mark.skip
    def test_sum_06(self):
        a = 3
        b = 4

        sum = a + b
        print(sum)

        if sum == 7:
            assert True
        else:
            assert False  # Now this will Run

    # ------------------------------------------------------
    def sum_06(self):  # This will not run bcoz fun name is not start with [test_].
        a = 3
        b = 4

        sum = a + b
        print(sum)

        if sum == 7:
            assert True
        else:
            assert False  # Now this will Run

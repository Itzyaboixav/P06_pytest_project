import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add_normal_1(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_add_normal_2(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 4
        assert result == expected
    
    def test_add_negative(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = -3
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 5
        b = 3
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 2
        assert result == expected
    
    def test_multiply(self):
        # arrange
        a = 5
        b = 3
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 15
        assert result == expected


    def test_divide_normal(self):
        # arrange
        a = 15
        b = 3
        cal = Calculator()
     

        # act
        result = cal.divide(a, b)

        # assert
        expected = 5
        assert result == expected

    def test_divide_zero(self):
        # arrange
        a = 15
        b = 0
        cal = Calculator()
       

        # act and assert
        with pytest.raises(ZeroDivisionError, match = "Division by zero error"):
            result = cal.divide(a, b)

       

    

    


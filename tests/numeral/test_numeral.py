"""Test cases for Roman numeral"""
# Standard library

#3rd Part library
import pytest

# Project library
from numeral.roman import to_roman
from numeral.roman import NumberOutOfRange

    
@pytest.mark.parametrize(
    "arabic_num, roman_num",
    [
        #Base case
        (1, 'I'),
        (5, 'V'),
        (10,'X'),
        (50,'L'),
        (100,'C'),
        (500,'D'),
        (1000,'M'),
        
        # Additive case
        (2,'II'),
        (3,'III'),
        (6,'VI'),
        
        # Subtraction case
        (4,'IV'),
        (9,'IX'),
    ]
)
def test_to_roman(arabic_num, roman_num):
    # Arrange
    
    # Act
    result = to_roman(arabic_num)
    
    # Assert
    assert result == roman_num
    

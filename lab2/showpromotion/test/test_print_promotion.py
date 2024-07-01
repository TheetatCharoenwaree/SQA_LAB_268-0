import pytest
import source.print_promotion as pp
#pytest showpromotion\test\test_printpromotion.py


def test_TS001_TC01_only_icecream():
    icecream_result = pp.print_promotion(total_cost = 500)
    assert icecream_result == 1

def test_TS001_TC02_only_icecream():
    icecream_result = pp.print_promotion(total_cost = 699)
    assert icecream_result == 1    




def test_TS002_TC01_only_cake():
    cake_result = pp.print_promotion(total_cost = 700)
    assert cake_result == 1

def test_TS002_TC02_only_cake():
    cake_result = pp.print_promotion(total_cost = 1199)
    assert cake_result == 1
    



def test_TS003_TC01_icecream_and_cake():
    result = pp.print_promotion(total_cost = 1200)
    assert result == (1,1)
    #(icecream , cake)

def test_TS003_TC02_icecream_and_cake():
    result = pp.print_promotion(total_cost = 1700)
    assert result == (2,1)
    #(icecream , cake)

def test_TS003_TC03_icecream_and_cake():
    result = pp.print_promotion(total_cost = 1900)
    assert result == (1,2)
    # (icecream , cake)

def test_TS003_TC04_icecream_and_cake():
    result = pp.print_promotion(total_cost = 2400)
    assert result == (2,2)
    # (icecream , cake)

def test_TS003_TC05_icecream_and_cake():
    result = pp.print_promotion(total_cost = 2499)
    assert result == (2,2)
    # (icecream , cake)



def test_TS004_TC01_no_promotion():
    result = pp.print_promotion(total_cost = 499)
    assert result == pp.NO_GIFT

def test_TS004_TC02_no_promotion():
    result = pp.print_promotion(total_cost = 0)
    assert result == pp.NO_GIFT

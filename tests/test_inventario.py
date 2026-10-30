import pytest 
from src.inventario import clasificar_stock, calcular_sobrestock
 
def test_stock_agotado(): 
    assert clasificar_stock(0, 20) == "AGOTADO" 
 
def test_stock_critico(): 
    assert clasificar_stock(7, 20) == "CRITICO" 
 
def test_stock_bajo(): 
    assert clasificar_stock(15, 20) == "BAJO" 
 
def test_stock_normal(): 
    assert clasificar_stock(30, 20) == "NORMAL" 

def test_stock_exceso(): 
    assert clasificar_stock(50, 20) == "EXCESO"

def test_stock_sobrestock(): 
    assert calcular_sobrestock(50, 20) == 30
 
def test_stock_invalido(): 
    with pytest.raises(ValueError): 
        clasificar_stock(-2, 20) 
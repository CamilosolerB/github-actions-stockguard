def clasificar_stock(stock_actual: int, stock_minimo: int) -> str: 
    if stock_actual < 0: 
        raise ValueError("El stock actual no puede ser negativo") 
    if stock_minimo <= 0: 
        raise ValueError("El stock minimo debe ser mayor que cero") 
    if stock_actual == 0: 
        return "AGOTADO" 
    if stock_actual <= stock_minimo * 0.5: 
        return "CRITICO" 
    if stock_actual <= stock_minimo: 
        return "BAJO" 
    if stock_actual > stock_minimo * 2:
        return "EXCESO"
    return "NORMAL" 

def calcular_sobrestock(stock_actual: int, stock_minimo: int) -> int: 
    return stock_actual - stock_minimo

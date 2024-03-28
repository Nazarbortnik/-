import re

def calculate(expression):
    expression = re.sub(r'\s+', '', expression) 
    pattern = r'\(([^()]+)\)'
    while re.search(pattern, expression):
        sub_expression = re.search(pattern, expression).group(0)  
        sub_result = calculate(sub_expression[1:-1])  
        expression = expression.replace(sub_expression, str(sub_result))  

   
    mul_div = re.findall(r'\d+\.?\d*[\*\/]-?\d+\.?\d*', expression)
    for item in mul_div:
        a, op, b = re.split(r'([\*\/])', item)
        result = eval(f'{a}{op}{b}')
        expression = expression.replace(item, str(result))

   
    add_sub = re.findall(r'\d+\.?\d*[\+\-]-?\d+\.?\d*', expression)
    for item in add_sub:
        a, op, b = re.split(r'([\+\-])', item)
        result = eval(f'{a}{op}{b}')
        expression = expression.replace(item, str(result))

    return float(expression)

expression = "((3.5*2-1)/2)+4.2"
result = calculate(expression)
print(result)

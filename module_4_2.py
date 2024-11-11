def test_function():  # задаем первую ф-ю - ОВ объемлющая
    def inner_function():  #задаем вторую ф-ю - встроенная - ОВ локальная
        print("Я в области видимости функции test_function")
    inner_function()  # вызываем вторую ф-ю внутри первой ф-и - все ОК
test_function()
# inner_function() - попытка вызвать на уровень выше- ОВ глобальная - выдает ошибку:
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?


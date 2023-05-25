# Дано: список dict-объектов вида вида {"key": "value"}, 
# например [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}].
# Напишите функцию, которая удаляет дубликаты из этого списка. 
# Для примера выше возвращаемое значение может быть равно [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
# Обязательное условие: функция не должна иметь сложность O(n^2).

def check_list(list_with_values: list) -> list:
    """
    Проверяет список на дубликаты.

    Возвращает:
        list : список с уникальными значениями.
    """
    result = {}
    for element in list_with_values:
        temprory = str(element)
        if not temprory in result:
            result[temprory] = element

    return [value for value in result.values()]
    
list_with_values = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

def test_check_list():
    expected_list = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}]
    assert check_list(list_with_values) == expected_list

test_check_list()

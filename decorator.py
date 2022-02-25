# Verifica se o argumento é divisível por 2
# caso contrário retorna None
verify = lambda x: x if (x % 2 == 0) else None

# Nosso decorador fica resposável por interceptar a função onde ele será inserido
# e fará as modificações necessárias
def not_pair_exception(function):
    def wrapper(*args, **kwargs):
        # A função map irá receber a lambda (verify) que ficará responsável
        # por dizer se existe algum valor ímpar.
        # Caso sim, sobe uma excessão
        verified_numbers = list(map(verify, args))
        if None in verified_numbers:
            raise Exception("We can't add not pairs numbers")
        return function(*args, **kwargs)
    return wrapper


@not_pair_exception
def add_numbers(*numbers) -> list:
    return numbers

try:
    add_numbers(2, 4, 9)
except Exception as err:
    print(f"Error -> {err}")
finally:
    authorized_numbers = add_numbers(6, 8, 10)
    print(f"Success -> {authorized_numbers}")
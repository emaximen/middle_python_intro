"""Генератор приветствий."""
from pprint import pprint as pp


def greeting(name: str) -> str:
    """Возвращает текст приветствия.

    Args:
        name: Имя пользователя.

    Returns:
        str: Текст приветствия.
    """
    pp(name.lower())
    return 'Привет, {0}'.format(name.title())

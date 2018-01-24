from enum import IntEnum
from enum import Enum
from enum import auto
from datetime import datetime


class NameHeaders(IntEnum):
    """Название заголовок таблицы."""
    ID = 0
    DATE = 1
    USER_ID = 2
    DURATION = 3
    MEDIUM = 4
    SOURCE = 5
    COST = 6
    ORDER_ID = 7
    AMOUNT_PAID = 8


# константы для подчёта LTV
class OptLTV(Enum):
    """Константы для подчёта LTV"""
    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)
    DATETIME = auto()
    PAID = auto()
    ID_USER = auto()
    AMOUNTS = auto()


# Вспомогательные фукнции
def conv_float(value: str) -> float:
    """ Конвертирует строку в число с плавующей запятой"""
    return float(value.replace(',', '.'))


def print_collection(stats: dict):
    for key, value in stats.items():
        print(f"{key}:{value}")


def print_user(stats: dict, user_id: str):
    _user = stats.get(user_id, None)
    if _user is not None:
        for key, values in _user.items():
            if key is OptLTV.DATETIME:
                calendar = [value.strftime(outdate_format) for value in values]
                print(f"{key}: {calendar}")
            else:
                print(f"{key}:{values}")


# название заголовок таблиц
headers = ("id", "date", "user_id",	"duration",	"medium", "source", "cost", "order_id", "amount_paid")
# путь до таблицы.
path_data = "../data"
data_txt = f"{path_data}/data_no_header.txt"

# формат времени
date_format = "%d.%m.%Y %H:%M"
outdate_format = "%d.%m.%Y"

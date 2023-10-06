import numpy as np

from app.models.lottery_model import Compera


def generate_lottery_numbers() -> list:  # 返回类型为list
    lottery_numbers = np.random.choice(
        np.array(
            [
                f"{i: 02d}" for i in range(1, 31)
            ]
        ),  # 从1-30中随机选取
        5,  # 生成5个随机数
        replace=False  # 没有重复值
    )
    return list(lottery_numbers)  # 返回随机数


def compare_two_list(list1: list, list2: list) -> Compera:
    common = list(set(list1).intersection(set(list2)))
    return Compera(common_numbers=common, match=len(common))

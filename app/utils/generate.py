import numpy as np


def generate_lottery_numbers() -> list:  # 返回类型为list
    lottery_numbers = np.random.choice(
        np.array(
            [
                f"{i: 02d}" for i in range(1, 31)
            ]
        ),  # 从1-30中随机选取 default:1
        5,  # 生成5个随机数 default:1
        replace=False  # 没有重复值  default:True
    )
    return list(lottery_numbers)  # 返回随机数


if __name__ == "__main__":
    for i in range(100):
        print(generate_lottery_numbers())

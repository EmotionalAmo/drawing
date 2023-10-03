import numpy as np


def random() -> list:                           # 返回类型为list
    random_num = np.random.choice(
        np.array([f"{i:02d}" for i in range(1, 31)]),    # 从1-30中随机选取 default:1
        5,                                      # 生成5个随机数 default:1
        replace=False                           # 没有重复值  default:True
    )
    return list(random_num)                     # 返回随机数


print(random())

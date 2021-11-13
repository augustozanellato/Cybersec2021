def fn(param_1, param_2, param_3) -> int:
    ivar2 = (param_3 - param_2) // 2 + param_2
    if param_1 < ivar2:
        return fn(param_1, param_2, ivar2 - 1) * 2
    elif ivar2 < param_1:
        return fn(param_1, ivar2 + 1, param_3) * 2 + 1
    else:
        return 0

import numpy as np
#평균 제곱 오차 E = 1/2 sigma start =k ~ n (y - t)^2


def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t)**2)


y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]    # 신경망이 추정한 값
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]                          # 정답

print(mean_squared_error(np.array(y), np.array(t)))         # 2와 차이나는 오차율이 얼마 되지 않음

y = [0.1, 0.05, 0.1, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]    # 신경망이 추정한 값
print(mean_squared_error(np.array(y), np.array(t)))         # 2와의 오차율이 꽤 높음
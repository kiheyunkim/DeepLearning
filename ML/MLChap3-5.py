import numpy as np
a = np.array([0.3, 2.9, 4.0])
exp_a = np.exp(a);
print(exp_a);

sum_exp_a = np.sum(exp_a)

y = exp_a / sum_exp_a
print(y)

a = np.array([1010, 1000, 990])
print(a)
#-----> 큰 수이기 때문에 오버 플로가 발생된다.
#따라서 가장 큰 숫자와 작은 숫자의 차를 이용해서
#전체 숫자들을 줄여주고 계산한다.

#print(np.exp(a) / np.sum(np.exp(a)))

c = np.max(a)
print(c)
print(a - c)

print(np.exp(a-c)/np.sum(np.exp(a-c)))

#따라서 위에서 했던 공식등을 활용하여 만드는 함수
def softmax(a):
    c=np.max(a)
    exp_a = np.exp(a-c) #OverFlow 방지
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a = np.array([0.3, 2.9, 4.0])
y = softmax(a)
print(y)
print(np.sum(y))
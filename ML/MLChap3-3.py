import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

#1층 신경망 처리
X = np.array([1.0, 0.5])    #입력부
W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])#각각 다음 노드로 가는 가중치
B1 = np.array([0.1, 0.2, 0.3]) #각노드에게 더해줘야하는 편향치

print(X.shape)
print(W1.shape)
print(B1.shape)

print(X)
print(W1)
print(B1)

A1 = np.dot(X, W1) + B1
print(A1)
Z1 = sigmoid(A1)
print(Z1)
#1층 신경망 처리 끝

#2층 신경망 처리
W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
B2 = np.array([0.1, 0.2])

print(W2.shape)
print(B2.shape)

Z2 = np.dot(Z1, W2) + B2        ## 1층에서 완료된 값들과 가중치를 곱하고 편향을 더해줌
print(Z2)

def identity_function(x):
    return x

W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
B3 = np.array([0.1, 0.2])

A3 = np.dot(Z2, W3) + B3
Y = identity_function(A3);
print(1)
print(Y)

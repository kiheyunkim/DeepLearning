#손글씨 인식
import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

#시간 좀 걸림
(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

print(x_train.shape)
print(t_train.shape)
print(x_test.shape)
print(t_test.shape)

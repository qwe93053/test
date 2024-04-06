import time
from ecpy.curves import Curve, Point
from gmpy2 import mpz, is_prime, random_state, mpz_urandomb, mpz_random, powmod, bit_length, mul, invert, t_mod, next_prime, f_div, mpfr, gcd
import random
import sys
import hashlib




# 定義橢圓曲線的參數
curve = Curve.get_curve('secp256k1')

# 定義兩個點的座標
rand=random_state(random.randrange(sys.maxsize))
bits=512
q = mpz(2)**(bits - 1) + mpz_urandomb(rand, bits - 1)
p = curve.generator
x_u=mpz_random(rand, q)

P = int(x_u) * p
Q = Point(0xa8465a758b1f5d072de759778fb7036e8e43d0bc2d0fb753f7916a686666891d, 
          0xa94fcc9e6b133d8999586fa33a3982f2dbef28983788ec04bdcd4c3e6828ecd0, 
          curve)
print(P)

# 運行多次取平均
num_iterations = 1000  # 執行次數
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    R = P + P
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations

# 輸出平均執行時間
print("點加法平均時間：", average_time, "秒")


#-----------------------------------------------------------------------------------------------------------

# 定義點的座標
rand=random_state(random.randrange(sys.maxsize))
bits=512
q = mpz(2)**(bits - 1) + mpz_urandomb(rand, bits - 1)
p = curve.generator
x_u=mpz_random(rand, q)

# 運行多次取平均
num_iterations = 1000  # 執行次數
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    R = int(x_u) * p
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations

# 輸出平均執行時間
print("點乘法法平均時間：", average_time, "秒")

#-----------------------------------------------------------------------------------------------------------
# 建立 SHA-512 哈希物件
hash_function = hashlib.sha512()
message = b"Hello, world!"

# 運行多次哈希操作並計時
num_iterations = 1000  # 執行哈希操作的次數
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    hash_function.update(message)
    hash_result = hash_function.digest()
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations

# 輸出結果和執行時間
print("哈希函數平均執行時間:", average_time, "秒")
#-----------------------------------------------------------------------------------------------------------

# 定義哈希函數
def hash_func(x):
    temp1 = hashlib.sha512()
    temp2 = hashlib.sha512()
    temp3 = hashlib.sha512()
    temp4 = hashlib.sha512()
    temp1.update(x + b"1")
    temp2.update(x + b"2")
    temp3.update(x + b"3")
    temp4.update(x + b"4")
    ret_str = temp1.hexdigest() + temp2.hexdigest() + \
        temp3.hexdigest() + temp4.hexdigest()
    return ret_str

def H1_hash(uid, x, y, bits):
    temp = hash_func(str(uid).encode('utf-8') +
                     str(x).encode('utf-8') + str(y).encode('utf-8'))
    H1_hash_value = mpz(temp[: bits - 2], 16)
    return H1_hash_value

def H4_hash(x, bits):
    temp = hash_func(str(x).encode('utf-8'))
    H4_hash_value = mpz(temp[: bits - 2], 16)
    return H4_hash_value

uid = 'Alice'
p_pub = (0xd14c0285591f0f352dcd34b6afe0c1cef73565427ccdf90b4ff7b839ab8db67b , 0x7ba0b0555122cbaea57fb17e1b43505e345bfc22217ee08dad8a313f736169b8)
p_pub = int(mpz_random(rand, q)) * curve.generator
z_u = mpz_random(rand, q)
Y_u = int(z_u) * p
# 運行多次取平均-h1
num_iterations = 100000  # 執行次數
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    # 使用 hash_func 哈希函數計算哈希值
    result = H1_hash(uid, Y_u, p_pub, 512)
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations
print("h1哈希函數平均執行時間:", average_time, "秒")


T_un=(0x2079480cb89dcde2ef957108690bcf9bba8fd3c1b96ebb02fcad8170ca23a85b , 0x716d83bee84bb79c9a03607c0f8fe74beafc3f3255049d6db5d7f4eae07bc320)

# 運行多次取平均-h4
num_iterations = 100000  # 執行次數
total_time = 0
for _ in range(num_iterations):
    start_time = time.time()
    # 使用 hash_func 哈希函數計算哈希值
    result = H4_hash(Y_u, 512)
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations
print("h4哈希函數平均執行時間:", average_time, "秒")


T_un=(0x2079480cb89dcde2ef957108690bcf9bba8fd3c1b96ebb02fcad8170ca23a85b , 0x716d83bee84bb79c9a03607c0f8fe74beafc3f3255049d6db5d7f4eae07bc320)

#-----------------------------------------------------------------------------------------------------------

# 運行多次取平均-指數運算
num_iterations = 1000  # 執行次數
total_time = 0
a=mpz(2)
b=512

for _ in range(num_iterations):
    start_time = time.time()
    # 進行運算
    c=a**b
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations
# 輸出結果和執行時間
print("指數運算時間:", average_time, "秒")

# 運行多次取平均-乘法運算
num_iterations = 10000  # 執行次數
total_time = 0
a=3401251992125380327022914746068595296167475114871847654739510444247833679662081781599398917378110794505931368546903479314330897470381401262047233405206046
b=5482383675437312539851890816995490672938239479025322190664797442484991333129081378339667204051015458008320360459086258049121851884188099496800690052324836
a=123
b=456
for _ in range(num_iterations):
    start_time = time.time()
    # 進行運算
    c=a*b
    end_time = time.time()
    total_time += end_time - start_time

# 計算平均時間
average_time = total_time / num_iterations
# 輸出結果和執行時間
print("乘法運算時間:", average_time, "秒")

#-----------------------------------------------------------------------------------------------------------

# 选择椭圆曲线参数
params = parameters.get_params('ss512')

# 随机选择两个椭圆曲线上的点
P = params.E.random_point()
Q = params.E.random_point()

# 测试配对运算的时间
num_iterations = 100
total_time = 0

for _ in range(num_iterations):
    start_time = time.time()
    result = pairing(params, P, Q)
    end_time = time.time()
    total_time += end_time - start_time

# 计算平均时间
average_time = total_time / num_iterations

print("配对运算平均时间：", average_time, "秒")
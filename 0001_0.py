import random

def ran_num():
    # uniform a <= x <= b 浮点数
    # randint a <= x <= b
    # randrange a <= x <= b, step
    return random.randint(0,9)

def ran_lchar():
    return chr(random.randint(65, 90))

def ran_bchr():
    return chr(random.randint(97, 122))

def gen_activation_code():
    string = ''
    for x in range(20):
        i = random.randint(1,3)
        if i == 1:
            string += str(ran_num())
        elif i == 2:
            string += ran_bchr()
        else:
            string += ran_lchar()
    return string

str_list = [gen_activation_code() for x in range(200)]
print(str_list)
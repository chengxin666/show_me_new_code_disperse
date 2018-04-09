import pymongo
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


def save_200_cdk():
    str_list = [gen_activation_code() for x in range(200)]
    client = pymongo.MongoClient('localhost', 27017)
    db = client['cdks']
    cdk_list = db['cdk-list']
    for cdk in str_list:
        data = {
            'cdk':cdk
        }
        cdk_list.insert(data)
    
    for item in cdk_list.find():
        print(item['cdk'])

if __name__ == '__main__':
    # save_200_cdk()
    client = pymongo.MongoClient('localhost', 27017)
    db = client['cdks']
    cdk_list = db['cdk-list']
    for item in cdk_list.find():
        print(item['cdk'])

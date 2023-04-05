import re

# try to learn re
if __name__ == '__main__':
    # text = '18812345678，他还有一个电话号码是18887654321，他爱好的数字是01234567891，他的座机是：0571-52152166'
    # print(re.findall(r'^\d{4}-\d{8}|^1\d{10}', text))

    # text = 'barbar carcar harhel'
    # print(re.findall(r'(\w{3})(\1)', text))

    text = '随机数字：01234567891，座机1：0571-52152166，座机2：0571-52152188-1234'
    print(re.findall('\d{3,4}-\d{7,8}-\d{3,4}|\d{3,4}-\d{7,8}',text))



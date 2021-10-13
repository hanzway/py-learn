# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/8 12:26
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : d5_encry_pwd.py
# @Project : py-learn

"""
example:
123456
encry_string =
'DMkJ7E5jihm1c8yT9Kb3flik6HjCEI8Wb7FiC79LX%2BXMl%2FPlg33fKk8aOYtiw9xkI84EVwUBdcnimY%2FqfXOMAw%3D%3D'


from pyDes import *

data = "Please encrypt my data"
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
# For Python3, you'll need to use bytes, i.e.:
#   data = b"Please encrypt my data"
#   k = des(b"DESCRYPT", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)
assert k.decrypt(d, padmode=PAD_PKCS5) == data

"""
import hashlib
from pyDes import des, CBC, PAD_PKCS5

encryString = 'MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJL0JkqsUoK6kt3JyogsgqNp9VDGDp+t3ZAGMbVoMPdHNT2nfiIVh9ZMNHF7g2XiAa8O8AQWyh2PjMR0NiUSVQMCAwEAAQ=='


def desEncrypt(data, pwd):
    """
    des cbc模式加密
    data:poros-authcenter/secret/xxx 接口返回data
    pwd:密码
    """
    x = des(data, CBC, [1, 2, 3, 4, 5, 6, 7, 8], padmode=PAD_PKCS5)
    k = x.encrypt(pwd)
    return base64.b64encode(k).decode()


def md5_encrypt(data, pwd):
    """
    加盐：data；
    密码：pwd
    """
    obj = hashlib.md5(data.encode('utf-8'))
    obj.update(pwd.encode('utf-8'))
    result = obj.hexdigest()
    return result


def des_encry():
    data = b'Please encrypt my data'
    k = des(b'DESCRYPT', CBC, b'\0\0\0\0\0\0\0\0', pad=None, padmode=PAD_PKCS5)
    # For Python3, you'll need to use bytes, i.e.:
    #   data = b"Please encrypt my data"
    #   k = des(b"DESCRYPT", CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
    d = k.encrypt(data)
    print("Encrypted: %r" % d)
    print("Decrypted: %r" % k.decrypt(d))
    assert k.decrypt(d, padmode=PAD_PKCS5) == data


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
import base64


def other_rsa():
    message = 'hello ghost hello ghost'
    with open('ghost-public.pem', "r") as f:
        key = f.read()
        # 导入读取到的公钥
        rsakey = RSA.importKey(key)
        # 生成对象
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        # 通过生成的对象加密message明文，注意，在python3中加密的数据必须是bytes类型的数据，不能是str类型的数据
        cipher_text = base64.b64encode(cipher.encrypt(message.encode(encoding="utf-8")))
        print(cipher_text)

    with open('ghost-private.pem') as f:
        key = f.read()
        # 导入读取到的私钥
        rsakey = RSA.importKey(key)
        # 生成对象
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        # 将密文解密成明文，返回的是一个bytes类型数据，需要自己转换成str
        text = cipher.decrypt(base64.b64decode(cipher_text), "ERROR")
        the_virgin = text.decode(encoding='utf-8')
        print(the_virgin, type(the_virgin))
    # # 结果：
    # b'meBtYXP35VNjtWXsONDluweXdG98tMHjb5GxBLFJ0GJzo+96wSrHe8SDhNJweDJP6/OdeIQ8jP1HKCK+aC9HA12YMSUUqcixsY5s8QUyTs+fkMjGrlC6I7hPLO4DGQbFXEY0jiqP9ycgmAi5FCsDMcm0oEm8/fVzv7vl9QarSN4='  # 加密后的密文
    # 解密后的明文
    # b'hello ghost, this is a plian text'


if __name__ == '__main__':
    print(other_rsa())

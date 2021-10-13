# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2021/10/8 20:44
# @Author : qingwei.han
# @Email : qingwei.han@tcl.com
# @File : d6_key.py
# @Project : py-learn


from Crypto import Random
from Crypto.PublicKey import RSA

def get_key():
    # 伪随机数生成器
    random_generator = Random.new().read

    # RSA算法生成实例
    rsa = RSA.generate(1024, random_generator)

    # master的秘钥对的生成
    private_pem = rsa.exportKey()
    # --------------------------------------------生成公私钥对文件-----------------------------------------------------------
    with open('master-private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open('master-public.pem', 'wb') as f:
        f.write(public_pem)

    # -------------------------------------------------------------------------------------------------------------------
    # ghost的秘钥对的生成
    private_pem = rsa.exportKey()
    with open('ghost-private.pem', 'wb') as f:
        f.write(private_pem)

    public_pem = rsa.publickey().exportKey()
    with open('ghost-public.pem', 'wb') as f:
        f.write(public_pem)



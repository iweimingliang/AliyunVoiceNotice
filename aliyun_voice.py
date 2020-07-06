#!/usr/bin/env python3

import requests
import urllib
import secrets
import string
import hmac
import base64
import datetime
import json
from hashlib import sha1

class AliyunVoice():
    def __random_number(self):
        ''' Generate random numbers '''
        alphanum = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphanum) for i in range(32)) 

        return password

    def __generate_timestamp(self):
        ''' Generate timestamp '''
        timestamp = datetime.datetime.utcnow().isoformat().split('.')[0] + 'Z'
        timestamp = urllib.parse.quote(timestamp, safe='/', encoding=None, errors=None)
       
        return timestamp 

    def __generate_signature(self,key,message):
        ''' Generate signature '''
        hmac_code = hmac.new(key.encode(), message.encode(), sha1).digest()
        return base64.b64encode(hmac_code).decode()
 
    def __string_coding(self,String):
        ''' String format conversion '''
        return urllib.parse.quote(String, safe='/', encoding=None, errors=None)
 
    def set_config(self,AccessKey,Secert,CalledNumber,CalledShowNumber,TtsCode,content):
        ''' Setting parameters ''' 
        #voice_config
        self.__url = 'https://dyvmsapi.aliyuncs.com/'
        self.__Version = '2018-01-11'
        self.__Format = 'json'

        self.__CalledNumber = CalledNumber
        self.__CalledShowNumber = CalledShowNumber
        self.__TtsCode = TtsCode
        self.__TtsParam = '{"content":"{'+ content + '}"}'

        self.__PlayTimes = '3'
        self.__Volume = '50'
        self.__Speed = '100'

        #pub_config
        self.__Format = 'json'
        self.__Version = '2017-05-25'
        self.__SignatureMethod = 'HMAC-SHA1'
        self.__AccessKey = AccessKey
        self.__Secert = Secert
        self.__SignatureVersion = '1.0'
        self.__timestamp = self.__generate_timestamp()
        self.__SignatureNonce = self.__random_number()
        self.__Action = 'SingleCallByTts'


        self.__TtsParam = urllib.parse.quote(self.__TtsParam,safe='/',encoding=None, errors=None)


        self.__sign_string = 'AccessKeyId={_AccessKey}&Action={_Action}&CalledNumber={_CalledNumber}&CalledShowNumber={_CalledShowNumber}&Format={_Format}&SignatureMethod={_SignatureMethod}&SignatureNonce={_SignatureNonce}&SignatureVersion={_SignatureVersion}&Timestamp={_timestamp}&TtsCode={_TtsCode}&TtsParam={_TtsParam}&Version={_Version}'.format(_AccessKey = self.__AccessKey, _Action = self.__Action, _CalledNumber = self.__CalledNumber, _CalledShowNumber = self.__CalledShowNumber, _Format = self.__Format, _SignatureMethod = self.__SignatureMethod, _SignatureNonce = self.__SignatureNonce, _SignatureVersion = self.__SignatureVersion, _timestamp = self.__timestamp, _TtsCode = self.__TtsCode, _TtsParam = self.__TtsParam, _Version = self.__Version)

  
        #生成签名字符串
        self.__string_to_sign = 'GET&%2F&' + urllib.parse.quote(self.__sign_string, safe='/', encoding=None, errors=None)

    def call_voice(self): 
        ''' Send voice announcement '''

        #生成签名
        self.__Signature = self.__generate_signature(self.__Secert,self.__string_to_sign)
        #对生成的签名编码
        self.__Signature = urllib.parse.quote(self.__Signature,safe='/',encoding=None, errors=None)

        #生成请求url
        request_url = self.__url + '?' + 'CalledNumber=' + self.__CalledNumber + '&CalledShowNumber=' + self.__CalledShowNumber + '&TtsCode=' + self.__TtsCode + '&Format=' + self.__Format + '&' + self.__sign_string + '&Signature=' + self.__Signature
    
        r = requests.get(request_url) 
        if r.status_code == 200:
            result= eval(r.text)
            if result['Message'] == 'OK':
                print('Result: Successful.\nmessage:{0}'.format(result))
            else:
                print('Result: Failed.\nmessage:\n{0}'.format(r.text))
        else:
            print('Result: Failed.\nmessage:\n{0}'.format(r.text))

        print(request_url)

    def help():
        pass
        
def main():
    CalledNumber = 'xxxxxxxxxxx'
    CalledShowNumber = 'xxxxxxxxxxxx' 
    AccessKey = 'xxxx'
    Secert = 'xxxx&'
    TtsCode = '语音模板ID'
    content = '语音内容'

    aliyun_voice = AliyunVoice()
    aliyun_voice.set_config(AccessKey, Secert, CalledNumber, CalledShowNumber, TtsCode, content)
    aliyun_voice.call_voice()

if __name__ == '__main__':
    main()

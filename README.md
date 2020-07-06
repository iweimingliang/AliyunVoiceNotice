# AliyunVoice
  阿里云语音通知脚本

## 程序功能
  基于事先定义好的语音模板发送语音通知。
  
## 运行方式
修改main函数中的以下几个参数，然后在命令行运行即可。如果需要放到程序中，根据需求修改即可。

    CalledNumber = 'xxxxxxxxxxx'
    CalledShowNumber = 'xxxxxxxxxxxx' 
    AccessKey = 'xxxx'
    Secert = 'xxxx&'
    TtsCode = '语音模板ID'
    content = '语音内容'
    
## 阿里云相关文档  
### 阿里云语音服务文档
  https://help.aliyun.com/product/54853.html?spm=a2c4g.11186623.6.540.33465ad5Jqkx19
  
### 阿里云语音验证码文档
  https://help.aliyun.com/document_detail/114035.html?spm=a2c4g.11186623.2.25.5f439152riitCl#doc-api-Dyvmsapi-SingleCallByTts
  
### 阿里云公共参数说明文档
  https://help.aliyun.com/document_detail/112500.html?spm=a2c4g.11186623.6.576.514466e4CiOnIw

### 阿里云签名机制文档
  https://help.aliyun.com/document_detail/44434.html?spm=a2c4g.11186623.2.9.793c18aecHLlQG&/#SignatureNonce


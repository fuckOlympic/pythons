# 文件服务


## 概述

上传文件服务器地址：http://192.168.3.90:18310 <br/>
默认 POST 方式<br/>
Content-Type: multipart/form-data<br/>


### 用户上传文件接口

```
POST
/file/client/upload
```

此接口需要在请求头中包含Token

#### 请求参数：
| 参数 | 含义 | 是否必须 |描述 |
| ------ | ------ | ------ | ------ |
| file | 上传文件| 必须 | - |
| use_type | 用途| 必须 | - |

**用途定义：**
* headImage:  头像
* IDImage: 证件照片

#### 返回参数：
```
{
  "code": 0,
  "data": {
    "name": "wKgDWmAHo_iAe6-yAACGW-LElOM182.png",
    "url": "http://192.168.3.90:18004/group1/M00/00/00/wKgDWmAHo_iAe6-yAACGW-LElOM182.png"
  },
  "msg": "上传成功！",
}

```


### 管理后台上传文件接口

```
POST
/file/admin/upload
```

#### 请求参数：
| 参数 | 含义 | 是否必须 |描述 |
| ------ | ------ | ------ | ------ |
| file | 上传文件| 必须 | - |
| use_type | 用途| 必须 | - |

**用途定义：**


#### 返回参数：
```
{
  "code": 0,
  "data": {
    "url": "http://192.168.3.90:18004/group1/M00/00/00/wKgDWmACqOyASO4gAAYB1ymW77M231_big.png",
    "name": "wKgDWmACqOyASO4gAAYB1ymW77M231_big.png"
  }
  "msg": "成功"
}
```
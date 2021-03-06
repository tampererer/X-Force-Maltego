# [IBM X-Force Exchange API] Maltego Local Transforms
Maltego Local Transform to use IBM X-Force Exchange API - https://exchange.xforce.ibmcloud.com/

# Prerequisites
- IBM X-Force Exchange API access
- Python 2.7.x + requests, json module
- Python 3.6.x will probably work.

# 必要なもの
- IBM X-Force Exchange APIのアクセス権
- Python 2.7.x + requests, json モジュール
- Python 3.6.x でもたぶん動作します。

# Setup
- Edit XForce.py and set "apikey" and "apipass" variable with your API key and API pass.
- Put all python files into your working directory. (e.g. C:\Maltego\Transforms\XForce_Exchange)
- Open XForce.mtz to import Maltego configuration.
- The current configuration uses the following directories, so you may have to change them according to your environment. (Maltego -> Transforms -> Transform Manager)  

  Command line = C:\Python36\python.exe  
  Working directory = C:\Maltego\Transforms\XForce_Exchange

# セットアップ
- XForce.py の中で、apikey と apipass という変数に、自分の API key と API Pass を記載してください。
- 全てのPythonファイルを、このTransform用に作ったディレクトリに置いてください。（例： C:\Maltego\Transforms\XForce_Exchange）
- XForce.mtz を開いて、Maltegoの設定をインポートしてください。
- mtzファイルに含まれる設定では、下記のディレクトリが指定されていますが、自分の環境に合わせて変更してください。（Maltego -> Transforms -> Transform Manager）

  Command line = C:\Python36\python.exe  
  Working directory = C:\Maltego\Transforms\XForce_Exchange

# Transforms
- [HA] url_to_categ  
Input: Domain, URL  
Output: Category  
<img src="https://user-images.githubusercontent.com/16297449/53248578-5e65d780-36f9-11e9-8fe7-7fd8bfeda904.png" width="800">

- [HA] url_to_malware  
Input: Domain, URL  
Output: Malware name, MD5 Hash, Domain, IP address  
<img src="https://user-images.githubusercontent.com/16297449/53251046-18ac0d80-36ff-11e9-88fe-10ea6221f0ac.png" width="1200">

- [HA]  ip_to_malware  
Input: IP address  
Output: Malware name, MD5 Hash, Domain  
<img src="https://user-images.githubusercontent.com/16297449/53251134-514be700-36ff-11e9-98bf-6f2c98f4b2ad.png" width="900">

- [HA] hash_to_malware  
Input: Domain, URL  
Output: Malware name, MD5 Hash, Domain, IP address  
<img src="https://user-images.githubusercontent.com/16297449/53250748-62e0bf00-36fe-11e9-8c36-50716fa93fdd.png" width="800">

- [HA]  domain_to_whois  
Input: Domain, URL  
Output: Whois (Email address, registrarName, createdDate, updatedDate)  
<img src="https://user-images.githubusercontent.com/16297449/53250791-80158d80-36fe-11e9-8434-9a6307285901.png" width="800">

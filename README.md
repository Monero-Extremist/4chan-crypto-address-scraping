# 4chan-crypto-address-scraping
Tool to help in harvesting crypto addresses from 4chan threads and archives.

### this runs with python 3

There are 3 python files.

addRip.py - this is the library file

ripArchive.py - this file is used to rip the whole archive and print out findings to the standard output


threadRIP.py - rips a specified thread as variable url



#### output format

The output format is a standard output of json objects seperated by new lines like seen below:

```
{'type': 'eth', 'address': '0x2eed4682197834708c0ea8d11d683440bbe104d1', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xdd74794ceb7ae1312c2aa2281f78ed43c48a5dff', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0x7f6a856b11c4bb61f9430d1f1e715177016d59a5', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xf2ab1027152af6f0b6bb30becf60d45450a9eaf3', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xD0ACCF05878caFe24ff8b3F82F194C62Ed755707', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xdd74794ceb7ae1312c2aa2281f78ed43c48a5dff', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0x1B3d161e0696e5688e0207a182BC5fA48FD0815d', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xf2ab1027152af6f0b6bb30becf60d45450a9eaf3', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xf2ab1027152af6f0b6bb30becf60d45450a9eaf3', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0x2fdcb16a977921fadac3a9e03d18ada77b4aa3f5', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0x4c769928971548eb71a3392eaf66bedc8bef4b80', 'blockchainData': 'n/a'}
{'type': 'eth', 'address': '0xa5a8275f4891a373d362e0df44e6e0b3020b9e01', 'blockchainData': 'n/a'}
```

requires-metadata
=================

A small demo using `pip` + `importlib-metadata` to read requirements
information from a wheeled package.


### demo

```console
$ python t.py  celery
*******************************************************************************
celery:
- pytz (>dev)
- billiard (<4.0,>=3.6.0)
- kombu (<5.0,>=4.4.0)
- vine (>=1.3.0)
$ python t.py  celery --include-extras
*******************************************************************************
celery:
- pytz (>dev)
- billiard (<4.0,>=3.6.0)
- kombu (<5.0,>=4.4.0)
- vine (>=1.3.0)
- pyArango (>=1.3.2) ; extra == 'arangodb'
- cryptography ; extra == 'auth'
- azure-storage (==0.36.0) ; extra == 'azureblockblob'
- azure-common (==1.1.5) ; extra == 'azureblockblob'
- azure-storage-common (==1.1.0) ; extra == 'azureblockblob'
- brotli (>=1.0.0) ; (platform_python_implementation == "CPython") and extra == 'brotli'
- brotlipy (>=0.7.0) ; (platform_python_implementation == "PyPy") and extra == 'brotli'
- cassandra-driver ; extra == 'cassandra'
- python-consul ; extra == 'consul'
- pydocumentdb (==2.3.2) ; extra == 'cosmosdbsql'
- couchbase ; extra == 'couchbase'
- couchbase-cffi ; (platform_python_implementation == "PyPy") and extra == 'couchbase'
- pycouchdb ; extra == 'couchdb'
- Django (>=1.8) ; extra == 'django'
- boto3 (>=1.4.6) ; extra == 'dynamodb'
- elasticsearch ; extra == 'elasticsearch'
- eventlet (>=0.24.1) ; extra == 'eventlet'
- gevent ; extra == 'gevent'
- librabbitmq (>=1.5.0) ; extra == 'librabbitmq'
- backports.lzma ; (python_version < "3.3") and extra == 'lzma'
- pylibmc ; extra == 'memcache'
- pymongo[srv] (>=3.3.0) ; extra == 'mongodb'
- msgpack ; extra == 'msgpack'
- python-memcached ; extra == 'pymemcache'
- pyro4 ; extra == 'pyro'
- redis (>=3.2.0) ; extra == 'redis'
- riak (>=2.0) ; extra == 'riak'
- boto3 (>=1.4.6) ; extra == 's3'
- softlayer-messaging (>=1.0.3) ; extra == 'slmq'
- ephem ; extra == 'solar'
- sqlalchemy ; extra == 'sqlalchemy'
- boto3 (>=1.4.6) ; extra == 'sqs'
- pycurl ; extra == 'sqs'
- tblib (>=1.3.0) ; extra == 'tblib'
- PyYAML (>=3.10) ; extra == 'yaml'
- kazoo (>=1.3.1) ; extra == 'zookeeper'
- zstandard ; extra == 'zstd'
```

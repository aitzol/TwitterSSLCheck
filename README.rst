TwitterSSLCheck
===============

This small package's pupouse is to check the server support for the new 2048 bit SSL cert of Twitter.

You must read more about this on 
https://dev.twitter.com/discussions/23085
https://dev.twitter.com/blog/rest-api-ssl-certificate-updates

As said in https://dev.twitter.com/discussions/23085 twitter userstream api endpoint has already enabled the new certificate so we open a connection to this endpoint. If the connection doesn't raise a SSL exception your server supports the new certificate. If it raises an exceptioon you must download and install the new certificates (https://www.symantec.com/page.jsp?id=roots)

Instalation and usage
---------------------

install with pip::

  $ pip install TwitterSSLCheck


Set the environment variables:

CONSUMER_KEY
CONSUMER_SECRET
ACCESS_TOKEN
ACCESS_TOKEN_SECRET

now run::
  
  $ check_ssl

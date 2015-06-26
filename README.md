#negaposi
##Introduction
This program judge negative or positve from twitter.


##How to use

###Make configure file, e.g., `secret.ini`

```
[oauth]
consumer_key = your_consumer_key
consumer_secret = your_consumer_secret

access_token = your_access_token
access_token_secret = your_access_token_secret
  
[negaposi]
dict = your_dictionary_path
```

###Download dictionary(単語感情極性対応表)
[http://www.lr.pi.titech.ac.jp/~takamura/pndic_en.html](http://www.lr.pi.titech.ac.jp/~takamura/pndic_en.html)

If you want to judge english tweets, you should download `pn_en.dic`.

If you want to judge japanese tweets, you should download `pn_ja.dic`.



###How to execute

```
$ git clone https://github.com/daguniko/negaposi.git
$ cd negaposi
$ ./negaposi.py
```

# SimplePhishingSpammer

SimplePhishingSpammer adalah simple bot otomatis untuk spam web phishing simple login form dengan 2 input username dan password,atau bisa di kustomisasi !

  - Dibuat dengan Python 3
  - Random username dan password
  - Mudah digunakan
  - Script simple mudah di kustomisasi
  - Gunain kalo kamu kesel terima link web phishing simple login form dari orang yang gak dikenal
  
### NOTE

Script ini dibuat secara coba - coba dri modifikasi script yang didapetin dri chatGPT dan beberapa fungsi saya ambil dari https://github.com/v3lip/PhishingSpammer, dan script bot spam pertama menggunakan python

Sebagai contoh atau mau coba - coba dulu ada file php form submit sederhana di folder 'tes_spam'
- buat database dan tablenya

```sql
CREATE DATABASE IF NOT EXISTS db_tespython;

USE db_tespython;

CREATE TABLE IF NOT EXISTS tb_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(10),
    password VARCHAR(10)
);
```


## SCREENSHOT


![Screenshot](https://github.com/Seftirobim/SimplePhishingSpammer/assets/16395774/d1a1e619-c221-49ce-a3c7-80d0424a57a6)



## How to use

Install dulu python-nya (kalo belum ada)

jalankan script 
```sh
$ python bot.py
```
Akan ada beberapa pertanyaan

    - 'attribute name value for (username) ?' - masukan value dari attribute name field 'username'     
    - 'attribute name value for (username) ?' - masukan value dari attribute name field 'password'
    - 'What is target url ?' - Masukan target url contoh : https://www.example.com/submit
          

## Installation requirement (kalo belum ada) 

Windows:
```sh
$ python -m pip install -r requirements.txt
```

Linux:
```sh
$ pip3 install -r requirements.txt
```


### Development

Bebas berkontribusi

### Donate

Want to buy me a cendol ?

<a href="https://trakteer.id/seftirobi.m/tip" target="_blank"><img id="wse-buttons-preview" src="https://cdn.trakteer.id/images/embed/trbtn-black-4.png" height="40" style="border:0px;height:40px;" alt="Trakteer Saya"></a>

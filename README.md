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


## Screenshots

![botspam1](https://github.com/Seftirobim/SimplePhishingSpammer/assets/16395774/6e97f3a0-b5d1-442e-b3ea-ef8756d73f87)
![botspam2](https://github.com/Seftirobim/SimplePhishingSpammer/assets/16395774/dbe0cd3e-c99c-482b-86bd-32474b0a6eb7)


## How to use

- Install dulu python-nya (kalo belum ada)
- jalankan script 

```sh
$ python bot.py
```
- masukan target url

## Installation requirements 

Windows:
```sh
$ python -m pip install -r requirements.txt
```

Linux:
```sh
$ pip3 install -r requirements.txt
```



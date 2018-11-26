# FOOD BLOG
A personal blogging website where you can create and share your opinions and other users can read and comment on them.

Built by Amira Mugure

## Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python 3.6.4

## Cloning of the respository
In terminal:
* $ git clone https://github.com/tiffanymugure/foodblog.git
* Creating the Virtual Environment
* sudo apt-get install python3.6-venv
* python3.6 -m venv virtual
* source virtual/bin/activate

## Install Dependencies
* pip3 install -r requirements.txt

 ### Required Libraries
* Flask==0.12.2
* Flask-Bootstrap4==4.0.2
* Flask-Script==2.0.6
* gunicorn==19.7.1

## Running Tests
* python3.6 manage.py test

## Running the web app
* python3.6 manage.py server
* open app in browser by default on 127.0.0.1:5000

## Technology Used
* Python3.6
* Flask
* Heroku

## License Information
MIT License

Copyright(c) 2018 Tiffany Mugure
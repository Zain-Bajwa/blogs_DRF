# Blog Application DRF
Blog application is used to publish an article/blog by an individual or a small group of people. User can register in the app and write his own blog to share his information. He is also able to draft, edit and publish the blog post.
## Installation
Download or clone the repository
```bash
$ git clone https://github.com/Zain-Bajwa/blogs_drf.git
```
Go to the directory `blogs_drf`, create a virtual environment and Install the `requirements.txt`

```bash
$ pip install requirements.txt
```

You also need to install the [PostgreSQL](https://www.postgresql.org/download/) and connect with [django](https://docs.djangoproject.com/en/4.1/) by configuring the `settings.py`.

## Usage
Run `manage.py` file with command line

```bash
$ python manage.py runserver
```
## Features
- ##### User authentication
User can register with email and password. Username is not allowed.


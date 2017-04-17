# TEST CASE / FOR PRICE PLAN

This project is scaffolded by Ivan Semernyakov <direct@beatum-group.ru>

## Architecture

Tested on:

* Ubuntu 14.04
* PostgreSQL 9.6.1
* Redis 2.8.4

## Usage

#### Install Redis:
```
$ sudo apt-get install redis-server
```

#### Clone project:
```
$ mkdir testproject && cd $_
$ git clone https://github.com/beatum/priceplan_test.git 
```

#### Initialize ```virtualenv``` if needed:
```
$ virtualenv {path}
```

#### Activate ```virtualenv```:
```
$ source {virtualenv_path}/bin/activate
```

#### Install ```pip``` dependencies using ```./requirements.txt``` they are not already installed:
```
(env)$ cd project && pip install -r requirements.txt
```

#### Configure PostgreSQL if needed:
```
$ sudo su postgres
$ createuser -P username
$ createdb --owner username dbname
$ exit
```

Check up settings.py !

#### Apply initial migration:
```
(env)$ ./manage.py migrate
```

#### Create admin user and test user:
```
(env)$ ./python manage.py createsuperuser --username admin --email admin@admin.ru
(env)$ ./python manage.py createsuperuser --username user --email user@user.ru
```

#### Test dev environment in ./project
```
(env)$ rqscheduler -i 5 && ./manage.py rqworker  && ./manage.py runserver
```

Or run this command in different terminal:

```
(env)$ rqscheduler -i 5
(env)$./manage.py rqworker 
(env)$./manage.py runserver
```

#### Use commands:

Create test data

```
(env)$ ./manage.py make_task
```

Put test data to history

```
(env)$ ./manage.py clear_task
```

Finally run sheduler - it's must have! 

```
(env)$ ./manage.py run_sheduler
```

#### Check it:

Now you can go to the localhost:8000 and you should see "Hello, World!" - page.

### That's all! Good luck!




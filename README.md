<img src="/img/airflowxheroku.png" title="airflowxheroku">

# Apache airflow instance on heroku

> This is a simple demonstration of Apache Airflow hosted on heroku

> This project implements a simple DAG that fetches the top questions from stackoverflow with the tag "airflow" and forwards to a specified email address

> Actually this is over engineered and can be done with a simple cronjob or a simple .py script but this a simple project I used to learn apache airflow

---

---

<img src="/img/airflowUIII.png" title="airflowxheroku">

## Setup

> To get started a basic knowledge of apache airflow, Heroku cli , AWS S3 bucket and python is required

### Step 1

- **Option 1**

  - 🍴 Fork this repo!

- **Option 2**
  - 👯 Clone this repo to your local machine using `https://github.com/jaywonder20/apache_airflow_basics.git`

### Step 2

- **Create heroku app and add postgreSql Add-on** 🔨🔨🔨

> necessary configuration for heroku app

```shell
Set the following from Heroku CLi
heroku config:set AIRFLOW_HOME=/app
```

---

> set environment variables

```
set AIRFLOW__CORE__SQL_ALCHEMY_CONN in  .profile to your postgreSql connection string
```

Heroku will automatically export .profile to the env on dyno start up. This way if/when your DB URL changes, it will automatically update.

---

- NB: To prevent error during configuration change the "dags_folder" in the airflow.cfg file to a non existent folder to prevent error as the airflow instance is not configured yet
- push app to heroku

### Step 3

> Now some configuration

```
configure the following in the airflow.cfg file
sql_alchemy_conn= postgress db uri
smtp_user =xxxxx@gmail.com
smtp_password =password
smtp_port = 587
```

### Step 4

> create s3 bucket and get key
> https://preventdirectaccess.com/docs/amazon-s3-quick-start-guide/

### Step 5

```shell
set the following connection parameters:

s3_connection
postgres_default
```

<img src="/img/connections.png" title="airflowxheroku">

### Step 6

- Create a Stackoverflow app
- Set the parameters in the variables.json file
- import variables.json file into variables from the airflow UI
  <img src="/img/graph.png" title="airflowxheroku">

### Step 7

- Run the dag from the airflow UI (The dag runs sucessfully and sends the mail to the specified email address)

 <img src="/img/mail.png" title="airflowxheroku">

### Step 8

> secure your account

```shell
 secure the app by adding an extra environment variables to the .profile file.


export AIRFLOW__WEBSERVER__AUTHENTICATE=True
export AIRFLOW__WEBSERVER__AUTH_BACKEND=airflow.contrib.auth.backends.password_auth
```

### Step 9

Open heroku bash with the Command

```
heroku run bash
```

> Start python on the heroku bash and type (you know i mean copy right) the following commands as also described in Airflow’s official
> <a href="https://airflow.incubator.apache.org/security.html" target="_blank">Documentation</a>.

```

>>> import airflow
>>> from airflow import models, settings
>>> from airflow.contrib.auth.backends.password_auth import PasswordUser
>>> user = PasswordUser(models.User())
>>> user.username = 'new_user_name'
>>> user.email = 'new_user_email@example.com'
>>> user.password = 'set_the_password'
>>> session = settings.Session()
>>> session.add(user)
>>> session.commit()
>>> session.close()
>>> exit()

```

If everything went well, you should be able to see this screen in your browser:
<img src="/img/login.png" title="airflowxheroku">

#####Proceed to modify DAG for further customization

## Support

Reach out to me at one of the following places!

- Website at <a href="https://jaywonder20.netlify.app" target="_blank">`jaywonder20.netlify.app`</a>
- Twitter at <a href="http://twitter.com/jaywonder20" target="_blank">`@jaywonder20`</a>
- Linkedin at <a href="http://linkedin.com/in/jaywonder20" target="_blank">`linkedin.com/in/jaywonder20`</a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://linkedin.com/in/jaywonder20" target="_blank">Jaywonder20</a>.

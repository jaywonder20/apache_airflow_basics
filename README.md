<img src="/img/airflowxheroku.png" title="airflowxheroku">

# Apache airflow instance on heroku

> This is a simple demonstration of Apache Airflow hosted on heroku

> This project implements a simple DAG that fetches the top questions from stackoverflow with the tag "airflow" and forwards to a specified email address

> Actually this is over engineered and can be done with a simple cronjob or a simple .py script but this a simple project I used to learn apache airflow

## Example (Optional)

- Clone this repo to your local machine using `https://github.com/jaywonder20/apache_airflow_basics`

### Setup

- create Heroku app
- add postgresSql add to heroku app
- create virtualenv

> necessary configuration for heroku app

```shell

Set the following from Heroku CLi
heroku config:setAIRFLOW**CORE**SQL_ALCHEMY_CONN=<your_postgres_con_string>
heroku config:set AIRFLOW**CORE**LOAD_EXAMPLES=False
heroku config:set AIRFLOW_HOME=/app
heroku config:set AIRFLOW**CORE**FERNET_KEY=<secret_key>
```

---

---

<img src="/img/airflowUIII.png" title="airflowxheroku">

## Setup

> To get started...

### Step 1

- **Option 1**

  - 🍴 Fork this repo!

- **Option 2**
  - 👯 Clone this repo to your local machine using `https://github.com/jaywonder20/apache_airflow_basics.git`

### Step 2

- **Create heroku app and add postgreSql Add-on** 🔨🔨🔨

### Step 3

> Now some configuration

```shell
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
- import variables.jsom file into variables from the airflow UI
  <img src="/img/graph.png" title="airflowxheroku">

---

## Support

Reach out to me at one of the following places!

- Website at <a href="https://jaywonder20.netlify.app" target="_blank">`fvcproductions.com`</a>
- Twitter at <a href="http://twitter.com/jaywonder20" target="_blank">`@jaywonder20`</a>

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © <a href="http://linkedin.com/in/jaywonder20" target="_blank">Jaywonder20</a>.

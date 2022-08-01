# sms_pc project

send sms via web with kavehnegar api

## How to run

1. Install python3, pip3, virtualenv, MySQL in your system.

2. Clone the project `https://github.com/rapexa/sms_pc.git` && cd sms_serial_verification

3. in the app folder, rename the `config.py.sample` to `config.py` and do proper changes.

4. run this comand in MYSQL database : `CREATE DATABASE smsmysql;`

5. run this comand in MYSQL database : `CREATE USER 'smsmysql'@'localhost' IDENTIFIED BY 'test';`

6. run this comand in MYSQL database : `GRANT ALL PRIVILEGES ON smsmysql.* TO 'smsmysql'@'localhost';`

7. run this comand in MYSQL database : `DROP TABLE IF EXISTS messages;`

8. db configs are in config.py. Create the db and grant all access to the specified user with specified password, but you also need to add this table to the database manually: `CREATE TABLE messages (status VARCHAR(30),sender VARCHAR(100) , message VARCHAR(1024));`

9. Create a virtualenve named build using `virtualenv -p python3 venv`

10. Connect to virtualenv using `source venv/bin/activate`

11. From the project folder, install packages using `pip install -r ./app/requirements.txt`

12. Now environment is ready. Run it by `python app/main.py`

### Or you can use Dockerfile

1. get service from some where that got pas service in this project i got service from `https://fandogh.cloud/`.

2. buy for your `fandogh` service `1024mb` ram .

3. make service for mysql and fill the blanks like this : name : `db` , pass : `test` , ram : `512mb` and got `phpmyadmin` GUI service for it.

4. goto `https://db-hologram.fandogh.cloud/server_databases.php` page for your MYSQL service.

5. in this page create database by : Database_name : `smsmysql` , Codeing : `utf8mb4_bin` and push `create` button.

6. choose the `smsmysql` in databases list and in this database choose `SQL` and copy in that editor `CREATE TABLE messages (status VARCHAR(30),sender VARCHAR(100) , message VARCHAR(1024));` and push `go` button.

7. goto to `https://docs.fandogh.cloud/docs/getting-started.html` page for how to deploy project there.

8. in your commmand line in `How to run : TODO : 10`

9. copy `pip install fandogh_cli` in your command line run by (venv).

10. copy and fill in the requrment variable in this text `fandogh login  --username=YOUR_USERNAME --password=YOUR_PASSWORD` in your command line run by (venv).

11. for makeing iso file from your project to run in your `fandogh service` copy : `fandogh image init  --name=app` in your command line run by (venv).

12. for makeing workspace in your `fandogh service` to deploying your version 0.1 of your project in next step to `fandogh service` copy `fandogh image publish --version v0.1` in your command line run by (venv).

13. for deploying your version 0.1 of your project in `fandogh service` copy `fandogh service deploy --version v0.1 --name app` in your command line run by (venv).

14. now you can check your `fandogh service` Dashbourd for makeing sure that you make your own deployed service name app.

15. if you make your service named `app` in your `fandogh service` edit app service ram to : `512mb` ad push `done makeing` button in bottom of the page.

16. now you can see your project in `https://app-hologram.fandogh.cloud/` Domin

#### DONE

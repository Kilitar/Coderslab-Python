# Database installation

Type: Article

Databases are one of data analysts' most commonly used tools. For our course, we will need to install one. A common favorite is `PostgreSQL` – this is the database we are going to install.

## Installation (Windows and MacOS)

Download the `PostgreSQL` database installer from [this website](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).

In the table, we select the newest available version of `PostgreSQL` for our operating system (MacOS, Windows).

We save the installer file to local drive to run it.

Run the installer Installation consists in... clicking the `next` button several times. The only interaction required of us is when we have to enter a password for the default user. Let's enter a password that is easy to remember, security is not a priority in this case. This will not be a production database where such a password should be secure.

In the last step, the installer will ask if we want to install additional software. Answer **no**.

## Installation (Linux)

Installation on Linux systems is a little more complicated. Course materials will include the installation instructions for Ubuntu with the `apt-get` package manager. If you use another package manager of a different Linux distribution, install `PostgreSQL` using [this](https://www.postgresql.org/download/) instruction.

### Installing`PostgreSQL` on Linux

**All the following commands should be typed in the terminal. Confirm each command by pressing enter**.
Start each installation by updating your system (this step may take a while):

``` bash
sudo apt-get update
sudo apt-get -y upgrade
```

Next we need to add repositories that we'll use to download `PostgreSQL` to our computer:

``` bash
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
```

After adding the appropriate repositories, we can install `PostgreSQL`:

``` bash
sudo apt update
sudo apt -y install postgresql-12 postgresql-client-12
```

Next, you need to check that the installation was successful and that the database is running on our system:

``` bash
systemctl status postgresql.service
```

The above command should return the following message:

``` text
● postgresql.service - PostgreSQL RDBMS
    Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
    Active: active (exited) since Sun 2019-10-06 10:23:46 UTC; 6min ago
  Main PID: 8159 (code=exited, status=0/SUCCESS)
     Tasks: 0 (limit: 2362)
    CGroup: /system.slice/postgresql.service
 Oct 06 10:23:46 ubuntu18 systemd[1]: Starting PostgreSQL RDBMS…
 Oct 06 10:23:46 ubuntu18 systemd[1]: Started PostgreSQL RDBMS.
```

If this is the case, you have successfully installed the database.

### Database password

During the installation, the system should ask for a password for logging into the database later. However, if it does not, the password must be set manually. To do this, log in as the `postgres` user. This is the user created automatically during `PostgreSQL` installation. To do it, enter the command:

``` bash
sudo su - postgres
```

Then the password can be changed with the command:

``` bash
psql -c "alter user postgres with password 'yournewpassword'"
```

In the command above, both the `'`, and `"` characters matter!

After changing the password, you can close the terminal.

### Installing pgAdmin

Once we installed the database, we also need to install the graphical interface we are going to use to communicate with the database: the program is called: `pgAdmin`. Installation is started by typing the command in the terminal:

``` bash
sudo apt-get install pgadmin4
```

The installer is going to ask us to set the password (if it doesn't, we will set it when we run the program for the first time). **This password is not the same as our database password!

## First steps

Our database server is installed - to manage it, we need to run the database client. The client is also installed: it is called `pgadmin`. Run this program:

- windows key + 'pgadmin' on Windows,
- command key + space + 'pgadmin' on a Mac
- open terminal and type 'pgadmin4' on Linux.

The client requests a password we set during `pgAdmin` installation.

After logging in correctly, we will see something like this:

![pgadmin](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/pgadmin.png)

On the left there is the menu. As you can see, we have one server, and a database in it. This database is used by `PostgreSQL` and we shouldn't change anything there.

### What if there is no visible server?

If our menu does not show any server, we will have to add it there. We do this by right-clicking on "Servers" and then selecting "Create" -> "Server" from the menu:
![Creating a server step 1](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/create_server_1.png)

Then we need to add the data for the connection:

1. In the "General" tab, fill out server name. It may be anything.
2. In the "Connection" tab, fill out "Host name" field. We need to enter "localhost" there.
3. In the "Connection" tab enter the "Password". We need to enter the password for our database (set during database installation).

After setting these options, click the "Save" button. If everything went fine, our local server should be available in the sidebar menu.

### Adding a new database

Let's create our own database. To do so, just right-click the 'Databases(1)' item and choose 'Create' > 'Database'.

!Creating database step1](images/new_database_1.png)

We enter the name of our new database and click 'Save'.
![Creating database step1](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/new_database_2.png)

The database has been created. It should appear in the side menu.

## Running SQL commands

The `SQL` query language is used to communicate with `PostgreSQL`. To get started, select the newly created database from the menu on the left, right-click it and select 'Query tool'.
![Creating database step1](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/Query_tool.png)

The following window will appear:
![Creating database step1](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/query_tool_2.png)

This is the editor where you should type SQL queries. After typing the commands, we run them using the button with the "play" icon located in the top menu of this window (more or less in the middle).

The results of our queries will appear in the bottom window:
![Creating database step1](/presentations/DTL/en/4.9/W/M_04_S_01/09354648-ce48-453a-aa20-098d13238c84/student_content/60703444-29b2-49d1-a353-cb5be5ac7481/images/data_output.png)

To test the performance of our database, we can enter a query:

``` sql
SELECT datname FROM pg_database;
```

after running it, the bottom window should display all the databases that are created on our server.

You will find out more about `SQL` later in the prework.

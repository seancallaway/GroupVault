# GroupVault
> A team-based password manager with RBAC and a REST API

## Installation

GroupVault will be distributed as a Docker container upon release.

The following environment variables should be passed to the container at runtime:

* `SECRET_KEY` - a 50 character string that must stay the same between deployments
* `DJANGO_ALLOWED_HOSTS` - a space-delimited list of allowed hosts, such as "groupvault groupvault.mydomain.com"
* `SQL_ENGINE` - the Django DB engine to use, such as "django.db.backends.postgresql"
* `SQL_DATABASE` - the name of the database to which to connect
* `SQL_USER` - the name of the user with permissions to the database
* `SQL_PASSWORD` - the password of the user with permissions to the database
* `SQL_HOST` - the host running the database
* `SQL_PORT` - the port on which the database server is listening (default: 5432)

## Development Setup

GroupVault uses Python 3.7 and Django 3.x. To setup your development environment on Linux or Mac OS, do the following
after cloning the repo:

```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Please note that when running the local server, you'll need to set the environment variable `DEBUG=1`, otherwise 
Django's debug mode will be off.

## Meta

Sean Callaway - [@smcallaway](https://twitter.com/smcallaway) - seancallaway@gmail.com

Distributed under the GNU GPL version 3. See ``LICENSE`` for more information.

## Contributing

Contributions are welcome!

1. Fork it (<https://github.com/seancallaway/GroupVault/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

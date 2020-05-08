# GroupVault
> A team-based password manager with RBAC and a REST API

## Installation

GroupVault will be distributed as a Docker container upon release. Once that happens, we'll provide instructions here 
on how to configure and run it.

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

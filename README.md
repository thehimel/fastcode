# fastcode
A repository to practice speed coding

## Getting Started

### Linux Configurations

#### Python Installation

```sh
sudo apt update
sudo apt install software-properties-common

sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9

python3.9 --version
```

#### Configure venv

```sh
sudo apt-get install python3.9-venv
python3.9 -m venv venv3.9
python3.9 -m venv venv
source venv/bin/activate
```

## Testing

```sh
python -m pytest tests
```

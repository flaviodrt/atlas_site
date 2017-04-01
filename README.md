# Atlas Site

Para rodar o projeto, execute os passos abaixo:

Atualize o conda e crie um environment:
```console
conda update conda
conda create --name atlas python=3
source activate atlas-site
```

Instale as bibliotecas dependentes:
```console
pip install -r requirements.txt
```

Crie o banco de dados:
```console
sudo su - postgres
psql
create database atlas;
create user atlas with password 'yourpassword';

alter role atlas set client_encoding to 'utf8';
alter role atlas set default_transaction_isolation to 'read committed';

grant all privileges on database atlas to atlas;
```

```console
cd atlas
```

Configure as variáveis do arquivo `.env` para conexão ao banco de dados
```console
cp .env.sample .env
```

Rode as migrations:
```console
python manage.py migrate
```

Rode o script que popula a base de dados:
```console
./scripts/run_scripts.sh
```

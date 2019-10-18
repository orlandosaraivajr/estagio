## Desenvolvimento de plataforma para Estágios

### Projeto piloto para uma plataforma de divulgação de Estágios

#### Professores envolvidos:

Prof. Me. Orlando Saraiva Júnior
 http://lattes.cnpq.br/5246678822563192

Prof. Dr. Leonardo Souza de Lima
http://lattes.cnpq.br/1283143287684346

Profa. Ma. Dhebora Souza Umbelino Silva
	http://lattes.cnpq.br/0011889719057828

### Como ajudar neste projeto ?

1. Clone o repositório
2. Crie um virtualenv
3. Ative a virtualenv
4. Instale as dependências
5. Configure a instância com o .env
6. Execute os testes

```console
git clone https://github.com/orlandosaraivajr/estagio
cd estagio/
virtualenv venv -p python3
source venv/bin/activate
pip install -r requirements.txt
python manage test
python manage runserver
```

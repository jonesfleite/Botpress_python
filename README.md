Exemplo do Action Server, escrito em Python

## Desdobramento, desenvolvimento

Abaixo você encontrará instruções para implantar este exemplo do Action Server no Heroku.

Pré-requisitos:

- Instale o Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli
- Crie uma conta Heroku (se ainda não tiver uma)
- Clone este repositório: `git clone git@github.com: botpress / action-server-example-python.git`
- `cd action-server-example-python`

Agora implante o aplicativo:

1. `login do heroku`
2. `heroku create`
3. `git push heroku master`
4. Defina o `BOTPRESS_SERVER_URL` para a URL pública de seu servidor Botpress, por exemplo, `https: //34.56.178.34: 3000` ou` https: // botpress.mydomain.com`, usando o seguinte comando: `heroku config: set BOTPRESS_SERVER_URL = {sua URL do servidor Botpress}`

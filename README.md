# InfoJobs Vagas Scraper

Este projeto contém um script em Python que faz scraping das vagas de estágio em TI no site InfoJobs Brasil, extraindo os títulos das vagas listadas na página de resultados.

---

## Objetivo

Extrair de forma automatizada os títulos das vagas de estágio em TI disponíveis no InfoJobs para a localidade especificada.

---

## Requisitos

- Python 3.6 ou superior
- Biblioteca `requests`
- Biblioteca `beautifulsoup4`

Você pode instalar as bibliotecas necessárias com:

```bash
pip install requests beautifulsoup4
```

---

## Como usar

1. Clone ou baixe este repositório.
2. Abra o arquivo `scraper.py` (ou o nome que você deu para o script).
3. Execute o script:

```bash
python scraper.py
```

O script irá fazer uma requisição à página de vagas de estágio em TI no InfoJobs, extrair e mostrar no terminal os títulos das vagas encontradas.

---

## Personalização

- Para mudar a palavra-chave ou a localização das vagas, altere o valor da variável `link` no script, modificando os parâmetros da URL.

---

## Exemplo de saída

```
STATUS:  200 - Request successful!
URL:  https://www.infojobs.com.br/empregos.aspx?palabra=estagio+ti&provincia=176
Found 20 job postings:
-----------------------------------
Job Title: Estágio em Desenvolvimento de Software
-----------------------------------
Job Title: Estagiário(a) de TI
...
```

---

## Avisos importantes

- Este script faz scraping de dados públicos disponíveis no site InfoJobs.  
- Use de forma ética, respeitando as regras do site e evitando sobrecarga com muitas requisições.

---

## Autor

Moisés Souza Santos

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

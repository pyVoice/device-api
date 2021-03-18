<p align="center">
<img src="https://i.imgur.com/xURT3C6.png" width="50%" />
</p>
<p align="center">Assistente pessoal, controlado por voz</p>
<br>

<p align="center">
<img src="https://img.shields.io/github/stars/pyvoice?style=social">
<img src="https://img.shields.io/badge/license-MIT-green.svg">
<img src="https://img.shields.io/badge/python-3.9-green.svg">

<br>

<img alt="GitHub issues" src="https://img.shields.io/github/issues/pyvoice/device-api">
<img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/pyvoice/device-api?color=green">
<img src="https://github.com/pyVoice/device-api/actions/workflows/ci.yml/badge.svg">
</p>

## Sobre

Este repositório contém a *API* responsável por agregar as instalações da aplicação, e alguns dados relativos a estas.

Pode visitar o site em [https://pap.pyvoice.tech](https://pap.pyvoice.tech).

## Funcionamento Geral

O diagrama abaixo representa a forma de funcionamento da *API*, de forma simplificada.

<p align="center">
    <img src="https://i.imgur.com/SyjLKJ5.png">
</p>

## Contribuir

Encontrou um erro? Quer fazer uma correção? Abra uma nova _Issue_ [aqui](https://github.com/pyVoice/site-pap/issues).

Todas as _Issues_ serão revistas e se aprovadas, adicionadas ao projeto.

## Apoios

O projeto teve o apoio das seguintes entidades:

- [Escola Secundária Dr. Augusto César da Silva Ferreira](https://www.esdacsf.pt) pelo corpo docente e equipamentos, que muito ajudou no decorrer da realização do projeto
- [GitHub Student Developer Pack](https://education.github.com/pack) por fornecer ferramentas que apoiaram o desenvolvimento do projeto
- [.TECH Domains](http://get.tech/) por forncer o domínio para o projeto

## Disclaimer

A obtenção, tratamento e divulgação de dados respeita os seguintes pontos:

- Os dados recolhidos são:
    - **`id`**: identificador único e aleatório, para identificar o dispositivo/instalação
    - **`operating_system`**: nome e versão do sistema operativo
    - **`location`**: localização obtida através do endereço IP do cliente, usando o serviço [IPinfo](https://ipinfo.io/)
    - **`version`**: versão da aplicação instalada
- Os dados apenas são usados para fins estatísticos.
- Os dados não são fornecidos a terceiros.
- O acesso aos dados é privado, e apenas disponível para membros da equipa.
- Os dados não sofrem processos de análise, ou qualquer transformação.
- O utilizador pode escolher fornecer ou não fornecer estes dados, de acordo com a sua preferência.
- O utilizador pode sempre contactar a equipa do projeto, a fim de remover os seus dados da base de dados (requer que o utilizador tenha conhecimento do seu `id`)

## Licença

[MIT](https://github.com/pyVoice/site-pap/blob/main/LICENSE)

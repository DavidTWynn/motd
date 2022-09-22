                     )  (
        )         ( /(  )\ )
       (      (   )\())(()/(
       )\  '  )\ (_))/  ((_))
     _((_))  ((_)| |_   _| |
    | '  \()/ _ \|  _|/ _` |
    |_|_|_| \___/ \__|\__,_|

# motd

![GitHub last commit](https://img.shields.io/github/last-commit/davidtwynn/motd?style=plastic)
![GitHub commit activity](https://img.shields.io/github/commit-activity/y/davidtwynn/motd?style=plastic)
![Python version](https://img.shields.io/badge/python%20version-3.10-blue)
![Coding style](https://img.shields.io/badge/code%20style-black-000000.svg)

Collaboration project to create a network device 'message of the day' generator web app.

## Plan:

- React front-end to easily create motd templates for applying them to a device
- Python backend with RestAPI for creating templates with desired inputs
- Jinja2 template engine for generating the text config
- Learn from this project as a foundation for other collaboration projects with Python and React

## Examples

<img src="https://github.com/DavidTWynn/motd/blob/master/images/basic_motd.JPG" width="37%" height="37%">
<img src="https://github.com/DavidTWynn/motd/blob/master/images/template_motd.JPG" width="37%" height="37%">

## Setup Python Backend

Requirements

- Python 3.10
- Jinja2

```bash
git clone https://github.com/DavidTWynn/motd
cd motd
python -m pip install -r requirements.txt
```

## Run Python Backend

```bash
> python .\motd_backend\motd\motd.py

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                  Welcome to                  %
%           9516 Snow Heights Cir NE           %
%                 Albuquerque                  %
%                   NM 87112                   %
%                                              %
%             Model: Cisco IOSvL2              %
% Uptime: 2 weeks, 2 days, 5 hours, 23 minutes %
%  Last change: 23:43:51 UTC Wed Sep 21 2022   %
%  CPU five seconds: 25%/0%; one minute: 15%   %
%                 Memory: 15%                  %
%            Uplink utilization: 5%            %
%                                              %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
```

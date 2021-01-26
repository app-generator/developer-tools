# [Developer tools](https://appseed.us/developer-tools)

Open-Source devtools provided by AppSeed under [EULA License](./LICENSE.md).

<br />

## Install Deps

```bash
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
```

<br />

## Check Assets

> Scan a design/ui kit for missing assets - Status WIP

<br />

**Usage**

```bash
$ python ./check-assets.py
```

<br />

**Sample Output** - [log file](./python ./check-assets.py)

```bash
(env) PS > python.exe .\check-assets.py

 Files (2)
['apps-calendar.html', 'index.html']

 ***** ***** *****

 PROCESSING --> apps-calendar.html | files (1) remaining
 PROCESSING --> index.html | files (0) remaining
 PROCESSING --> apps-calendar.html
 ERR - Missing Asset -> /static/assets/css/classic-horizontal/style-ERROR.css
 ERR - Missing Asset -> /static/assets/images/logo-mini-ERROR.svg
 PROCESSING --> index.html
 ERR - Missing Asset -> /static/assets/images/favicon-ERROR.png
    |
    |
    |
    |
    |- apps-calendar.html
    |    |
    |    |--- CSS: 6 file(s)
    |    |     | /static/assets/vendors/mdi/css/materialdesignicons.min.css
    |    |     | /static/assets/vendors/css/vendor.bundle.base.css
    |    |     | /static/assets/vendors/fullcalendar/fullcalendar.min.css
    |    |     | /static/assets/css/classic-horizontal/style.css
    |    |     | /static/assets/css/classic-horizontal/style-ERROR.css
    |    |     | /static/assets/images/favicon.png

...
...
...



Pages with errors: 2
    |
    |- apps-calendar.html
    |    |     | /static/assets/css/classic-horizontal/style-ERROR.css
    |    |     | /static/assets/images/logo-mini-ERROR.svg
    |
    |- index.html
    |    |     | /static/assets/images/favicon-ERROR.png
```

<br />

## [Html Parser](https://appseed.us/developer-tools/html-parser)

A powerfull **Html Parser** coded in Python / Beatiful Soup library capable to parse flat HTML pages and extract components for various template engines: Pug, Jinja2, CodeIgniter and Laravel. A simple working flow: 

 - HTML theme is loaded into the parser
 - the user selects a page and have the posibility to walk on HTML tree in a interactive way
 - components can be extracted for Jinja2, Laravel, Pug
 
 Read more about this cutting-edge <a href="https://appseed.us/developer-tools/html-parser">HTML Parser</a> developed by AppSeed.

<br />

## [Bootstrap to Bulma CSS](https://appseed.us/developer-tools/bootstrap-to-bulma-css)

Migrate <a href="https://getbootstrap.com/">Bootstrap</a> projects to <a href="https://bulma.io/">Bulma CSS</a>. 
Read more about <a href="https://appseed.us/developer-tools/bootstrap-to-bulma-css">Bootstrap to Bulma CSS</a> tool developed by AppSeed.

<br />

## [Bootstrap to Tailwind CSS](https://appseed.us/developer-tools/bootstrap-to-tailwind-css)

Migrate <a href="https://getbootstrap.com/">Bootstrap</a> projects to <a href="https://tailwindcss.com/">Tailwind CSS</a>. 
Read more about <a href="https://appseed.us/developer-tools/bootstrap-to-tailwind-css">Bootstrap to Tailwind CSS</a> tool developed by AppSeed.

<br />

### Support

For issues and features request, use **Github** or access the [support page](https://appseed.us/support) provided by **AppSeed** 

<br />

[Developer tools](https://appseed.us/developer-tools) provided by **AppSeed**

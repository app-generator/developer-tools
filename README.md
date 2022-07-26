# [Tools for Developers](https://appseed.us/developer-tools/)

A collection with **[tools](https://appseed.us/developer-tools/)** (`open-source` and `closed-source`) built and actively supported by **AppSeed**.  

> `FREE` Tools (MIT license)

- 👉 [Database Introspection Tool](https://github.com/app-generator/devtool-db-introspection): `open-source`, MIT License
- 👉 [Data Converter](https://github.com/app-generator/devtool-data-converter): `open-source`, MIT License
- 👉 [Full-Stack OpenApi Generator](https://github.com/app-generator/devtool-fullstack-generator): `open-source`, MIT License

<br />

> `Closed-Source` Tools, **Free for AppSeed [PRO Users](https://appseed.us/terms/)**

- 🚀 [OpenAPI Editor](https://appseed.us/generator/openapi/): In-Browser editor (built with Vue.js)
- 🚀 [OpenAPI Parser](https://github.com/app-generator/devtool-openapi-parser): Python tool that extracts OpenAPI definitions
- 🚀 [DevTool UI Tester](https://github.com/app-generator/devtool-ui-tester): Test the compilation across multiple environments for React Projects 
- 🚀 [Django Dynamic API](https://appseed.us/developer-tools/django-dynamic-api/): code secure APIs using `DRF` with a minimum effort
- 🚀 [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/): server-side paginated data, search, export PDF, CVS  
- 🚀 [Flask Dynamic API](https://github.com/app-generator/devtool-flask-dynamic-api): code secure APIs using `Flask-RestX` with a minimum effort
- 🚀 [Flask Dynamic DataTables](https://github.com/app-generator/devtool-flask-dynamic-datatb): server-side paginated data, search, export PDF, CVS  

<br />

## ✨ [DB Introspection Tool](https://github.com/app-generator/devtool-db-introspection) `free tool`

`Open-Source` **[developers tool](https://appseed.us/developer-tools/)** that provides simple helpers for legacy databases introspection. Crafted on top of `Python` and [Peewee](http://docs.peewee-orm.com/en/latest/).

- `Peewee` DB Reflection
- Supported DB: SQLite, MySql, PostgreSQL
- DbWrapper Class:
  - `print_all_models()` - returns all tables
  - `print_db_model` - print table definition
  - `dump_tables()` - Dump SQL definitions (all tables) 
  - `dump_tables_data()` - Dump database content (all tables)
  
![Database Introspection Tool - Developers Tools, provided by AppSeed.](https://user-images.githubusercontent.com/51070104/181057709-398e8c10-8f20-48bf-8023-83508d13c112.png)

<br />

## ✨ [Data Converter](https://github.com/app-generator/devtool-data-converter) `free tool`

A tools that provides simple helpers for data management: 

- UI managed by `Flask`
- CSV Files:
  - Print
  - Columns: Remove, Update
  - Add New Column with random values:
    - `timestamp`, `random_int` and `random string` (via Faker)
  - `CSV to JSON` conversion
  
  ![Data Converter - Provided by AppSeed.](https://user-images.githubusercontent.com/51070104/153058975-1947b69f-231d-48cc-afb2-8cc867b8b284.png)

<br />

## ✨ [Full-Stack OpenAPI Generator](https://github.com/app-generator/devtool-fullstack-generator) `free tool`

Starter project that uses an OpenAPI specifications to bind a NodeJs Express backend and a React frontend, using an API-first approach. Generated codebase features and options: 

> **Backend**

- [Express](https://expressjs.com/) is the most popular NodeJs web framework; the following commonly used plugins have been included:
  - [helmet](https://github.com/helmetjs/helmet) is a utility for setting HTTP headers
  - [morgan](https://expressjs.com/en/resources/middleware/morgan.html) is a logging utility
  - [cors](http://expressjs.com/en/resources/middleware/cors.html) is a utility for configuring cross origin request security
  - [express-openapi-validator](https://github.com/cdimascio/express-openapi-validator) is a utility for validating API requests against the OpenAPI specification
- [TypeORM](https://typeorm.io/#/) is an ORM that supports the `DataMapper` pattern, which makes is more attractive in combination with the "API first" approach
- [Express JWT](https://github.com/auth0/express-jwt) and [JWKS-RSA](https://github.com/auth0/node-jwks-rsa) are two utilities for verifying a JWT token authenticity, in an OAuth2 / OpenID connect context

> **React Frontend**

- [Create React App](https://reactjs.org/docs/create-a-new-react-app.html#create-react-app) is the most popular way to start with React; the Seed provides three UI alternatives:
  - [Material UI](https://mui.com/)
  - [Chakra UI](https://chakra-ui.com/)
  - [React Bootstrap](https://react-bootstrap.github.io/)
  - [Ant Design](https://ant.design/)
- [React Redux](https://react-redux.js.org/) is a state container using the immutable state / action / reducer pattern
- [Recharts](https://recharts.org/en-US/) is a charts library built with React and D3
- [React I18Next](https://react.i18next.com/) is a popular internationalization framework for React
- [OpenID AppAuth-Js](https://github.com/openid/AppAuth-JS) is an OAuth2 / OpenID connect flow library 

<br />

## 🚀 [OpenAPI Editor](https://appseed.us/generator/openapi/)

In-Browser Developers Tool - Edit your OpenAPI definition directly in browser and download the generated JSON file. For newcomers, **OpenAPI** is an open-source format for designing `RESTful APIs` and `web services` that serves as a single source of truth for all parties involved in the software development process: developers, testers.

This free service/tools can be used to edit and generate unlimited OpenAPI definitions. The editor supports editing the global API information (Title, API version, description), add/remove entities, and fields for each OpenAPI entity:

- ✔️ `string`
- ✔️ `timestamp`
- ✔️ `UUID`
- ✔️ `binary`
- ✔️ `boolean`
- ✔️ `number`
- ✔️ `array`
- ✔️ `object` (all entities previously defined)

![OpenAPI Editor - Free, In-Browser tool for editing OpenAPI definitions](https://user-images.githubusercontent.com/51070104/166137630-68fbff6d-24b7-4cf7-9be0-706cb102b61e.gif)

<br />

## 🚀 [OpenAPI Parser](https://github.com/app-generator/devtool-openapi-parser)

Tool to extract relevant information from an OpenAPI descriptor. The information can be used to generate code (helpers, business logic or a database schema). 

- 👉 Free [support](https://appseed.us/support/) via Email and [Discord](https://discord.gg/fZC6hup)
- 👉 More [Developer Tools](https://appseed.us/developer-tools/) - provided by AppSeed

<br />

## 🚀 [DevTool UI Tester](https://github.com/app-generator/devtool-ui-tester) 

This [tool](https://appseed.us/developer-tools/) provides a simple way to ensure compatibilty of a React project accross different Node environments and tools (NPM, Yarn). 

> How it Works

- The target React Projects are added to `repositories.json` file
- Tool Configuration
  - Supported Compilers: `NPM`, `Yarn`
  - Supported environments: Ubuntu, MacOS (All provided by GH Actions)
  - Node Versions: 10.x, 12.x, 14.x, 16.x, 18.x
- Once the changes are subbmitted, the automatized tests are executed via Github actions
- For each build, a screen-shot is taken at the end 

<br />

## 🚀 [Django Dynamic API](https://appseed.us/developer-tools/django-dynamic-api/) 

This tool aims to provide a secure, `production-ready API via DRF` (Django REST Framework) using the developer's minimum amount of code. 

> How it works

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic API over the model
- `Start the app`
- Access the `Dynamic API Service`

> Development Status

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_api` | - |
| ✅ | Models enabled in `core/settings.py` via `DYNAMIC_API` variable | - |
| ✅ | The project exposes automatically a CRUD API over the new model | - |
| ✅ | Path of the service: `/api/products/` | In case the new model is `Products` | 
| ✅ | The API is powered via DRF using best practices | - | 

<br />

## 🚀 [Django Dynamic DataTables](https://appseed.us/developer-tools/django-dynamic-datatables/) 

The tool aims to provide a powerful data table interface using the developer's minimum amount of code. 

> How it works 

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic Data Table service over the model
- `Start` the app
- Access the `Dynamic DataTable` provided on op of the model

> Development Status

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_datatables` | - |
| ✅ | Models enabled in `core/settings.py` via `DYNAMIC_DATATB` variable | - |
| ✅ | The project exposes automaticaly a view powered by `Simple-DataTables` JS Library | - |
| ✅ | Path of the service: `/datatb/products/` | In case the new model is `Products` | - | 
| ✅ | The page exposes the controls: `Items per page`, `Search`, `Server Side Pagination`  | - |

<br />

## 🚀 [Flask Dynamic DataTables](https://github.com/app-generator/devtool-flask-dynamic-datatb) 

The tool aims to provide a powerful data table interface using the developer's minimum amount of code. 

> How it works

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic Data Table service over the model
- `Start` the app
- Access the `Dynamic DataTable` provided on op of the model

> Development status

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_datatables` | - |
| ✅ | Models enabled in `apps/config.py` via `DYNAMIC_DATATB` variable | - |
| ✅ | The project exposes automaticaly a view powered by `Simple-DataTables` JS Library | - |
| ✅ | Path of the service: `/datatb/products/` | In case the new model is `Products` | - | 
| ✅ | The page exposes the controls: `Items per page`, `Search`, `Server Side Pagination`  | - |

<br />

## 🚀 [Flask Dynamic API](https://github.com/app-generator/devtool-flask-dynamic-api)

This tool aims to provide a secure, `production-ready API via Flask-RestX` using the developer's minimum amount of code. 

> Tool Specs & Status

- `Define a new model` in the project (an old one can be also used)
- `Execute the database migration` to create/update the associated tables
- `Update the configuration` to enable the Dynamic API over the model
- `Start the app`
- Access the `Dynamic API Service`

> Development Status 

| Status | Item | info | 
| --- | --- | --- |
| ✅ | New Models Definition in `apps/models` | - |
| ✅ | The app is saved in `apps/dyn_api` | - |
| ✅ | Models enabled in `apps/config.py` via `DYNAMIC_API` variable | - |
| ✅ | The project exposes automatically a CRUD API over the new model | - |
| ✅ | Path of the service: `/api/products/` | In case the new model is `Products` | 
| ✅ | The API is powered via DRF using best practices | - | 

<br />

--- 
[Developers Tools](https://appseed.us/developer-tools/) - Actively supported and versioned by **AppSeed**. 
  

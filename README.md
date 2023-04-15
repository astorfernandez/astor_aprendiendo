# Project Description

## Description
This project is a general purpose container to run shell scripts and python3 scripts.

## To run tests
In `/dk` path, clone or pull repos `DKAnalyticContainer` and `AnalyticContainer`:
``` bash
cd C:\Users\Astor\PycharmProjects\Aprendiendo
run_tests.bat
```
## To run project


## To do list
completar el test de TestTicket:
que consiste en terminar de testear
y armar otro caso de test distinto con otros productos, cantidades, precios y totales
completar  y emrolijar le ReadMe.

Papa:
cuando corra el test imprimir el nombre del test.
herencia

## Changelog

### 1.7.1 - 2023-02-18
* Starting now, echange rate comes from a txt file 

### 1.7.0 - 2020-03-11
* Fixed log output from apt + pip instllations in GPC.

### 1.6.0 - 2020-03-02
* Fixed log items from shell script output in GPC.

### 1.5.0 - 2020-02-17
* Added a check for cases in which vault secrets are being used directly in scripts.
This is not allowed for security reasons. The recommended procedure is to use "parameters" in config.json instead.
Example:
    "keys": {
        "run-script": {
            "script": "test.ipynb",
            "parameters": {
                "param1": "#{vault://param1}"
            }
        }
    }

### 1.4.1 - 2019-12-09
* python libraries included: tableauserverclient==0.9

### 1.4.0 - 2019-11-04
* Added compatibility with Kubernetes Secrets.

### 1.3.1 - 2019-10-08
* Do not remove package lists from Docker image - this breaks user defined apt-get installs.

### 1.3.0 - 2019-10-07
* Added support for Jupyter Notebooks
* Update Dockerfile based on [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
* Alphebetized requirements.txt
* Added markdown to this README

### 1.2.1 - 2019-09-19
* Installed pip dependency xlrd==1.1.0 (needed for pandas to work properly)

### 1.2.0 - 2019-09-12
* Refactor to use python3
* Refactor container name to dk_general_purpose_container (previously was ac_container_template)

### 1.1.3 - 2019-09-12
* python libraries removed: boxsdk[jwt]

### 1.1.2 - 2019-09-11
* include feature to install apt and pip dependencies in config.json. For example:
```json
{
    "apt-dependencies": [
      "curl", "nano"
    ],
    "dependencies": [
      "DKCloudCommand", "boxsdk[jwt]"
    ],
    "keys": {
        ...
    }
}
```

* python libraries included: azure-cli, awscli, requests==2.22.0
* python libraries removed: DKCloudCommand (we will use rest api instead)

### 1.1.1 - 2019-09-11
* python libraries included: google-cloud-bigquery, google-cloud-storage

### 1.1.0 - 2019-09-10
* Add unit tests
* Python and shell script auto detection.
* New Os environment variables feature, through the use of:
```json
    {
        "keys" : {
            "key" : {
                "script" : "env_variables.py",
                "environment": {
                    "env_variable_0": "I am a string",
                    "env_variable_1": 45
                }
           }
        }
    }
```    
* DKCloudCommand package included
* python libraries included: boto, paramiko, pandas, numpy, psycopg2, salesforce

### 1.0.0 - 2019-06-14
* Initial version

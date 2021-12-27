# Anomalous Sound Detection for predictive maintenance of industrial machines

## Table of Contents
1. [Description](#description)
1. [Objectives](#objectives)
	1. [Challenges](#challenges)
	2. [Limitations](#limitations)
	3. [Further developments](#further-developments)
1. [Repo Architecture](#repo-architecture)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Visuals](#visuals)
1. [Timeline](#timeline)
1. [Personal situation](#personal-situation)

## Description
This project is a part of the Becode.org AI Bootcamp programme. The goal is to to create a dashboard with insights about games on Steam platform based on scraped data provided in JSON format. The dashboard should be deployed with Flask, Docker and Heroku.

![steam games](https://static.techspot.com/images2/news/bigimage/2019/09/2019-09-20-image-3.jpg)

## Objectives

- Be able to parse JSON files
- Be able to build and deploy an app using Flask, Docker, and Heroku
- Be able to save json data into an SQL database
- Be able to design a relational SQL database
- Be able to visualize data from a SQL database
- Be able to deploy said database alongside (interactive) visualizations

### Strengths

- Normalised SQL database (See: the ER diagram below)
- Full pipeline:  JSON to SQL, data insights, Flask + HTML, Docker, Heroku.

### Limitations

- Not all data was transformed to a normalised database.

### Further Developments

- Creating more columns in the database.
- Performing more insights.
- Creating interactive dashboard.

## Repo Architecture

- *(1) **/img** - folder contains images, contains an ER diagram of the existing SQL database and a suggested data pipelines (1 - implemented, 2 - work in progress; in a separate repo)
- *(2) **/static** - folder contains images used in the app
- *(3) **/templates** - folder contains .html file used in the app
- *(4) **README.md*** - project documentation
- *(5) **Dockerfile**  - docker file
- *(6) **ETL.ipynb** - Python notebook contains code necessary to extract data from json and load it to SQL database
- *(7) **Insights.ipynb** - Python notebook contains data insights along with graphs which can be saved to .png

## Installation

 *git clone* the repo 


## Usage

## Visuals

![db schema](img/steam_analytics_ER_diagram.png)
![pipeline](img/pipeline.png)
## Timeline

The project took 10 working days.

## Personal situation

[kpranke](https://github.com/kpranke)

I am currently participating in the Becode.org AI Bootcamp to upskill into a career in data science.

**[Back to top](#table-of-contents)**

# Frisco Fusion full game history scraper
A Python scraper deployed to AWS Lambda that pulls down the Frisco Fusion game history and saves it as a `.csv` file.

## .env
A `.env` file with AWS credentials is required.

## Running
* `pipenv shell` to get us going
* Make changes
* Run `zappa update` to deploy changes
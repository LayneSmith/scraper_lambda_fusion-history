These are generic instructions for deploying a lambda scraper. You will need to have appropriate permissions. As of January 2019, this deployment requires Python 3.6.8.

## To build ##
1. Run `pipenv install`
2. Set up a `.env` file with AWS credentials
3. In terminal run `source .env` to marry credentials
4. Write scraper in `scraper_file.py`
5. Update `zappa_setings.json` with project name, description and interval

## Install errors ##
If `pipenv install` doesn't work you may need to manually install your packages. `pipenv install zappa`, `pipenv install requests`, etc...

## To deploy to lambda ##
1. Run `zappa deploy`

## To update with changes ##
1. Run `zappa update`

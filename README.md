# PasteIOCExtractor
Scrape Pastebin API to collect daily pastes and extract IOCs from the pastes											 

## Description
The PasteMonitor tool allows you to perform two main actions (for educational purposes only):

### Download daily new public pastes
Average number of pastes per day: 1000-3000 (filetype: .json)

## Before start

Before starting the tool, make sure to:
- Get a [Pastebin PRO](https://pastebin.com/pro) account
- Enter the IP address of your machine in the "[Your Account & Whitelisted IP](https://pastebin.com/doc_scraping_api)" section
- Activate a mail account that can authorize a third party application (here we use a [Gmail account](https://www.google.com/intl/fr/gmail/about/))
- [Enable 2-step verification](https://myaccount.google.com/u/2/signinoptions/two-step-verification)
- [Generate app password](https://myaccount.google.com/u/2/apppasswords) (for more help, see this [tutorial](https://ljmocic.medium.com/send-an-email-using-python-and-gmail-4ebc980eae9b))

## Prerequisite

```bash
pip install -r requirements.txt
```

## Usage

```bash
python3 pastemonitor.py
```

## Pastebin.com usage
Visit the official Pastebin webpage [Scraping API](https://pastebin.com/doc_scraping_api).

## Contributing
Feel free to clone this project. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)

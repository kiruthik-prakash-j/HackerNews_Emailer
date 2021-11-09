# HackerNews_Emailer

## USAGE

It gets the top 30 news from the [Hacker News](https://news.ycombinator.com/) Website
and sends it to the receiver list using smtp 

## SETUP

### Clone the repo 
```
git clone https://github.com/kiruthik-prakash-j/HackerNews_Emailer.git
```

### Build the packages
```
pip install -r requirements.txt
```

### Set the Environment Variables

Create a .env file and store the following : 
```
EMAIL_ID=<SENDERS_MAIL_ID>
EMAIL_PASSWORD=<SENDERS_PASSWORD>
SMTP_SERVER=<SMTP_SERVER_NAME>
SMTP_PORT=<SMTP_SERVER_PORT>
```

**Note:** For gmail  
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Update the list of receivers

Open the file receivers.py

Remove the email-id and add your required email-id's

### Run the program

```
python main.py
````


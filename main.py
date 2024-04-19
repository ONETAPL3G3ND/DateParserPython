import dateparser

if __name__ == "__main__":
    text = "Вчера в 15:00"

    date = dateparser.parse(text)
    print(date)
import json


with open("KJV.json", mode="r") as bible_text:
    kjv = json.load(bible_text)

bible = [content for content in kjv]

bible_version = "KJV"
bible_books = [books["name"] for books in bible]
# print(bible_books)


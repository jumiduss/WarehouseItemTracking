from stockmanager.models import StockedItem
import csv

with open('inventory_list.csv',newline='') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['item_name','article_number'])
    i=0
    for row in reader:
        print("{}   {}".format(row['item_name'],row['article_number']))
        article_number = row['article_number']
        if article_number=='':
            article_number = '0'
        item = StockedItem(item_name=row['item_name'],article_number=article_number)
        item.save()
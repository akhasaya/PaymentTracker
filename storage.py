# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import requests
# import mysql.connector
# import pandas as pd

class Entity:
    def __init__(self, id, tags):
        self.id = id
        self.tags = tags


class Storage:
    def __init__(self):
        self.array = []

    def add_to_storage(self, id, tags):
        e = Entity(id, tags)
        self.array.append(e)

    def remove_from_storage(self, id):
        for i in range(len(self.array)):
            if self.array[i].id == id:
                self.array.pop(i)
                break

    def count_for_tags(self, search_tags):
        new_shortlist = self.array
        for index, s_tag in enumerate(search_tags):
            shortlist = new_shortlist
            to_add = []
            for k, items in enumerate(shortlist):
                if index < len(items.tags) and items.tags[index] == s_tag:
                    to_add.append(k)

            new_shortlist = []
            for k in to_add:
                new_shortlist.append(shortlist[k])

        return len(new_shortlist)


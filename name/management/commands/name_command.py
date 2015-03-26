#-*-coding:utf8;-*-
from django.core.management.base import BaseCommand
from name.func import fetch_name, query_name, load_dict, cname_name

class Command(BaseCommand):
    help = "product"
    output_transaction = True

    def handle(self, *args, **options):
        func = args[0]
        if func == "name":
            if args[1] == "fetch":
                fetch_name()
                print "ok"
            if args[1] == "query":
                query_name()
                print "ok"
            if args[1] == "cname":
                cname_name()
                print "ok"
        if func == "dict":
            if args[1] == "load":
                load_dict()
                print "ok"

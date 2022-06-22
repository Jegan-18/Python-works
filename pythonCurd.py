import pymongo
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["myDatabase"]



print((myclient.list_database_names()))
dblist =myclient.list_database_names()
if "myDatabase" in dblist:
    print("the db exits")
else:
   print("db is not there")





mycol=mydb["mycollection"]




print(mydb.list_collection_names())
collist=mydb.list_collection_names()
if"mycollection"in collist:
   print("the collection exits")
else:
    print("the collection is not there")



mydict={"name":"mounikaRavinder","address":"Kariminagar"}
x=mycol.insert_one(mydict)



mylist=[
     {"name":"Rav","address":"pdpl"},
      {"name":"swar","address":"mnt"},
       {"name":"Naya","address":"hyd"},
     {"name":"druv","address":"hyd"},
      {"name":"Sri","address":"pune"}

]
x=mycol.insert_many(mylist)
print(x.inserted_ids)



x=mycol.find_one()
myquery={"address":"kariminagar"}
mycol.update_one(myquery,newvalues)
for x in mycol.find():
   print(x)



x=mycol.delete_many({})
print(x.deleted_count,"documents deleted")


mycol=mydb["mycollection"]
mycol.drop()


myresult=mycol.find().limit(3)
for x in myresult:
   print(x)
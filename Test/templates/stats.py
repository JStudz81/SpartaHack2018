from querybuilder.query import Query

from querybuilder.tests.models import User

#from django.contrib.auth.models import User
#from models.

query = Query().from_table(User)
query.select()

query.get_sql()




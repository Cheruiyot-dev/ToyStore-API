from datetime import datetime
from django.utils import timezone
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

# create Toy objects(toy1 and 2)
toy_release_date = timezone.make_aware(datetime.now())
current_time = timezone.now()
toy1 = Toy(name='Snoopy talking action figure',
           description='Snoopy speaks five languages',
           release_date=toy_release_date, toy_category='Action figures',
           was_included_in_home=False,
           created=current_time)
toy1.save()
toy2 = Toy(name='Hawaiian Barbie', description='Barbie loves Hawaii',
           release_date=toy_release_date, toy_category='Dolls',
           was_included_in_home=True,
           created=current_time)
toy3 = Toy(name='Paw Patrol', description='Just paw',
           release_date=toy_release_date, toy_category='Action figures',
           was_included_in_home=True,
           created=current_time)
toy2.save()

# Serializing object 
# The Toy model instances are translated into Python native datatypes.
# Render(serialize) the data in Python native instances into Json.
serializer_for_toy1 = ToySerializer(toy1)  
serializer_for_toy1 = ToySerializer(toy1)  
serializer_for_toy3 = ToySerializer(toy3)  
print(serializer_for_toy1)


toy3_rendered_into_json = JSONRenderer().render(serializer_for_toy3.data)
print(toy3_rendered_into_json)

# Resful web services work with json. Json data is sent over the network. 
"""Django uses stringbytes
Complex data(Python model instances) translated to Python native datatypes/ primitives
Then from primitives to Json data
Serialization
# Process
# 1. Create a model instance and persist in the database
# 2. Serialize the model instance using the created model serializer(convert the complex model instance into Python native datatypes
# 3. Render the Python native datatypes into Json
# 4. Deserialize the objects"""

# Deserializing objects
# 

json_bytes_for_new_toy = io.BytesIO(toy3_rendered_into_json)
data = JSONParser().parse(json_bytes_for_new_toy)

serializer = ToySerializer(data=data)
serializer.is_valid()
serializer.validated_data

json_bytes_for_toy4 = io.BytesIO(toy4_json)
data = 


toy4 = Toy(name='Transformers Optimus Prime', description='Robot in disguise',release_date=toy_release_date, toy_category='Action figures',was_included_in_home=True,created=current_time)

toy5 = Toy(name='Monopoly Classic', description='Buy, sell, trade',release_date=toy_release_date, toy_category='Board Games',was_included_in_home=True,created=current_time)
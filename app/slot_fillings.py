import recognizers_suite as Recognizers
from recognizers_suite import Culture, ModelResult



# Use English for the Recognizers culture
culture = Culture.English

async def extract_slots(input_value):
  """
  extract important info using microsoft recognizer.
   
  """
  slot = {}
  try:
    # extract number
    slot['numbers'] = [result.resolution["values"] for result in Recognizers.recognize_number(input_value, culture)]
  except:
    pass
  try:
    # extract date time
    slot['datetime'] = [result.resolution["values"] for result in Recognizers.recognize_datetime(input_value, culture)]
  except:
    pass
  try:
    # extract currency value
    slot['currency']= [result.resolution["values"] for result in Recognizers.recognize_currency(input_value, culture)]
  except:
    pass
  try:
    # extract ordinal value
    slot['ordinal'] = [result.resolution["values"] for result in Recognizers.recognize_ordinal(input_value, culture)]
  except:
    pass
  try:
    # extract dimension
    slot['dimension'] =[result.resolution["values"] for result in Recognizers.recognize_dimension(input_value, culture)]
  except:
    pass
  # return slot
  return slot 




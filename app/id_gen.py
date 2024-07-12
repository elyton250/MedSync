import random
import string

def generate_id(first_name, last_name, id_number):
  """
  Generates an 8-character ID based on provided names and ID number.
  Returns:
      An 8-character string generated from the provided information.
  """

  # Extract first characters of names and ensure they are letters
  first_initial = first_name[0].upper() if first_name else 'X'
  last_initial = last_name[0].upper() if last_name else 'X'
  first_initial = random.choice(string.ascii_uppercase) if not first_initial.isalpha() else first_initial
  last_initial = random.choice(string.ascii_uppercase) if not last_initial.isalpha() else last_initial

  # Extract and format the last 6 digits of the ID number
  last_digits = str(id_number)[-6:].zfill(6)

  # Combine initials and last digits of ID
  generated_id = first_initial + last_initial + last_digits

  return generated_id


def history_id():
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

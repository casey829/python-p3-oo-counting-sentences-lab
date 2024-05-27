#!/usr/bin/env python3

class MyString:
    def __init__(self, value =''):
      self.value = value

    def get_value(self):
      return self._value
   
    def set_value(self, value):
      if isinstance(value, str):  
          self._value = value
      else:
          print("The value must be a string.")

    value = property(get_value, set_value)

    def is_sentence(self):
       if self.value.endswith('.'):
          return True
       else:
          return False
       
    def is_question(self):
       if self.value.endswith('?'):
          return True
       else:
          return False
       
    def is_exclamation(self):
       if self.value.endswith('!'):
          return True
       else:
          return False
       
    def count_sentences(self):
       replaced_value = self.value.replace('!', '.').replace('?', '.')
       new_sentence = replaced_value.split('.')
       sentences = [s.strip() for s in new_sentence if s.strip()]
       return len(sentences)

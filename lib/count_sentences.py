#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
      self.value = value
    
    @property
    def value(self):
      return self._value
  
    @value.setter
    def value(self, value):
      if  isinstance(value, str):
        self._value = value
      else:
        print("The value must be a string.")
        self._value = ''
    
    def is_sentence(self):
      return self._value.endswith('.')
  
    def is_question(self):
      return self._value.endswith('?')
  
    def is_exclamation(self):
      return self._value.endswith('!')
  
    def count_sentences(self):
      temp_value = self._value.replace('!',".").replace('?',".")
      sentences = [s.strip() for s in temp_value.split('.') if s.strip()]
      return len(sentences)
    

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
string.count_sentences()
  


import random
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def bartender_questions(questions):
  answers = {}
  for key in questions.keys():
    while True:
      answer = raw_input(questions[key] + " ")
      if answer.upper() == 'YES':
        answers[key] = True
        break
      elif answer.upper() == 'NO':
        answers[key] = False
        break
  return answers

def construct_drink(answers):
  selected_ingredients = []
  for key in answers.keys():
      if answers[key]:
        ingredient_list = ingredients[key]
        selected_ingredients.append(random.choice(ingredient_list))
  return selected_ingredients

if __name__ == '__main__':
  answer_list = bartender_questions(questions)
  drink = construct_drink(answer_list)
  print drink

  
  
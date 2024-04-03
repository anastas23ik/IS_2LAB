import json
import copy

class Fact:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Rule:
    def __init__(self, name_rule, question, update_fact, priority, value, appendedFacts):
        self.name = name_rule
        self.question = question
        self.update_fact = update_fact
        self.is_used = False
        self.priority = priority
        self.value = value
        self.own_facts = []
        self.count_condition = 0
        self.appendedFacts = appendedFacts

    def add_condition(self, name, value):
        str = f'{name}, {value}'
        self.own_facts.append(str)

class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def load(self):
        with open('Rule.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        #Проходится по каждому правилу
        for item in data:

            rule = Rule(item.get('rulename'), item.get('question'), item.get('updateFact'), item.get('priority'), item.get('value'), item.get('appendedFacts'))

            dixt = item.get('condition')
            operation = dixt.get('operation')
            facts = dixt.get('facts')

            if facts and facts[0].get('facts') is not None:
                arr = []
                if operation == '&':
                    for fact in facts:
                        nest = fact.get('operation')
                        for lfact in fact.get('facts'):
                            if nest == '&':# Добавляет факты напрямую, если вложенная операция тоже &
                                arr.append(Fact(lfact.get('name'), lfact.get('value')))
                            else:# Создает копию списка, добавляет в него факт и сохраняет в own_facts правила
                                newarr = copy.copy(arr)
                                newarr.append(Fact(lfact.get('name'), lfact.get('value')))
                                rule.own_facts.append(newarr)
                else:  # случай ||
                    for fact in facts:
                        arr = []
                        nest = fact.get('operation')
                        operands = fact.get('facts')
                        if operands is not None:
                            for lfact in operands:

                                if nest == '&':
                                    arr.append(Fact(lfact.get('name'), lfact.get('value')))
                                else:
                                    arr.append(Fact(lfact.get('name'), lfact.get('value')))
                                    rule.own_facts.append(arr)
                                    arr = []

                        if nest == '&':
                            rule.own_facts.append(arr)




            else:# когда факты не вложены
                arr = []
                if operation == "&":
                    for fact in facts:
                        arr.append(Fact(fact.get('name'), fact.get('value')))
                    rule.own_facts.append(arr)
                else:
                    for fact in facts:
                        rule.own_facts.append([Fact(fact.get('name'), fact.get('value'))])


            self.rules.append(rule) # Добавляет правило в список всех правил


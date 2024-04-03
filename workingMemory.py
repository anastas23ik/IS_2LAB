from knowledgeBase import Fact
class WorkingMemory:
    def __init__(self):
        self.current_facts = []
        self.current_facts_names = []

    # добавляем новый факт в рабочую память
    def add_fact(self, name, value):
        fact = Fact(name, value)
        self.current_facts.append(fact)
        self.current_facts_names.append(name)
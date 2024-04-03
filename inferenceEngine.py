from explanationComponent import ExplanationComponent
from knowledgeBase import KnowledgeBase
from workingMemory import WorkingMemory

class InferenceEngine:
    def __init__(self):
        self.knowledgeBase = KnowledgeBase()
        self.workingMemory = WorkingMemory()
        self.explanationComponent = ExplanationComponent()
        self.knowledgeBase.load()
        self.current_rule = None
        self.answers = None
        self.question = None
        self.get_answer_question()
        self.isAnswer = False

    def get_answer_question(self):
        current_rules = self.get_current_rules()#Получение списка текущих подходящих правил
        print("количество текущих правил из базы знаний(get)",len(current_rules))
        current_rules.sort(key=lambda c: c.priority, reverse=True)
        current_rules.sort(key=lambda c: c.count_condition)
        print("список доступных правил:")
        for rule in current_rules:
            print(rule.name)
        if len(current_rules) == 0:
            self.isAnswer = True
            self.question = self.workingMemory.current_facts[-1].value
            return
        self.current_rule = current_rules[0]#берем первое правило из списка правил
        self.knowledgeBase.rules[self.knowledgeBase.rules.index(self.current_rule)].is_used = True
        print("len current.value", len(self.current_rule.value))
        if len(self.current_rule.value) != 0:
            self.question = self.current_rule.question
            print("question",self.question)
            self.answers = self.current_rule.value
            print("answers",self.answers)
        else:
            print("если нет вариантов ответа")
            if self.current_rule.update_fact.get('name') in self.workingMemory.current_facts_names:
                self.isAnswer = True
                self.question = self.workingMemory.current_facts[-1].value
                return
            print("добавление факта( имя)",self.current_rule.update_fact.get('name'))
            print("добавление факта( значение)",self.current_rule.update_fact.get('value') )
            self.workingMemory.add_fact(self.current_rule.update_fact.get('name'), self.current_rule.update_fact.get('value'))
            self.get_answer_question()


    def get_current_rules(self):
        current_rules = []
        if len(self.workingMemory.current_facts) == 0:
            print("количество фактов в рабочей памяти",len(self.workingMemory.current_facts))
            current_rules = self.knowledgeBase.rules
            print("количество правил в  базе знаний",len(current_rules))
            return current_rules


        for rule in self.knowledgeBase.rules:
            if not rule.is_used:
                flag = []
                for condition in rule.own_facts:
                    arr = True
                    for fact in condition:
                        for cur_fact in self.workingMemory.current_facts:
                            if fact.name == cur_fact.name:
                                if fact.value != cur_fact.value:
                                    arr = False
                                    break
                    if arr:
                        flag.append(1)
                    else:
                        flag.append(0)

                if sum(flag) > 0:
                    rule.count_condition = sum(flag)
                    current_rules.append(rule)
        return current_rules

    def set_user_answer(self, value):
        self.workingMemory.add_fact(self.current_rule.update_fact.get('name'), value)
        if (self.current_rule.appendedFacts):
            for appendedFact in self.current_rule.appendedFacts:
                cond_value = appendedFact.get('conditionValue')
                if (cond_value == value):
                    self.workingMemory.add_fact(appendedFact.get('fact').get('name'), appendedFact.get('fact').get('value'))

    def get_logs(self):
        return self.explanationComponent.get_logs(self.workingMemory.current_facts)



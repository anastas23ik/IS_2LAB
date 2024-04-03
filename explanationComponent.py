class ExplanationComponent:
    def get_logs(self, facts):
        listFacts = []
        for fact in facts:
            entry = '{0} : {1}'.format(fact.name, fact.value)
            listFacts.append(entry)
        return '\n'.join(listFacts)
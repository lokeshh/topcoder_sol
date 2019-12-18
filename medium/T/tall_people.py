class TallPeople:
    def transpose(self, people):
        new_people = []
        for i in range(len(people[0])):
            col = []
            for j in range(len(people)):
                col.append(people[j][i])
            new_people.append(col)
        return new_people

    def getPeople(self, people):
        for i in range(len(people)):
            people[i] = list(map(int, (people[i]).split(' ')))
        return max(map(min, people)), min(map(max, self.transpose(people)))


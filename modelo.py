class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @property
    def likes(self):
        return self._likes

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def thumbs_up(self):
        self._likes += 1


class Movie(Program):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    def __str__(self):
        return f'{self._name} - {self.year} - {self.length} min - {self._likes} likes'


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} seasons - {self._likes} likes'


class Playlist:
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __getitem__(self, item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)

    @property
    def listing(self):
        return self._programs


avengers = Movie('avengers: infinity war', 2018, 160)
avengers.thumbs_up()
atlanta = Series('atlanta', 2018, 2)
scary = Movie('Scary Movie', 1999, 100)
demolidor = Series('Demolidor', 2016, 2)


scary.thumbs_up()
scary.thumbs_up()
demolidor.thumbs_up()
atlanta.thumbs_up()
atlanta.thumbs_up()
atlanta.thumbs_up()
atlanta.thumbs_up()

movies_and_series = [avengers, atlanta, scary]
weekend_playlist = Playlist('weekend', movies_and_series)

print(f'Playlist size: {len(weekend_playlist)}')

for program in weekend_playlist:
    print(program)

print(f'Is in? {demolidor in weekend_playlist}')

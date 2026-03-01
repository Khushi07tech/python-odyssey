class Entry:
    total_entries = 0
    def __init__(self, entry_date, entry_day):
        self.entry_date = entry_date
        self.entry_day = entry_day
    def describe (self):
        print (f"Today is {self.entry_date} {self.entry_day}.")

class Mood_entry(Entry):
    def __init__(self, entry_date, entry_day, mood, energy_level):
        self.mood = mood
        self.energy_level = energy_level
        Entry.__init__ (self, entry_date, entry_day)
        print("Select a mood; Happy | Normal | Sad")
    def describe(self):
        super().describe()
        print (f"Your mood is {self.mood} and the energy level on the count of 10 is {self.energy_level}")

class Journal_entry(Entry):
    def __init__(self, entry_date, entry_day, text):
        self.text = text
        Entry.__init__(self, entry_date, entry_day)
    def describe(self):
        super().describe()
        print (self.text[0:10])

class Mood_journal(Mood_entry, Journal_entry):
    def __init__(self, entry_date, entry_day, mood, energy_level, text):
        Mood_entry.__init__ (self, entry_date, entry_day, mood, energy_level)
        Journal_entry.__init__(self, entry_date, entry_day, text)
        Entry.total_entries += 1
    def describe(self):
        Entry.describe(self)

mood1 = Mood_entry(entry_date= "Jan 3",
                   entry_day= "Saturday",
                   mood= "Happy",
                   energy_level= 7)
journal1 = Journal_entry(entry_date= "Jan 3",
                         entry_day= "Saturday",
                         text= "Today I suffered the DOMS pain in my lower body, btw the daughter of our neighbours is going to marry, her husband is working in UAE so she's gotta live abroad!")
mood_journal1 = Mood_journal(entry_date= "Jan 3",
                             entry_day= "Saturday",
                             mood= "Happy",
                             energy_level= 7,
                             text= "Today I suffered the DOMS pain in my lower body, btw the daughter of our neighbours is going to marry, her husband is working in UAE so she's gotta live abroad!")

print(f"Entry date: {mood1.entry_date}")
print(f"Entry day: {mood1.entry_day}")
print(f"Entry mood: {mood1.mood}")
print(f"Energy level: {mood1.energy_level}")
print(f"Journal Text: {journal1.text}")
print (f"Total Entries:{Entry.total_entries}")
#################################
# Instruction
# This quiz is a simplified version of 2020 presidential election. Write a definition for a class named Candidate with the following methods:

# An __init__ method that initializes name, winning_states and number of votes.
# A __str__ method that returns a string representation of this candidate, including name and winning state(s).
# A method named win_state that takes a string of state abbreviation, adds it to winning_states and updates votes.
# A special method that overloads the operator > to compare votes of two candidates.
# #################################

#################################
# Expected Results
# Before voting:
# Donald Trump has won TX, FL.
# Joe Biden has won CA, MA.
# Kanye West has not won any state yet.
# Does Trump win?
# True

# After election day:
# Donald Trump has won TX, FL, OH, IA.
# Joe Biden has won CA, MA, PA, AZ.
# Does Trump win?
# False
#######################################


ELECTORAL_VOTES = {'AZ': 11, 'CA': 55, 'FL': 29, 'IA': 6, 'MA': 11, 'OH': 18, 'PA': 20, 'TX': 38}


class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s) (even before voting).
        votes: integer, representing number of votes
        """
        if winning_states is None: 
            winning_states=[]
        self.winning_states = winning_states
        self.name = name 
        self.win_state = winning_states
        self.votes = votes

    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        pass

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        pass



###########################################
# Please DO NOT change code in main method!
###########################################
def main():
    trump = Candidate('Donald Trump', winning_states=['TX', 'FL'])
    biden = Candidate('Joe Biden', winning_states=['CA', 'MA'])
    west = Candidate('Kanye West')
    print('Before voting:')
    print(trump)
    print(biden)
    print(west)
    print('Does Trump win?')
    print(trump > biden)
    print()
    print('After election day:')
    trump.win_state('OH')
    trump.win_state('IA')
    biden.win_state('PA')
    biden.win_state('AZ')
    print(trump)
    print(biden)
    print('Does Trump win?')
    print(trump > biden)


if __name__ == '__main__':
    main()
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

ELECTORAL_VOTES = {
    "AZ": 11,
    "CA": 55,
    "FL": 29,
    "IA": 6,
    "MA": 11,
    "OH": 18,
    "PA": 20,
    "TX": 38,
}


class Candidate:
    """The presidential candidate"""

    # An __init__ method that initializes name, winning_states and number of votes.
    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s) (even before voting).
        votes: integer, representing number of votes
        """
        self.name = name  #  candidate name

        if winning_states is None:  #  when candidate has no win, return empty list
            self.winning_states = []
        else:
            self.winning_states = winning_states  #  state candidate is winning

        total_vote = []
        for i in self.winning_states:
            total_vote.append(ELECTORAL_VOTES[i])
        self.votes = sum(
            total_vote
        )  # total number of electoral votes in all state of a candidate

    # A __str__ method that returns a string representation of this candidate, including name and winning state(s).
    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        if len(self.winning_states) > 0:
            return f"{self.name} has won {', '.join(self.winning_states)}."  #  return candidate and their winning states
        else:
            return f"{self.name} has not won any state yet."  # return when candidate has no winning state

    # A method named win_state that takes a string of state abbreviation, adds it to winning_states and updates votes.
    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(
            state
        )  #  add state to the winning state list of a candidate
        self.votes += ELECTORAL_VOTES[state]  #  update vote counts

    # A special method that overloads the operator > to compare votes of two candidates.
    def __gt__(self, other):  #  __gt__ is a method for implementation of >
        """
        Returns True if 'self' candidate has more electoral votes than the 'other'candidate
        output: boolean
        """
        return self.votes > other.votes  # return True when arguement is correct


###########################################
# Please DO NOT change code in main method!
###########################################
def main():
    trump = Candidate("Donald Trump", winning_states=["TX", "FL"])
    biden = Candidate("Joe Biden", winning_states=["CA", "MA"])
    west = Candidate("Kanye West")
    print("Before voting:")
    print(trump)
    print(biden)
    print(west)
    print("Does Trump win?")
    print(trump > biden)
    print()
    print("After election day:")
    trump.win_state("OH")
    trump.win_state("IA")
    biden.win_state("PA")
    biden.win_state("AZ")
    print(trump)
    print(biden)
    print("Does Trump win?")
    print(trump > biden)


if __name__ == "__main__":
    main()

import random


class Doctor:
    def __init__(self, greeting_message: str, signoff_message: str, hedges: list, qualifiers: list, replacements: dict):
        self.greeting_message = greeting_message
        self.signoff_mesSsage = signoff_message
        self.history = []
        self.hedges = hedges
        self.qualifiers = qualifiers
        self.replacements = replacements

    def greeting(self):
        return self.greeting_message

    def farewell(self):
        return self.signoff_message

    def changePerson(self, sentence):
        """Replaces first person pronouns with second person pronouns."""
        words = sentence.split()
        replyWords = []

        for word in words:
            replyWords.append(self.replacements.get(word, word))

        return " ".join(replyWords)

    def reply(self, sentence):
        """Implements three different reply strategies."""
        probability = random.randint(1, 5)

        if probability in (1, 2):
            # Just hedge
            answer = random.choice(self.hedges)
        elif probability == 3 and len(self.history) > 3:
            # Go back to an earlier topic
            answer = "Earlier you said that " + \
                     self.changePerson(random.choice(self.history))
        else:
            # Transform the current input
            answer = random.choice(self.qualifiers) + self.changePerson(sentence)

        # Always add the current sentence to the history list
        self.history.append(sentence)

        return answer


main.py

from doctor import Doctor


def main():
    hedges = ("Please tell me more.", "Many of my patients tell me the same thing.", "Please continue.")

    qualifiers = ("Why do you say that ", "You seem to think that ", "Can you explain why ")

    replacements = {"I": "you", "me": "you", "my": "your", "we": "you", "us": "you", "mine": "yours", "you": "I",
                    "your": "my", "yours": "mine"}

    greeting_message = "Good morning, I hope you are well today. \nWhat can I do for you?"

    signoff_message = "Have a nice day!"

    doctor = Doctor(greeting_message, signoff_message, hedges, qualifiers, replacements)

    print(doctor.greeting())

    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print(doctor.farewell())
            break

        print(doctor.reply(sentence))


# The entry point for program execution
if name == "__main__":
    main()
    answer

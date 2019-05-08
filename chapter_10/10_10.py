# 10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
# and find a few texts you’d like to analyze. Download the text files
# for these works, or copy the raw text from your browser into a text
# file on your computer. You can use the count() method to find out
# how many times a word or phrase appears in a string. For example,
# the following code counts the number of times 'row' appears in a stringself.

# Notice that converting the string to lowercase using lower() catches
# all appearances of the word you’re looking for, regardless of how it’s
# formatted. Write a program that reads the files you found at Project
# Gutenberg and determines how many times the word 'the' appears in each text.

filenames = ['The_North_American_Indian.txt',
    'Its_Cause_and_Treatment_by_Clarence_Darrow.txt']

print("<<<Enter 'q' to quit in any time>>>")
for filename in filenames:
    with open(filename) as file_object:
        contents = file_object.read()
        word = input(f"Enter the word you want to count in the file: \
{filename}\n: ")

        if word == 'q':
            break

        count = contents.lower().count(word)
        print(f"The word '{str(word)}' is used {str(count)} times \
in the file: '{filename}'.")
        print("---")

# Tilden Winston (tw8rt) Alec Ross(asr3bj) Writes debug info, records high scores
# referenced: https://stackoverflow.com/questions/37799078/how-to-append-data-to-text-file-in-python-2-7-11
# https://wiki.python.org/moin/HowTo/Sorting

import time

ordering = 0

def highscores(newscore):
    writescore(newscore)
    topten = returnscores()


def writescore(newscore):
    outfile = open("scores.txt", "a+")
    outfile.write(str(newscore) + "\n")
    outfile.close()

    # except:
    #     print("this")
    #     print(newscore)
    #
    #     outfile = open("scores.txt", "w")
    #     # outfile.write(str(newscore))
    #     outfile.close()


# def writescore(newscore):
#     if os.path.exists("scores.txt"):
#         with open("scores.txt", "r") as source_file_object:
#             source_file_contains = source_file_object.readlines()  # return all lines of data as items of a list
#             source_file_contains = source_file_contains.sort()
#             print(source_file_contains)
#         # source.txt is closed
#
#         os.remove("scores.txt")
#         os.rename("temp.txt", "scores.txt")  # rename the temp file NAME (not file object) with original NAME
#         with open("scores.txt", "r") as source_file_object:
#             print(
#                 "C and D are not printed to temp.txt, when source.txt is deleted and temp.txt renamed, C and D are gone")
#             print(source_file_object.read())
#             # source.txt is closed
#
#     else:
#         # Create file
#         print(newscore)
#
#         outfile = open("scores.txt", "w")
#
#         # write some data.  Each line of data written must terminate with a \n (newline) character.
#         # Python needs this newline character for the file object methods readline() and readlines() to work.
#         outfile.write(str(newscore))
#
#         # Print to the file with an additional argument to the print function. \n automatically attached.
#
#         # The next print places multiple items on a line. flush=True ensures immediate (rather than buffered) write to file.
#         # Using flush to ensure immediate writes will degrade performance, generally buffered writes are preferred
#         # print("Peter", "Piper", "Phoebe", file=outfile, flush=True)
#         outfile.close()

def returnscores():
    infile = open("scores.txt", "r")
    scores_in_file = infile.read().split()
    print(scores_in_file)
    infile.close()
    empty = []
    for each in scores_in_file:
        #print(type(each))
        empty.append(int(each))
    empty.sort(reverse=True)
    # print(empty)
    topten = []
    x = 0
    while x < 10 and x < len(empty):
        topten.append(empty[x])
        x = x + 1

    print(topten)
    return topten



def errorlog(location, note="none"):
    ordering = time.time()
    outfile = open("errorlog.txt", "a+")
    outfile.write(str(ordering) + " " + str(location) + " " + str(note) + "\n")
    outfile.close()

# def plusone(number=0):
#     return number+1
# errorlog.ordering = 0
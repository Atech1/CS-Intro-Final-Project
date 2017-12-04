# Tilden Winston (tw8rt) Alec Ross(asr3bj) Writes debug info, records high scores
# Not functional yet. Based on code from class demonstration

def highscores(newscore):
    writescore(newscore)
    returnscores()


def writescore(newscore):
    if os.path.exists("scores.txt"):
        with open("scores.txt", "r") as source_file_object:
            source_file_contains = source_file_object.readlines()  # return all lines of data as items of a list
            source_file_contains = source_file_contains.sort()
            print("file object.readlines() returns THE LIST of data on each line, each line terminated with \\n:")
            print(source_file_contains)
        # source.txt is closed

        os.remove("source.txt")
        os.rename("temp.txt", "source.txt")  # rename the temp file NAME (not file object) with original NAME
        with open("source.txt", "r") as source_file_object:
            print(
                "C and D are not printed to temp.txt, when source.txt is deleted and temp.txt renamed, C and D are gone")
            print(source_file_object.read())
            # source.txt is closed

    else:
        # Create file
        print(newscore)

        outfile = open(scores.txt, "w")

        # write some data.  Each line of data written must terminate with a \n (newline) character.
        # Python needs this newline character for the file object methods readline() and readlines() to work.
        outfile.write(newscore)

        # Print to the file with an additional argument to the print function. \n automatically attached.

        # The next print places multiple items on a line. flush=True ensures immediate (rather than buffered) write to file.
        # Using flush to ensure immediate writes will degrade performance, generally buffered writes are preferred
        # print("Peter", "Piper", "Phoebe", file=outfile, flush=True)
        outfile.close()

def returnscores():

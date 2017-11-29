# Tilden Winston (tw8rt) Alec Ross(asr3bj) Writes debug info, records high scores
# Not functional yet. Based on code from class demonstration

if os.path.exists("scores.txt"):
    with open("scores.txt", "r") as source_file_object:
        source_file_contains = source_file_object.readlines()   # return all lines of data as items of a list
        print("file object.readlines() returns THE LIST of data on each line, each line terminated with \\n:")
        print(source_file_contains)
    # source.txt is closed

    with open("scores.txt", "r") as source_file_object:
        source_file_contains = source_file_object.read()        # return all lines of data as a string
        print("file object.read() returns all \\n terminated lines of data in the file:")
        print(source_file_contains)
    # source.txt is closed

    with open("source.txt", "r") as source_file_object:
        with open("temp.txt", "w") as temp_file_object:
            for line in source_file_object:         # for in automatically detects end of file and terminates for loop
                key, value = line.split()           # each line has two strings, separated by a space
                if not(key == "67" or key == "68"):  # skipping keys 67 and 68 and not printing to temp deletes them
                    print(key, value, file=temp_file_object, flush=True)
        # temp.txt is closed
    # source.txt is closed

    # files must be closed before doing the behind the scenes magic stuff
    # remove (delete) the source file first.  Note: use the file name here, not the file object (handle)
    os.remove("source.txt")
    os.rename("temp.txt", "source.txt")             # rename the temp file NAME (not file object) with original NAME
    with open("source.txt", "r") as source_file_object:
        print("C and D are not printed to temp.txt, when source.txt is deleted and temp.txt renamed, C and D are gone")
        print(source_file_object.read())
    # source.txt is closed

else:
    # first time program runs, execution is here because the os.path.exists is False
    # with open guarantees file is closed if an exception is thrown.  file opened for write access.
    with open("source.txt", "w") as source_file_object:
        for key, value in a_dict.items():
            # must convert the integer data to string before writing it to disk
            print(str(key), value, file=source_file_object, flush=True)

    print("Open PyCharm's explorer window and open source.txt.  Now source.txt exists so run the program again.")

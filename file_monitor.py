import hashlib      


import datetime      


import json


# Print welcome message


print("==================================================")


print("            FILE HASH MONITOR            ")


print("==================================================")


# Declare variables


keepLooping = True


data = []


LOG_FILE = "file_hash_log.json"  # Path to the JSON log file


# Begin main loop


while keepLooping:


    # Ask the user for the file path


    filePath = input('Enter the full path of the file to check (example: C:/test.txt) or [e] to exit: ').strip()


    # Check for exit press


    if filePath.lower() == "e":


        print("Goodbye!")


        break  # Exit the loop to stop the program


    try:


        # Try to calculate the SHA256 value of the file by first opening it in bytes mode


        f = open(filePath, "rb")


        # Try to calculate SHA hash


        fileData = f.read()


        f.close()


        sha256Hash = hashlib.sha256(fileData).hexdigest()


    except Exception:


        print("Invalid input or cannot open file. Please try again.")


        continue  # Prompt again if there's an error


    # Load existing log entries from the JSON file


    try:


        log_f = open(LOG_FILE, 'r')


        data = json.load(log_f)


        log_f.close()


    except Exception as e:


        # Only warn if the error is not "No such file or directory"


        if  "No such file or directory" not in str(e):


            print(f"Warning: could not read log file: {e}")


        data = []  # Start with an empty list if the file doesn't exist or is invalid


    # Find previous entries for the same file path


    prev_entries = []


    for entry in data:


        if entry.get('file') == filePath:


            prev_entries.append(entry)  


    # If the file was seen before, compare the new hash with the last one


    if prev_entries:


        last_hash = prev_entries[-1].get('hash')


        if sha256Hash != last_hash:


            print("WARNING: This file's content has changed since the last recorded hash.")


    # Create a new log entry and append it


    timeStamp = str(datetime.datetime.now())


    # Create a new entry with the current timestamp, file path, and hash


    newEntry = {'time_stamp': timeStamp, 'file': filePath, 'hash': sha256Hash}


    data.append(newEntry)


    # Attempt to save the updated log back to the JSON file


    try:


        log_f = open(LOG_FILE, 'w')


        json.dump(data, log_f, indent=2)


        log_f.close()


    except Exception as e:


        print(f"Warning: could not save log file: {e}")


    # Display the new hash entry


    print("\n==================================================")


    print(f" New hash recorded for: {filePath}")


    print(f" Time: {timeStamp}")


    print(f" SHA-256: {sha256Hash}")


    print("==================================================")


    # Print all previous hashes for this file for user comparison


    if prev_entries:


        print("Previous hashes for this file:")


        for entry in prev_entries:


            ts = entry.get('time_stamp')


            h = entry.get('hash')


            print(f" {ts}  |  {h}")


    else:


        print("No previous hashes found for this file.")


    print()



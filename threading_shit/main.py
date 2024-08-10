import json, pickle
import shutil
import threading, random, os

numbers = []


def fill_list(value):
    global numbers
    numbers = []
    for i in range(value):
        numbers.append(random.randint(0, 10))


def summary():
    global numbers
    print(sum(numbers))


def average():
    global numbers
    print(sum(numbers) / len(numbers))

def get_path_file():
    while True:
        path = input("enter a path to existing file: ")
        if os.path.exists(path):
            return path
        print("path deosnt exist")

def copy_directory(original: str, new_path: str):
    original_name, format_of_file = os.path.basename(original).rsplit('.', 1)
    i = ""

    directoris = new_path.split('/')  #making sure file path exist
    check_dir: str = ""
    for new_dir in directoris:
        if not os.path.exists(f"{check_dir}{new_dir}"):
            os.mkdir(f"{check_dir}{new_dir}")
        check_dir += f"{new_dir}/"

    while True:  #creating unique file name
        final_path = f"{new_path}/copy_of_{original_name}{i}.{format_of_file}"
        if not os.path.exists(final_path):
            break
        try:
            i += 1
        except:
            i = 1

    if format_of_file == "json":  #if file format is json
        with open(original, 'r') as file:
            new_file = open(final_path, 'w')
            json.dump(json.load(file), new_file)

    elif format_of_file == "pickle":  #of file format is pickle
        import pickle
        with open(original, 'rb') as file:
            new_file = open(final_path, 'wb')
            pickle.dump(pickle.load(file), new_file)

    else:  #for everithing else
        with open(original, 'r') as original_file:
            new_file = open(final_path, 'w')
            for line in original_file.readlines():
                new_file.write(line)

    """
    shutil.copyfile(original, final_path)
    """


def main():
    global numbers
    thread1 = threading.Thread(target=fill_list, args=(10,))
    thread2 = threading.Thread(target=summary)
    thread3 = threading.Thread(target=average)
    thread1.start()
    thread1.join()
    print(f"Thread 1: {thread1.is_alive()}")
    print(f"list s full numbers: {numbers}\nstarting thread 2 and thread 3")
    thread2.start()
    thread3.start()  #konec ukolu1

    with open("original.txt", 'a') as f:
        for i in numbers:
            f.write(f"{str(i)}")
        f.write('\n')
    thread1 = threading.Thread(target=copy_directory, args=(get_path_file(),
                                                            input("enter a path to directory where you want a "
                                                                  "copy: ")))


copy_directory("original.txt", "finish/another/another/another/another/another")

main()

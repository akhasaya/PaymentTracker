from storage import Storage

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    filename = "input.txt"
    with open(filename, "r") as fp:
        lines = fp.readlines()

    storage = Storage()
    for line in lines:
        print(line)
        index = 0
        function = []
        while index < len(line) and line[index].isalnum():
            function.append(line[index])
            index += 1

        function = "".join(function)

        if function == "startTracking":
            index += 1
            id = []
            while index < len(line) and line[index].isdigit():
                id += line[index]
                index += 1
            id = "".join(id)
            id = int(id)

            index += 3
            tags = []
            while index < len(line) and line[index] != "]":
                if line[index] != "\"" and line[index] != " ":
                    tags.append(line[index])
                index += 1

            tags = "".join(tags)
            tags = tags.split(",")
            storage.add_to_storage(id, tags)

        elif function == "getCounts":
            index += 3
            tags = []
            while index < len(line) and line[index] != "]":
                if line[index] != "\"" and line[index] != " ":
                    tags.append(line[index])
                index += 1
            tags = "".join(tags)
            tags = tags.split(",")
            result = storage.count_for_tags(tags)
            print(result)

        elif function == "stopTracking":
            index += 1
            id = []
            while index < len(line) and line[index].isdigit():
                id += line[index]
                index += 1
            id = "".join(id)
            id = int(id)

            storage.remove_from_storage(id)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

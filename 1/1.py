def solution(table, languages, preference):

    score = {"SI": 0, "CONTENTS": 0, "HARDWARE": 0, "PORTAL": 0, "GAME": 0}
    user_info = {}
    for i in range(len(languages)):
        user_info[languages[i]] = preference[i]

    for t in table:
        job, five, four, three, two, one = t.split()
        table_dict = {five: 5, four: 4, three: 3, two: 2, one: 1}

        for lang in user_info.keys():
            if lang in table_dict.keys():
                score[job] += table_dict[lang] * user_info[lang]

    answer = sorted(score.items(), key=lambda x: (-x[1], x[0]))
    return answer[0][0]




if __name__ == "__main__":
    a = solution([
            "SI JAVA JAVASCRIPT SQL PYTHON C#",
          "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
          "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
          "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
          "GAME C++ C# JAVASCRIPT C JAVA"],
                    ["PYTHON", "C++", "SQL"], [7, 5, 5])
    print(a == "HARDWARE", a)

    a = solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"],
        ["JAVA", "JAVASCRIPT"], [7, 5])
    print(a == "PORTAL", a)
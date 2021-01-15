def solution(s):
    answer = []
    split_numbers = s[2:-2].split("},{")
    split_numbers.sort(key=lambda x: len(x))
    for split_number in split_numbers:
        numbers = split_number.split(",")
        for n in numbers:
            if int(n) not in answer:
                answer.append(int(n))
    return answer
def get_distance(now, destination):
    return abs(now[0] - destination[0]) + abs(now[1] - destination[1])


def solution(numbers, hand):
    answer = ''
    number_directions = {
         1: (0, 0), 2: (0, 1), 3: (0, 2),
         4: (1, 0), 5: (1, 1), 6: (1, 2),
         7: (2, 0), 8: (2, 1), 9: (2, 2),
         '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_no = [1, 4, 7]
    right_no = [3, 6, 9]

    left, right = '*', '#'
    for i in numbers:
        if i in left_no:
            answer += 'L'
            left = i
        elif i in right_no:
            answer += 'R'
            right = i
        else:
            left_distance = get_distance(number_directions[left], number_directions[i])
            right_distance = get_distance(number_directions[right], number_directions[i])
            if left_distance > right_distance:
                answer += 'R'
                right = i
            elif left_distance < right_distance:
                answer += 'L'
                left = i
            else:
                if hand == "left":
                    answer += 'L'
                    left = i
                else:
                    answer += 'R'
                    right = i

    return answer
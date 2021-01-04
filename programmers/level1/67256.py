def get_distance(hand_position, pad_position):
    return abs(hand_position[0] - pad_position[0]) + abs(hand_position[1] - pad_position[1])


def solution(numbers, hand):
    answer = ''

    pad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)
    }

    left_hand = [1,4,7]
    right_hand = [3,6,9]
    left, right = pad['*'], pad['#']
    for n in numbers:

        if n in left_hand:
            answer += 'L'
            left = pad[n]
        elif n in right_hand:
            answer += 'R'
            right = pad[n]
        else:
            left_distance = get_distance(left, pad[n])
            right_distance = get_distance(right, pad[n])

            if left_distance < right_distance:
                answer += 'L'
                left = pad[n]
            elif left_distance == right_distance:
                if hand == "left":
                    answer += 'L'
                    left = pad[n]
                elif hand == "right":
                    answer += 'R'
                    right = pad[n]
            elif left_distance > right_distance:
                answer += 'R'
                right = pad[n]

    return answer

























##################################################################################
a = solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],	"right")
print(a == "LRLLLRLLRRL", a)
b = solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left")
print(b == "LRLLRRLLLRR", b)
c = solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")
print(c == "LLRLLRLLRL", c)
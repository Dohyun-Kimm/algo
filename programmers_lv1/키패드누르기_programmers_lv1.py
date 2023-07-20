def solution(numbers, hand):
    answer = ''
    mutual_board = [2, 5, 8, 0]
    left_hand, right_hand = [3, 0], [3, 2]
    key_board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    keyboard_coor = {}
    for row in range(len(key_board)):
        for col in range(len(key_board[0])):
            keyboard_coor[key_board[row][col]] = [row, col]
    # print(keyboard_coor)
    for number in numbers:
        if number in mutual_board:
            if answer == '':
                answer += hand[0].upper()
                if hand == 'left':
                    left_hand = keyboard_coor[number]
                elif hand == 'right':
                    right_hand = keyboard_coor[number]
            else:
                left = abs(keyboard_coor[number][0] - left_hand[0]) + abs(keyboard_coor[number][1] - left_hand[1])
                right = abs(keyboard_coor[number][0] - right_hand[0]) + abs(keyboard_coor[number][1] - right_hand[1])
                if left < right:
                    answer += 'L'
                    left_hand = keyboard_coor[number]
                elif right < left:
                    answer += 'R'
                    right_hand = keyboard_coor[number]
                else:
                    answer += hand[0].upper()
                    if hand == 'left':
                        left_hand = keyboard_coor[number]
                    elif hand == 'right':
                        right_hand = keyboard_coor[number]
        elif number % 3 == 1:
            left_hand = keyboard_coor[number]
            answer += 'L'
        else:
            right_hand = keyboard_coor[number]
            answer += 'R'

    return answer
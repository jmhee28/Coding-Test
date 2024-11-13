op_start_num = 0
op_end_num = 0

def solution(video_len, pos, op_start, op_end, commands):
    global op_start_num, op_end_num
    answer = ''
    video_len_num = timeToSec(video_len)
    pos_num = timeToSec(pos)
    op_start_num = timeToSec(op_start)
    op_end_num = timeToSec(op_end)
    
    for command in commands:
        if op_start_num <= pos_num <= op_end_num: # 오프닝 건너뛰기
            pos_num = op_end_num
        if command == "prev":
            pos_num -= 10
            if pos_num < 0:
                pos_num = 0
        else:
            pos_num += 10
            if pos_num > video_len_num:
                pos_num = video_len_num
    if op_start_num <= pos_num <= op_end_num: # 오프닝 건너뛰기
            pos_num = op_end_num
    min = pos_num // 60
    sec = pos_num % 60
    answer = '{0:02d}'.format(min) + ':' + '{0:02d}'.format(sec)
    return answer

def timeToSec(timeStr):
    timeStrParsed = timeStr.split(':')
    min = int(timeStrParsed[0])
    sec = int(timeStrParsed[1])
    return (min * 60) + sec


    
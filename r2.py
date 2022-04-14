

def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    new = []
    person = None # person這個值先宣告"無"
    allen_word_count = 0
    viki_word_count = 0
    for line in lines:  # 一行一行讀取對話紀錄
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            print(s[2:])
        elif name == 'Viki':
            print(s[2:])
        
        # print(s)

    return new


def write_file(filename, lines):
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    lines = read_file('LINE-Viki.txt')
    lines = convert(lines)
   # write_file('output.txt', lines)

main()  # main function進入點，呼叫使用上方功能
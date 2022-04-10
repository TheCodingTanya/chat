
def read_file(filename):
    lines = []
    with open(filename, 'r', encoding = 'utf-8-sig') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None # person這個值先宣告"無"
    for line in lines:  # 一行一行讀取對話紀錄
        if line == 'Allen':
            person = 'Allen' # 把現在說話的人存起來
            continue  # 跳到下一迴
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:  # 如果person有值的話
            new.append(person + ': '+ line) # 人名+: +對話紀錄
    return new


def write_file(filename, lines):
	with open(filename, 'w') as f:
	    for line in lines:
	    	f.write(line + '\n')


def main():
    lines = read_file('input.txt')
    lines = convert(lines)
    write_file('output.txt', lines)

main()  # main function進入點，呼叫使用上方功能
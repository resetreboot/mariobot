
def get_loop_code(code, ip):
    result = code[ip+1:]
    level = 1
    count = 0
    while count < len(result) and level > 0:
        if result[count] == '[':
            level += 1

        if result[count] == ']':
            level -= 1

        count += 1

    return result[:count-1]


def loop_code(code, cells, pointer, ip):
    output = ""
    while cells[pointer] != 0:
        output += execute(code, cells, pointer, ip)


def execute(code, cells, pointer = 0, ip = 0):
    ip = 0
    output = ""
    while ip < len(code):
        instruction = code[ip]
        if instruction == '>':
            pointer += 1

            if pointer > len(cells):
                pointer = 0

        elif instruction == '<':
            pointer -= 1

            if pointer < 0:
                pointer = len(cells)

        elif instruction == '+':
            cells[pointer] = cells[pointer] + 1

        elif instruction == '-':
            cells[pointer] = cells[pointer] - 1

        elif instruction == '.':
            output += chr(cells[pointer])

        elif instruction == '[':
            inner_code = get_loop_code(code, ip)
            loop_code(inner_code, cells, pointer, ip)
            ip += len(inner_code)    # Jump away after we executed the loop

        ip += 1

    return output

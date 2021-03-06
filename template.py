import os

def run(lines):
    for line in lines:
        print(line)

if __name__ == '__main__':
    is_example = True
    script_dir = os.path.dirname(__file__)
    filename = 'input-example.txt' if is_example else 'input.txt'
    with open(os.path.join(script_dir, filename), 'r') as f:
        answer = run(f.read().splitlines())
        print("### ANSWER ### ")
        print(answer)

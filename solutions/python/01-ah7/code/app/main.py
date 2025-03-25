import sys

# import pyparsing - available if you need it!
# import lark - available if you need it!


def match_pattern(input_line, pattern):
    if len(pattern) == 1:
        return pattern in input_line
    else:
        raise RuntimeError(f"Unhandled pattern: {pattern}")


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    # if sys.argv[1] != "-E":
    #     print("Expected first argument to be '-E'")
    #     exit(1)

    print("1")
    exit(0)


if __name__ == "__main__":
    main()
class BColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    ITALIC = "\x1B[3m"
    UNDERLINE = '\033[4m'


def print_okblue(text, user,  end=""):
    formatted_str = text.format(BColors.OKBLUE+user, BColors.BOLD+BColors.ITALIC, BColors.ENDC+BColors.OKBLUE)
    print(formatted_str+BColors.ENDC, end=end)


def print_info_okblue(text, user,  end=""):
    print_okblue(text, user,  end)

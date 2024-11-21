def draw_char_hash(mychar):
    letter = []
    match mychar:
        case "A": letter = [
                    "    ###    ",
                    "   ## ##   ",
                    "  ##   ##  ",
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## "
                ]
        case "B": letter = [
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ########  "
                ]
        case "C": letter = [
                    "  ######## ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    "  ######## "
                ]
        case "D": letter = [
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ########  "
                ]
        case "E": letter = [
                    " ######### ",
                    " ##        ",
                    " ##        ",
                    " ########  ",
                    " ##        ",
                    " ##        ",
                    " ######### "
                ]
        case "F": letter = [
                    " ######### ",
                    " ##        ",
                    " ##        ",
                    " #######   ",
                    " ##        ",
                    " ##        ",
                    " ##        "
                ]
        case "G": letter = [
                    "  ######## ",
                    " ##        ",
                    " ##        ",
                    " ##   #### ",
                    " ##     ## ",
                    " ##     ## ",
                    "  ######## "
                ]
        case "H": letter = [
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ######### ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## "
                ]
        case "I": letter = [
                    " ######### ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    " ######### "
                ]
        case "K": letter = [
                    " ##    ##  ",
                    " ##   ##   ",
                    " ##  ##    ",
                    " #####     ",
                    " ##  ##    ",
                    " ##   ##   ",
                    " ##    ##  "
                ]
        case "L": letter = [
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ##        ",
                    " ######### "
                ]
        case "M": letter = [
                    " ##     ## ",
                    " ###   ### ",
                    " #### #### ",
                    " ## ### ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## "
                ]
        case "N": letter = [
                    " ##    ##  ",
                    " ###   ##  ",
                    " ####  ##  ",
                    " ## ## ##  ",
                    " ##  ####  ",
                    " ##   ###  ",
                    " ##    ##  "
                ]
        case "O": letter = [
                    "  ######   ",
                    " ##    ##  ",
                    " ##    ##  ",
                    " ##    ##  ",
                    " ##    ##  ",
                    " ##    ##  ",
                    "  ######   "
                ]
        case "P": letter = [
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ########  ",
                    " ##        ",
                    " ##        ",
                    " ##        "
                ]
        case "Q": letter = [
                    "  ######   ",
                    " ##    ##  ",
                    " ##    ##  ",
                    " ##    ##  ",
                    " ## ## ##  ",
                    "  ######   ",
                    "       ### "
                ]
        case "R": letter = [
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ########  ",
                    " ##   ##   ",
                    " ##    ##  ",
                    " ##     ## "
                ]
        case "S": letter = [
                    "  #######  ",
                    " ##        ",
                    " ##        ",
                    "  ######   ",
                    "       ##  ",
                    " ##    ##  ",
                    "  ######   "
                ]
        case "T": letter = [
                    " ######### ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     "
                ]
        case "U": letter = [
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    "  #######  "
                ]
        case "V": letter = [
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    "  ##   ##  ",
                    "   #####   "
                ]
        case "W": letter = [
                    " ##      ## ",
                    " ##  ##  ## ",
                    " ##  ##  ## ",
                    " ##  ##  ## ",
                    " ##  ##  ## ",
                    "  ###  ###  ",
                    "   ##  ##   "
                ]
        case "X": letter = [
                    " ##     ## ",
                    "  ##   ##  ",
                    "   ## ##   ",
                    "    ###    ",
                    "   ## ##   ",
                    "  ##   ##  ",
                    " ##     ## "
                ]
        case "Y": letter = [
                    " ##    ##  ",
                    "  ##  ##   ",
                    "   ####    ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     ",
                    "    ##     "
                ]
        case "Z": letter = [
                    " ######### ",
                    "       ##  ",
                    "      ##   ",
                    "     ##    ",
                    "    ##     ",
                    "   ##      ",
                    " ######### "
                ]
        case "1": letter = [
                    "     ##    ",
                    "    ###    ",
                    "   ####    ",
                    "     ##    ",
                    "     ##    ",
                    "     ##    ",
                    " ########  "
                ]
        case "2": letter = [
                    "  #######  ",
                    " ##     ## ",
                    "       ##  ",
                    "      ##   ",
                    "     ##    ",
                    "    ##     ",
                    " ######### "
                ]
        case "3": letter = [
                    "  #######  ",
                    "       ##  ",
                    "       ##  ",
                    "  #######  ",
                    "       ##  ",
                    " ##     ## ",
                    "  #######  "
                ]
        case "4": letter = [
                    "     ##    ",
                    "   ## ##   ",
                    "  ##  ##   ",
                    " ##   ##   ",
                    " ######### ",
                    "      ##   ",
                    "      ##   "
                ]
        case "5": letter = [
                    " ########  ",
                    " ##        ",
                    " ##        ",
                    " #######   ",
                    "       ##  ",
                    " ##    ##  ",
                    "  #######  "
                ]
        case "6": letter = [
                    "  #######  ",
                    " ##        ",
                    " ##        ",
                    " ########  ",
                    " ##     ## ",
                    " ##     ## ",
                    "  #######  "
                ]
        case "7": letter = [
                    " ######### ",
                    "       ##  ",
                    "      ##   ",
                    "     ##    ",
                    "    ##     ",
                    "   ##      ",
                    "  ##       "
                ]
        case "8": letter = [
                    "  #######  ",
                    " ##     ## ",
                    " ##     ## ",
                    "  #######  ",
                    " ##     ## ",
                    " ##     ## ",
                    "  #######  "
                ]
        case "9": letter = [
                    "  #######  ",
                    " ##     ## ",
                    " ##     ## ",
                    "  ######## ",
                    "       ##  ",
                    " ##     ## ",
                    "  #######  "
                ]
        case "0": letter = [
                    "  #######  ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    " ##     ## ",
                    "  #######  "
                ]
        case " ": letter = [
                    "           ",
                    "           ",
                    "           ",
                    "           ",
                    "           ",
                    "           ",
                    "           "
                ]
    return letter
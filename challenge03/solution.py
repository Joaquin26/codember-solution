replacements = ['"', " ", "[", "]", "\n"]


def get_largest_alternate_colors_length(colors: list[str]):
    max_len = 0
    current_lent = 2
    last_color = colors[1]
    for index, color in enumerate(colors[2:]):
        if color != colors[index + 1] and color == colors[index]:
            current_lent += 1
        else:
            if current_lent >= max_len:
                max_len = current_lent
                last_color = colors[index + 1]
            current_lent = 2
    if current_lent >= max_len:
        max_len = current_lent
        last_color = colors[-1]
    return f"{max_len}@{last_color}"


with open("colors.txt", "r") as file:
    colors = file.read()
    for replace in replacements:
        colors = colors.replace(replace, "")
    colors = colors.split(",")
    print(get_largest_alternate_colors_length(colors))

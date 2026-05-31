import os
import time
import random

def draw_colored_tree(height=12, light_percentage=0.05):
    # ANSI Color Constants
    GREEN = "\033[38;2;0;100;0m"        # Dark green needles
    BROWN = "\033[38;2;139;69;19m"       # Brown trunk
    RESET = "\033[0m"
    
    LIGHT_COLORS = [
        "\033[38;2;255;0;0m",     # Red
        "\033[38;2;255;255;0m",   # Yellow
        "\033[38;2;0;255;255m",   # Cyan
        "\033[38;2;255;0;255m",   # Magenta
        "\033[38;2;255;165;0m",   # Orange
        "\033[38;2;255;105;180m", # Pink
        "\033[38;2;124;252;0m"    # Lawn Green
    ]

    star_positions = []
    for r in range(1, height + 1):
        num_stars = 2 * r - 1
        for c in range(num_stars):
            star_positions.append((r, c))

    total_stars = len(star_positions)
    num_lights = max(1, int(total_stars * light_percentage))
    light_indices = set(random.sample(range(total_stars), num_lights))
    
    output = []
    idx = 0
    for r in range(1, height + 1):
        leading_spaces = " " * (height - r)
        line_chars = []
        num_stars = 2 * r - 1
        for c in range(num_stars):
            if idx in light_indices:
                color = random.choice(LIGHT_COLORS)
                line_chars.append(f"{color}*{RESET}")
            else:
                line_chars.append(f"{GREEN}*{RESET}")
            idx += 1
        output.append(leading_spaces + "".join(line_chars))

    trunk_spaces = " " * (height - 2)
    trunk_color = f"{BROWN}|||{RESET}"
    output.append(trunk_spaces + trunk_color)
    output.append(trunk_spaces + trunk_color)
    
    return "\n".join(output)

def main():
    print("Press Ctrl+C to stop the blinking animation.\n")
    time.sleep(1)
    
    # Dynamic blinking animation loop
    try:
        while True:
            # Clear standard terminal screen cleanly in Windows/Linux/macOS
            os.system('cls' if os.name == 'nt' else 'clear')
            print(draw_colored_tree(12))
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nBlinking tree animation stopped.")

if __name__ == "__main__":
    main()

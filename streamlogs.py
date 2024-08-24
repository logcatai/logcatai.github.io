
import time

# Define ANSI escape codes for colors
COLOR_RESET = "\033[0m"
COLOR_RED = "\033[91m"    # Light red
COLOR_GREEN = "\033[92m"  # Light green
COLOR_YELLOW = "\033[93m" # Light yellow
COLOR_BLUE = "\033[94m"   # Light blue

# Function to get color based on log level
def get_color_for_log_level(log_level):
    if log_level == 'E':
        return COLOR_RED
    elif log_level == 'W':
        return COLOR_YELLOW
    elif log_level == 'I':
        return COLOR_GREEN
    elif log_level == 'D':
        return COLOR_BLUE
    elif log_level == 'V':
        return COLOR_RESET  # Default color (no color)
    else:
        return COLOR_RESET  # Default color for any other cases

def stream_log_file(file_path, delay=0.5):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                # Extract the log level (assuming it follows the PID and TID)
                log_level = stripped_line.split()[3] if len(stripped_line.split()) > 3 else 'I'
                color = get_color_for_log_level(log_level)
                # Print the colored log line
                print(f"{color}{stripped_line}{COLOR_RESET}")
                time.sleep(delay)
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the path to your log file
log_file_path = 'dummy_logcat_logs.txt'

# Call the function to start streaming logs with color
stream_log_file(log_file_path)


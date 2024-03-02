import re
import sys

def process_input():
    total = 0
    processing_enabled = True
    patterns = [
        r"(?P<number>[+-]?\d+)",    
        r"(?P<activate>on)",       
        r"(?P<deactivate>off)",    
        r"(?P<calculate>=)"         
    ]

    combined_patterns = re.compile('|'.join(patterns), re.IGNORECASE)
    for input_line in sys.stdin:
        found_matches = re.finditer(combined_patterns, input_line)
        for match in found_matches:
            if match.lastgroup == 'number':
                total += int(match.group('number')) if processing_enabled else 0
            elif match.lastgroup == 'activate':
                processing_enabled = True
            elif match.lastgroup == 'deactivate':
                processing_enabled = False
            elif match.lastgroup == 'calculate':
                print("Total = " + str(total))

if __name__ == "__main__":
    process_input()

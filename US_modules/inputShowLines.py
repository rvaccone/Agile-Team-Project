#TaeSeo 

#List line numbers from GEDCOM source file when reporting errors
def report_errors_in_gedcom(file_path):
    error_lines = []
    
    with open(file_path, 'r') as gedcom_file:
        line_number = 0
        
        for line in gedcom_file:
            line_number += 1
            
            # Check for errors on the current line.
            # Replace 'error_condition' with the actual condition you want to check for.
            error_condition = False
            
            if error_condition:
                error_lines.append(line_number)
                print(f"Error found on line {line_number}: {line.strip()}")
    
    return error_lines

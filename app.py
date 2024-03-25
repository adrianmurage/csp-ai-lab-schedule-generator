from flask import Flask, render_template, request
from constraint import Problem, AllDifferentConstraint
import json


app = Flask(__name__)

# Function to solve CSP problem for a group


def solve_csp(group_data, labs):
    problem = Problem()

    # Add variables to the problem
    for class_data in group_data:
        course_code = class_data[2]
        section = class_data[3]
        variable_name = f"{course_code}_{section}"
        problem.addVariable(variable_name, labs)

    # Add AllDifferentConstraint to ensure each class is assigned to a different lab
    problem.addConstraint(AllDifferentConstraint())

    # Solve the problem
    solution = problem.getSolution()

    return solution

# Function to print lab distribution for each group


# Function to print lab distribution for each group
def print_lab_distribution(grouped_data, labs):
    master_solutions = []
    for group, data in grouped_data.items():
        # Extract class names for the group
        class_names = [
            f"{class_data[2]}_{class_data[3]}" for class_data in data]

        # Solve CSP for all classes in the group together
        solution = solve_csp(data, labs)

        solutions = []
        if solution:
            for class_name in class_names:
                # Get lab or empty string if not found
                lab = solution.get(class_name, '')
                class_data = next(
                    cd for cd in data if f"{cd[2]}_{cd[3]}" == class_name)
                course_name = class_data[4]  # Course name
                # Print the faculty names for debugging
                print("Raw faculty name:", class_data[5].strip('"'))
                # Fix faculty name by splitting and formatting
                faculty = ", ".join(class_data[5].strip('"').split(', '))
                print("Formatted faculty name:", faculty)
                # Include all values
                solutions.append((class_name, lab, course_name, faculty))
        else:
            # If no solution found, append placeholder values
            solutions = [(class_name, '', '', '')
                         for class_name in class_names]

        master_solutions.append((group, solutions))

    return master_solutions


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Read CSV file
            stream = file.stream
            stream.seek(0)
            csv_data = stream.read().decode("UTF-8").splitlines()
            header = csv_data[0].split(",")
            data = [row.split(",") for row in csv_data[1:]]

            # Group data
            grouped_data = {}
            for row in data:
                key = f"{row[0]} {row[1]}"
                if key not in grouped_data:
                    grouped_data[key] = []
                grouped_data[key].append(row)

            # Solve CSP and print lab distribution
            labs = ['LAB1', 'LAB2', 'LAB3', 'LAB4',
                    'LAB7', 'GLAB', 'HLAB', 'SLAB']
            schedule = print_lab_distribution(grouped_data, labs)

            # Convert schedule to JSON string
            schedule_json = json.dumps(schedule)

            # Render lab schedule HTML with schedule_json
            return render_template('schedule.html', schedule=schedule)
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(debug=True)

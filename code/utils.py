"""Non-UI specific utility functions"""

import pandas as pd
import os

EMPLOYEE_PICKLE_FILE = "../data/employee.pkl"
PROJECT_PICKLE_FILE = "../data/project.pkl"


def remove_all_data():
    """
    Removes all the employee and project data.

    """
    if os.path.exists(EMPLOYEE_PICKLE_FILE):
        os.remove(EMPLOYEE_PICKLE_FILE)
    if os.path.exists(PROJECT_PICKLE_FILE):
        os.remove(PROJECT_PICKLE_FILE)


def dump_details(category, data):
    """
    Dump the data entered by the user (from the application)
    as pickle files.

    :param category: Tells if the data is for the project or employee
    :param data: The main data entered by the user from the application.

    """
    old_data = None
    filename = EMPLOYEE_PICKLE_FILE if category == "employee" else PROJECT_PICKLE_FILE
    if os.path.exists(filename):
        old_data = pd.read_pickle(filename)
    new_entry = pd.DataFrame(data, index=[0])
    if old_data is not None:
        pd.concat([old_data, new_entry]).to_pickle(filename)
    else:
        new_entry.to_pickle(filename)


def allot_projects():
    """
    The primary function that allots the projects to the employees.
    It generates a maximum match for a bipartite graph of employees and projects.

    :return: A tuple having the allotments, count of employees allotted and
    total project headcount (a project where two people need to work
    will have a headcount ot two).

    """
    allotments = []
    try:
        emp_data = pd.read_pickle(EMPLOYEE_PICKLE_FILE)
        project_data = pd.read_pickle(PROJECT_PICKLE_FILE)
    except IOError as e:
        print("Either employee or project data is not present. No allocation done.")
        return [], 0, 0

    employees = []
    for _, emp_row in emp_data.iterrows():
        transposed = emp_row.T
        transposed = transposed[transposed == 1]
        skills = set(transposed.index)
        employees.append(
            {
                'name': emp_row['name'],
                'value': skills
            }
        )
    projects = []
    for _, project_row in project_data.iterrows():
        n = int(project_row['emp_count'])
        for i in range(n):
            projects.append(
                {
                    'absolute_name': project_row['name'],
                    'name': project_row['name'] + str(i),
                    'value': set(project_row[['domain', 'language', 'type']].values)
                }
            )
    matrix = []
    for e in employees:
        row = []
        for p in projects:
            if len(e['value'].intersection(p['value'])) >= 2:
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)

    employee_count = len(employees)
    project_count = len(projects)

    # An array to keep track of the employees assigned to projects.
    # The value of emp_project_match[i] is the employee number
    # assigned to project i.
    # If value = -1 indicates nobody is allocated that project.
    emp_project_match = [-1] * project_count

    def bipartite_matching(employee, match, seen):
        """
        A DFS based recursive solution that returns true if a project mapping
        for employee is possible.

        :param employee: The employee for whom we are searching a project.
        :param match: Stores the assigned employees to projects.
        :param seen: An array to tell the projects available to employee.
        :return: `True` if match for employee is possible else `False`.

        """

        # Try every project one by one.
        for project in range(project_count):

            # If employee is fit for the project and the project has not yet been
            # checked by the employee.
            if matrix[employee][project] and seen[project] is False:

                # Mark the project as checked by employee.
                seen[project] = True

                # If project is not assigned to anyone or previously assigned to someone else
                # (match[project]) but that employee could find an alternate project.
                # Note that since the project has been seen by the employee above, it will
                # not be available to match[project].
                if match[project] == -1 or bipartite_matching(match[project], match, seen):
                    match[project] = employee
                    return True

        return False

    emp_allotted = 0
    for emp in range(employee_count):
        # Mark all projects as not seen for next applicant.
        projects_seen = [False] * project_count
        # Find if the employee can be assigned a project
        if bipartite_matching(emp, emp_project_match, projects_seen):
            emp_allotted += 1

    for p, e in enumerate(emp_project_match):
        if e != -1:
            allotments.append((employees[e]['name'], projects[p]['absolute_name']))

    return allotments, emp_allotted, project_count

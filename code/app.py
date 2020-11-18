"""
The main project manager application.

"""

import tkinter as tk
import tkinter.font as font
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils import *


def construct_app():
    """
    Construct the GUI application using Tkinter.

    """
    root = tk.Tk()
    root.title("PROJECT MANAGEMENT")

    root.geometry("+{}+{}".format(int(root.winfo_reqwidth()), int(root.winfo_reqheight())))

    main_panel = tk.PanedWindow()
    main_panel.pack(fill=tk.BOTH, expand=True)

    # ---------------------------------------------------LEFT PANEL-----------------------------------------------------

    left_panel = tk.PanedWindow(main_panel, bg="#004c72", orient=tk.VERTICAL)
    main_panel.add(left_panel)

    emp = tk.Label(left_panel, text="EMPLOYEE",
                   font=font.Font(family='Copperplate Gothic Bold', size=15),
                   anchor=tk.W,
                   relief=tk.RAISED,
                   fg="white", bg='#d11d53', bd=5)
    left_panel.add(emp)

    name_window = tk.PanedWindow(left_panel, bg="#004c72",
                                 orient=tk.HORIZONTAL)
    left_panel.add(name_window)
    name_lbl = tk.Label(name_window,
                        text="Name:",
                        font=font.Font(family='Copperplate Gothic Bold', size=15), bg="#004c72", fg="white")
    name_val = tk.Entry(name_window)
    name_window.add(name_lbl)
    name_window.add(name_val)

    language_lbl = tk.Label(left_panel,
                            anchor=tk.W,
                            text="Language",
                            font=font.Font(family='Copperplate Gothic Bold', size=15,
                                           underline=True), bg="#004c72",
                            fg="white")
    left_panel.add(language_lbl)

    language_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(language_window)

    python_val = tk.IntVar()
    java_val = tk.IntVar()
    cpp_val = tk.IntVar()

    java_btn = tk.Checkbutton(language_window, justify=tk.LEFT,
                              font=font.Font(family='Copperplate Gothic Bold', size=15),
                              text="Java",
                              onvalue=1, offvalue=0,
                              variable=java_val, bg="#a7e2ff")
    language_window.add(java_btn)

    python_btn = tk.Checkbutton(language_window, justify=tk.LEFT,
                                text="Python",
                                font=font.Font(family='Copperplate Gothic Bold', size=15),
                                onvalue=1, offvalue=0,
                                variable=python_val, bg="#a7e2ff")
    language_window.add(python_btn)

    cpp_btn = tk.Checkbutton(language_window, justify=tk.LEFT,
                             font=font.Font(family='Copperplate Gothic Bold', size=15),
                             text="C++",
                             onvalue=1, offvalue=0,
                             variable=cpp_val, bg="#a7e2ff")
    language_window.add(cpp_btn)

    domain_lbl = tk.Label(left_panel,
                          anchor=tk.W,
                          text="Domain",
                          font=font.Font(family='Copperplate Gothic Bold', size=15, underline=True),
                          bg="#004c72", fg="white")
    left_panel.add(domain_lbl)

    domain_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(domain_window)
    payments_val = tk.IntVar()
    tracking_val = tk.IntVar()
    inventory_val = tk.IntVar()
    payments_btn = tk.Checkbutton(domain_window, justify=tk.LEFT, text="Payments",
                                  font=font.Font(family='Copperplate Gothic Bold', size=15),
                                  onvalue=1, offvalue=0,
                                  variable=payments_val, bg="#a7e2ff")
    domain_window.add(payments_btn)
    tracking_btn = tk.Checkbutton(domain_window, justify=tk.LEFT, text="Tracking",
                                  font=font.Font(family='Copperplate Gothic Bold', size=15),
                                  onvalue=1, offvalue=0,
                                  variable=tracking_val, bg="#a7e2ff")
    domain_window.add(tracking_btn)
    inventory_btn = tk.Checkbutton(domain_window, justify=tk.LEFT, text="Inventory",
                                   font=font.Font(family='Copperplate Gothic Bold', size=15),
                                   onvalue=1, offvalue=0,
                                   variable=inventory_val, bg="#a7e2ff")
    domain_window.add(inventory_btn)

    type_lbl = tk.Label(left_panel, text="Type",
                        anchor=tk.W,
                        font=font.Font(family='Copperplate Gothic Bold', size=15, underline=True), bg="#004c72",
                        fg="white")
    left_panel.add(type_lbl)

    type_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(type_window)
    frontend_val = tk.IntVar()
    backend_val = tk.IntVar()
    ios_val = tk.IntVar()
    android_val = tk.IntVar()
    frontend_btn = tk.Checkbutton(type_window, justify=tk.LEFT, text="Front-end",
                                  font=font.Font(family='Copperplate Gothic Bold', size=15),
                                  onvalue=1, offvalue=0, variable=frontend_val, bg="#a7e2ff")
    type_window.add(frontend_btn)
    backend_btn = tk.Checkbutton(type_window, justify=tk.LEFT, text="Back-end",
                                 font=font.Font(family='Copperplate Gothic Bold', size=15),
                                 onvalue=1, offvalue=0, variable=backend_val, bg="#a7e2ff")
    type_window.add(backend_btn)
    ios_btn = tk.Checkbutton(type_window, justify=tk.LEFT, text="Mobile Application: iOS",
                             font=font.Font(family='Copperplate Gothic Bold', size=15),
                             onvalue=1, offvalue=0,
                             variable=ios_val, bg="#a7e2ff")
    type_window.add(ios_btn)
    android_btn = tk.Checkbutton(type_window, justify=tk.LEFT, text="Mobile Application: Android",
                                 font=font.Font(family='Copperplate Gothic Bold'),
                                 onvalue=1,
                                 offvalue=0, variable=android_val, bg="#a7e2ff")
    type_window.add(android_btn)

    add_emp_btn = tk.Button(left_panel,
                            text="Add Employee",
                            font=font.Font(family='Copperplate Gothic Bold', size=15),
                            command=lambda: dump_details(category="employee", data={
                                "name": name_val.get(),
                                "python": python_val.get(),
                                "java": java_val.get(),
                                "cpp": cpp_val.get(),
                                "payments": payments_val.get(),
                                "tracking": tracking_val.get(),
                                "inventory": inventory_val.get(),
                                "frontend": frontend_val.get(),
                                "backend": backend_val.get(),
                                "ios": ios_val.get(),
                                "android": android_val.get()}))
    left_panel.add(add_emp_btn)

    project = tk.Label(left_panel,
                       text="PROJECT",
                       font=font.Font(family='Copperplate Gothic Bold', size=15),
                       anchor=tk.W, relief=tk.RAISED, fg="white", bg='#d11d53', bd=5)
    left_panel.add(project)

    p_name_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(p_name_window)
    p_name_lbl = tk.Label(p_name_window, text="Name:",
                          font=font.Font(family='Copperplate Gothic Bold',
                                         size=15), bg="#004c72", fg="white")
    p_name_val = tk.Entry(p_name_window)
    p_name_window.add(p_name_lbl)
    p_name_window.add(p_name_val)

    p_language_lbl = tk.Label(left_panel, text="Language",
                              anchor=tk.W,
                              font=font.Font(family='Copperplate Gothic Bold', size=15,
                                             underline=True), bg="#004c72", fg="white")
    left_panel.add(p_language_lbl)

    p_language_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(p_language_window)
    p_lang_val = tk.StringVar()
    p_java_btn = tk.Radiobutton(p_language_window, justify=tk.LEFT, text="Java",
                                font=font.Font(family='Copperplate Gothic Bold',
                                               size=15), variable=p_lang_val, value="java", bg="#a7e2ff")
    p_language_window.add(p_java_btn)
    p_python_btn = tk.Radiobutton(p_language_window, justify=tk.LEFT, text="Python",
                                  font=font.Font(family='Copperplate Gothic Bold',
                                                 size=15), variable=p_lang_val, value="python", bg="#a7e2ff")
    p_language_window.add(p_python_btn)
    p_cpp_btn = tk.Radiobutton(p_language_window, justify=tk.LEFT, text="C++",
                               font=font.Font(family='Copperplate Gothic Bold',
                                              size=15), variable=p_lang_val, value="cpp", bg="#a7e2ff")
    p_language_window.add(p_cpp_btn)

    p_domain_lbl = tk.Label(left_panel,
                            anchor=tk.W,
                            text="Domain",
                            font=font.Font(family='Copperplate Gothic Bold', size=15,
                                           underline=True), bg="#004c72",
                            fg="white")
    left_panel.add(p_domain_lbl)

    p_domain_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(p_domain_window)
    p_domain_val = tk.StringVar()
    p_payments_btn = tk.Radiobutton(p_domain_window, justify=tk.LEFT, text="Payments",
                                    font=font.Font(family='Copperplate Gothic Bold',
                                                   size=15), variable=p_domain_val,
                                    value="payments", bg="#a7e2ff")
    p_domain_window.add(p_payments_btn)
    p_tracking_btn = tk.Radiobutton(p_domain_window, justify=tk.LEFT, text="Tracking",
                                    font=font.Font(family='Copperplate Gothic Bold',
                                                   size=15), variable=p_domain_val,
                                    value="tracking", bg="#a7e2ff")
    p_domain_window.add(p_tracking_btn)
    p_inventory_btn = tk.Radiobutton(p_domain_window, justify=tk.LEFT, text="Inventory",
                                     font=font.Font(family='Copperplate Gothic Bold',
                                                    size=15), variable=p_domain_val,
                                     value="inventory", bg="#a7e2ff")
    p_domain_window.add(p_inventory_btn)

    p_type_lbl = tk.Label(left_panel,
                          anchor=tk.W,
                          text="Type",
                          font=font.Font(family='Copperplate Gothic Bold', size=15,
                                         underline=True), bg="#004c72",
                          fg="white")
    left_panel.add(p_type_lbl)

    p_type_window = tk.PanedWindow(left_panel, orient=tk.HORIZONTAL, bg="#004c72")
    left_panel.add(p_type_window)
    p_type_val = tk.StringVar()
    p_frontend_btn = tk.Radiobutton(p_type_window, justify=tk.LEFT, text="Front-end",
                                    font=font.Font(family='Copperplate Gothic Bold',
                                                   size=15), variable=p_type_val,
                                    value="frontend", bg="#a7e2ff")
    p_type_window.add(p_frontend_btn)
    p_backend_btn = tk.Radiobutton(p_type_window, justify=tk.LEFT, text="Back-end",
                                   font=font.Font(family='Copperplate Gothic Bold',
                                                  size=15), variable=p_type_val,
                                   value="backend", bg="#a7e2ff")
    p_type_window.add(p_backend_btn)
    p_ios_btn = tk.Radiobutton(p_type_window, justify=tk.LEFT, text="Mobile Application: iOS",
                               font=font.Font(family='Copperplate Gothic Bold',
                                              size=15), variable=p_type_val,
                               value="ios", bg="#a7e2ff")
    p_type_window.add(p_ios_btn)
    p_android_btn = tk.Radiobutton(p_type_window, justify=tk.LEFT, text="Mobile Application: Android",
                                   font=font.Font(family='Copperplate Gothic Bold',
                                                  size=15), variable=p_type_val,
                                   value="android",
                                   bg="#a7e2ff")
    p_type_window.add(p_android_btn)

    emp_count_window = tk.PanedWindow(left_panel, bg="#004c72", orient=tk.HORIZONTAL)
    left_panel.add(emp_count_window)
    emp_count_lbl = tk.Label(emp_count_window, text="Employee Count:",
                             font=font.Font(family='Copperplate Gothic Bold', size=15),
                             bg="#004c72", fg="white")
    emp_count_spinbox = tk.Spinbox(left_panel, font=font.Font(family='Copperplate Gothic Bold',
                                                      size=15), from_=1, to=3)
    emp_count_window.add(emp_count_lbl)
    emp_count_window.add(emp_count_spinbox)

    add_project_btn = tk.Button(left_panel, text="Add Project",
                                font=font.Font(family='Copperplate Gothic Bold', size=15),
                                command=lambda: dump_details(category="project", data={
                                    "name": p_name_val.get(),
                                    "language": p_lang_val.get(),
                                    "domain": p_domain_val.get(),
                                    "type": p_type_val.get(),
                                    "emp_count": emp_count_spinbox.get()}))
    left_panel.add(add_project_btn)

    # -------------------------------------------------RIGHT PANEL------------------------------------------------------
    right_panel = tk.PanedWindow(main_panel, orient=tk.VERTICAL, bg="#F5F5F5")
    main_panel.add(right_panel)

    refresh_btn = tk.Button(right_panel, anchor=tk.N, text="Refresh",
                            font=font.Font(family='Copperplate Gothic Bold', size=15),
                            command=lambda: refresh(root))
    right_panel.add(refresh_btn)

    clear_btn = tk.Button(right_panel, anchor=tk.N, text="Clear",
                          font=font.Font(family='Copperplate Gothic Bold', size=15),
                          command=lambda: refresh(root, clear=True))
    right_panel.add(clear_btn)

    allotments, emp_allotted, project_count = allot_projects()

    add_result_map(right_panel, allotments)

    # Add a pie chart showing how many assignments were done
    # and how many are still left.
    if len(allotments) > 0:
        fig = plt.Figure(figsize=(1, 1))
        ax = fig.add_axes([0, 0, 1, 1])
        chart_type = FigureCanvasTkAgg(fig, right_panel)
        right_panel.add(chart_type.get_tk_widget())
        ax.axis('equal')
        students = [emp_allotted, project_count - emp_allotted]
        ax.pie(students, colors=["#008400", "#b30000"])

    root.mainloop()


def add_result_map(window, allotments):
    """
    Add the resultant allotments to the application.

    :param window: The window where we want to add the result (allotments).
    :param allotments: A list of tuples having employee to project mappings.

    """
    if len(allotments) == 0:
        lbl = tk.Label(window, anchor=tk.N, text="NO DATA", relief=tk.RAISED,
                       font=font.Font(family='Copperplate Gothic Bold', size=15), fg="white",
                       bg="#004c72")
        window.add(lbl)
    for i, (emp, project) in enumerate(allotments):
        lbl = tk.Label(window, anchor=tk.N, text=emp + " -> " + project,
                       font=font.Font(family='Copperplate Gothic Bold', size=15), fg="white",
                       bg="#004c72" if i % 2 == 0 else "#d11d53")
        window.add(lbl)
    lbl = tk.Label(window, anchor=tk.N, text="",
                   font=font.Font(family='Copperplate Gothic Bold', size=15), bg="white")
    window.add(lbl)


def refresh(root, clear=False):
    """
    Refresh the application by restarting it.

    :param root: The main window of the application.
    :param clear: If true, it deletes the existing employee and project data, enabling
                  the user to restart the process.

    """
    if clear:
        remove_all_data()
    root.destroy()
    construct_app()


def main():
    construct_app()


if __name__ == '__main__':
    main()

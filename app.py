import flet as ft
import os

def main(page: ft.Page):
    page.title = "Gabriel Portfolio"
    page.theme_mode = ft.ThemeMode.DARK  
    page.padding = 20
    
    # Disables continuous page scrolling
    page.scroll = None  

    # --- ROUTING VIEW SWITCHER ---
    def switch_section(section_name):
        display_canvas.controls.clear()
        
        if section_name == "About Me":
            display_canvas.controls.append(view_about_me())
        elif section_name == "Project Timeline":
            display_canvas.controls.append(view_project_timeline())
        elif section_name == "Matlab Achievements":
            display_canvas.controls.append(view_matlab_achievements())
        elif section_name == "Technical Blog":
            display_canvas.controls.append(view_technical_blog())
        elif section_name == "Mathematical Notation":
            display_canvas.controls.append(view_mathematical_notation())
        elif section_name == "Github Evidence":
            display_canvas.controls.append(view_github_evidence())
        
        page.update()

    def on_nav_click(e):
        clicked_text = e.control.text if hasattr(e.control, "text") and e.control.text else e.control.data
        switch_section(clicked_text)
        if page.drawer:
            page.drawer.open = False
            page.update()

    # --- FUNCTION TO OPEN PRODUCTION WEBPAGE CERTIFICATE PDFS ---
    def open_certificate(e):
        pdf_name = e.control.data
        # On the web, assets are served directly relative to the app root folder
        web_pdf_path = f"assets/{pdf_name}"
        page.launch_url(web_pdf_path)

    # --- WIREFRAME SUBVIEW BUILDERS ---

    def view_about_me():
        return ft.Column([
            ft.Text("About Me", size=26, weight=ft.FontWeight.BOLD),
            ft.ResponsiveRow([
                ft.Container(
                    content=ft.Column([
                        ft.Container(
                            content=ft.Video(
                                expand=True,
                                playlist=[ft.VideoMedia("gabi.mp4")],
                                playlist_mode=ft.PlaylistMode.LOOP,
                                fill_color=ft.colors.BLACK26,
                                aspect_ratio=16/9,
                                autoplay=False,
                                show_controls=True,
                            ),
                            border=ft.border.all(1, ft.colors.WHITE10),
                            border_radius=8,
                        ),
                        ft.ElevatedButton("Watch Videos", icon=ft.icons.PLAY_ARROW_ROUNDED)
                    ]),
                    col={"sm": 12, "md": 6}
                ),
                ft.Container(
                    content=ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("Project Contribution", size=16, weight=ft.FontWeight.W_600),
                                ft.Text(
                                    "Hello, my name is Gabriel Filemon Shuumbwa, a second-year Electrical Engineering "
                                    "student with a strong interest in software development and problem-solving. "
                                    "During my semester project, I was responsible for project documentation while "
                                    "also assisting with the development of the application alongside the project manager, "
                                    "Aletta Gottlieb. Working on the project allowed me to gain practical experience "
                                    "in software development, teamwork, and project planning. I enjoy learning new "
                                    "technologies, improving my coding skills, and applying engineering principles "
                                    "to create useful solutions to real-world problems.",
                                    color=ft.colors.WHITE70,
                                    size=14
                                )
                            ]),
                            padding=20
                        )
                    ),
                    col={"sm": 12, "md": 6}
                )
            ], spacing=20)
        ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def view_project_timeline():
        timeline_data = [
            {"date": "20 Feb 2026", "task": "Project Briefing & Team Allocation", "status": "Completed"},
            {"date": "06 Mar 2026", "task": "Requirements Specification & Initial Design", "status": "Completed"},
            {"date": "27 Mar 2026", "task": "Preliminary Design Review (PDR)", "status": "Completed"},
            {"date": "24 Apr 2026", "task": "Critical Design Review (CDR)", "status": "Completed"},
            {"date": "15 May 2026", "task": "System Integration & Initial Testing", "status": "Completed"},
            {"date": "22 May 2026", "task": "Final Project Showcase & Presentation", "status": "In Progress"},
            {"date": "29 May 2026", "task": "Final Report & Portfolio Submission", "status": "Upcoming"},
        ]

        timeline_tiles = []
        for milestone in timeline_data:
            is_upcoming = milestone["status"] == "Upcoming"
            is_progress = milestone["status"] == "In Progress"
            
            icon_color = ft.colors.GREY_600 if is_upcoming else (ft.colors.AMBER_500 if is_progress else ft.colors.GREEN_500)
            icon_type = ft.icons.RADIO_BUTTON_UNCHECKED if is_upcoming else (ft.icons.PENDING_OUTLINED if is_progress else ft.icons.CHECK_CIRCLE_ROUNDED)

            timeline_tiles.append(
                ft.Row([
                    ft.Container(
                        content=ft.Text(milestone["date"], size=13, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                        width=100
                    ),
                    ft.Icon(icon_type, color=icon_color, size=20),
                    ft.VerticalDivider(width=10, color=ft.colors.WHITE10),
                    ft.Column([
                        ft.Text(milestone["task"], size=15, weight=ft.FontWeight.W_500),
                        ft.Text(milestone["status"], size=12, color=icon_color)
                    ], spacing=2, expand=True)
                ], alignment=ft.MainAxisAlignment.START)
            )

        return ft.Column([
            ft.Text("Project Timeline", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Semester Milestones & Execution Schedule", size=14, color=ft.colors.WHITE38),
            ft.Container(
                content=ft.Column(timeline_tiles, spacing=20, scroll=ft.ScrollMode.ADAPTIVE),
                padding=20,
                bgcolor=ft.colors.BLACK26,
                border=ft.border.all(1, ft.colors.WHITE10),
                border_radius=8,
                expand=True
            )
        ], expand=True)

    def view_matlab_achievements():
        certificates = [
            {"title": "MATLAB Onramp", "file": "certificate onramp.pdf"},
            {"title": "Simulink Onramp", "file": "certificate simulink onramp.pdf"},
            {"title": "Calculation with Vectors", "file": "certificate calculation with vectors.pdf"},
            {"title": "Circuit Simulation", "file": "certificate circuit simulation.pdf"}
        ]

        certificate_cards = []
        for cert in certificates:
            certificate_cards.append(
                ft.Container(
                    content=ft.Column([
                        ft.Icon(ft.icons.PICTURE_AS_PDF_ROUNDED, size=36, color=ft.colors.RED_ACCENT),
                        ft.Text(cert["title"], size=13, weight=ft.FontWeight.BOLD, text_align=ft.TextAlign.CENTER),
                        ft.Text("Click to view certificate", size=11, color=ft.colors.WHITE70)
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    bgcolor=ft.colors.SURFACE_VARIANT,
                    border_radius=8,
                    padding=10,
                    height=130,
                    on_click=open_certificate,
                    data=cert["file"],  
                    col={"sm": 6, "md": 3}  
                )
            )

        gallery_images = [
            "Screenshot 2026-05-31 102944.png",
            "Screenshot 2026-05-31 162820.png",
            "Screenshot 2026-05-31 164844.png"
        ]

        pic_grid = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=ft.Image(
                        src=img_src,
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=6,
                    ),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.BLACK26,
                    border=ft.border.all(1, ft.colors.WHITE10),
                    border_radius=6,
                    padding=6,
                    height=200,
                    col={"sm": 12, "md": 4}
                ) for img_src in gallery_images
            ], 
            spacing=12
        )

        return ft.Column([
            ft.Text("Matlab Achievements", size=26, weight=ft.FontWeight.BOLD),
            ft.Text("Verified Course Certifications (Stored in local assets)", size=14, color=ft.colors.BLUE_200, weight=ft.FontWeight.W_500),
            ft.ResponsiveRow(certificate_cards, spacing=12),
            ft.Text("Project Evidence Gallery", size=14, color=ft.colors.BLUE_200, weight=ft.FontWeight.W_500),
            pic_grid
        ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def view_technical_blog():
        return ft.Column([
            ft.Text("Technical Blog", size=26, weight=ft.FontWeight.BOLD),
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text("Lessons I Learned During Our Semester Project", size=20, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_200),
                        ft.Divider(thickness=1, color=ft.colors.WHITE10),
                        
                        ft.Text(
                            "One of the most valuable experiences in my academic journey was working on our semester project. "
                            "My primary responsibility was project documentation, but I also assisted with coding and worked "
                            "closely with our project manager, Aletta Gottlieb, throughout the development process.",
                            size=14, color=ft.colors.WHITE70
                        ),
                        ft.Text(
                            "Like many software projects, we faced several challenges during development. There were times when "
                            "our application crashed due to errors in the code, and troubleshooting these issues often took longer "
                            "than expected. Although these challenges were frustrating, they taught us important lessons about "
                            "software development and teamwork.",
                            size=14, color=ft.colors.WHITE70
                        ),
                        
                        ft.Text("1. Importance of a Planned Timeline", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER_400),
                        ft.Text(
                            "One lesson I learned is the importance of following a well-planned timeline. When tasks are completed "
                            "according to schedule, it becomes easier to identify problems early and make necessary adjustments. "
                            "Good time management also reduces pressure and helps the team stay focused on project goals.",
                            size=14, color=ft.colors.WHITE70
                        ),
                        
                        ft.Text("2. Clear Logic & Structure Premise", size=15, weight=ft.FontWeight.BOLD, color=ft.colors.AMBER_400),
                        ft.Text(
                            "Another important lesson was the value of having a clear logic and structure before starting development. "
                            "Understanding how the application should be organized, how different components interact, and how data "
                            "flows through the system makes coding more efficient and helps prevent unnecessary errors.",
                            size=14, color=ft.colors.WHITE70
                        ),
                        
                        ft.Text(
                            "This project strengthened my technical skills, improved my ability to work within a team, and showed me "
                            "that successful software development requires careful planning, communication, and persistence. "
                            "The challenges we faced became opportunities to learn, and the experience has prepared me for "
                            "future projects in both my academic and professional career.",
                            size=14, color=ft.colors.WHITE70
                        ),
                    ], spacing=14),
                    padding=24
                )
            )
        ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    def view_mathematical_notation():
        return ft.Column([
            ft.Text("Mathematical Notation", size=26, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=ft.Column([
                    ft.Text("Put Blasting Formulas Here", size=16, weight=ft.FontWeight.W_500, color=ft.colors.AMBER_400),
                    ft.Text("$$E = mc^2$$", size=28, weight=ft.FontWeight.BOLD),
                    ft.Text("$$\\int_{a}^{b} f(x)\\,dx = F(b) - F(a)$$", size=22, italic=True)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=15),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.BLACK26,
                border=ft.border.all(1, ft.colors.WHITE10),
                border_radius=8,
                padding=30,
                expand=True
            )
        ], expand=True)

    def view_github_evidence():
        return ft.Column([
            ft.Text("Github Evidence", size=26, weight=ft.FontWeight.BOLD),
            
            ft.Card(ft.Container(content=ft.Column([
                ft.Text("Commit History", size=16, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Image(
                        src="commit_logs.png",
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=6
                    ),
                    bgcolor=ft.colors.BLACK26,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1, ft.colors.WHITE10),
                    border_radius=6,
                ),
                ft.Text("A paragraph explaining the image and tracking master branch commits context.", size=13)
            ]), padding=12)),

            ft.Card(ft.Container(content=ft.Column([
                ft.Text("Pull Request Logs", size=16, weight=ft.FontWeight.BOLD),
                ft.Container(
                    content=ft.Image(
                        src="pull_requests.png",
                        fit=ft.ImageFit.CONTAIN,
                        border_radius=6
                    ),
                    bgcolor=ft.colors.BLACK26,
                    alignment=ft.alignment.center,
                    border=ft.border.all(1, ft.colors.WHITE10),
                    border_radius=6,
                ),
            ]), padding=12)),

            ft.Card(ft.Container(content=ft.Column([
                ft.Text("Impact Summary", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("A paragraph breakdown verifying total deployment analytics, automated test coverage percentages, and stable feature versions.", size=13)
            ]), padding=12))
        ], scroll=ft.ScrollMode.ADAPTIVE, expand=True)

    # --- HEADER NAVIGATION CONFIGURATION ---
    
    nav_titles = [
        "About Me", 
        "Project Timeline", 
        "Matlab Achievements", 
        "Technical Blog", 
        "Mathematical Notation", 
        "Github Evidence"
    ]

    top_nav_buttons = [
        ft.TextButton(text=title, data=title, on_click=on_nav_click, style=ft.ButtonStyle(color=ft.colors.WHITE70)) 
        for title in nav_titles
    ]

    def open_drawer(e):
        page.drawer.open = True
        page.update()

    def on_drawer_change(e):
        selected_index = int(e.data)
        if 0 <= selected_index < len(nav_titles):
            switch_section(nav_titles[selected_index])
        page.drawer.open = False
        page.update()

    page.drawer = ft.NavigationDrawer(
        controls=[
            ft.Container(padding=15, content=ft.Text("Navigation Menu", size=20, weight=ft.FontWeight.BOLD)),
            ft.Divider(thickness=1, color=ft.colors.WHITE10),
            *[ft.NavigationDrawerDestination(label=title, icon=ft.icons.CHEVRON_RIGHT_ROUNDED) for title in nav_titles]
        ],
        on_change=on_drawer_change
    )

    header_bar = ft.Container(
        content=ft.Row([
            ft.Row([
                ft.CircleAvatar(content=ft.Text("GF", weight=ft.FontWeight.BOLD), bgcolor=ft.colors.BLUE_GREY_800),
                ft.Text("Gabriel Portfolio", size=18, weight=ft.FontWeight.BOLD)
            ], spacing=10),
            
            ft.Row([
                ft.Row(top_nav_buttons, spacing=5, scroll=ft.ScrollMode.ADAPTIVE),
                ft.VerticalDivider(width=10, color=ft.colors.WHITE10),
                ft.IconButton(icon=ft.icons.MENU_ROUNDED, icon_color=ft.colors.BLUE_400, on_click=open_drawer, tooltip="Open Navigation Drawer")
            ], spacing=10)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        padding=10,
        border=ft.border.only(bottom=ft.BorderSide(1, ft.colors.WHITE10))
    )

    # --- BASE APP LAYOUT FRAME ---
    display_canvas = ft.Column(controls=[view_about_me()], expand=True)
    
    content_container = ft.Container(
        content=display_canvas, 
        padding=15, 
        expand=True
    )

    page.add(
        header_bar,
        content_container
    )

# --- RUN CONFIGURATION TUNED FOR WEB ASSEMBLY DEPLOYMENT ---
if __name__ == "__main__":
    ft.app(
        target=main, 
        assets_dir="assets",
        web_renderer=ft.WebRenderer.HTML
    )
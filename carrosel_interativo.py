import flet as ft

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bfcolor = ft.colors.WHITE
    page.window_width = 550
    page.window_height = 500
    page.window_resizable = False
    page.title = 'Carrosel Interativo de Fotos'
    
    def move_backward(e):
        carousel.scroll_to(delta=-100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()

    def move_forward(e):
        carousel.scroll_to(delta=100, duration=300, curve=ft.AnimationCurve.DECELERATE)
        carousel.update()


    layout = ft.Container(
        content=ft.Column(
            controls=[
                carousel := ft.Row(
                    scroll=ft.ScrollMode.HIDDEN,
                    controls=[
                        ft.Image(
                            src=f'https://picsum.photos/250/300?{num}'
                        ) for num in range(10)
                    ]
                ),
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_LEFT, on_click=move_backward),
                        ft.IconButton(icon=ft.icons.KEYBOARD_ARROW_RIGHT, on_click=move_forward),
                    ]
                )
            ]
        )
    )
        
    
    

    page.add(layout)


if __name__ == '__main__':
    ft.app(target=main)
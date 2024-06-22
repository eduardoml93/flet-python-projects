#
import flet as ft
import asyncio

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.colors.BLACK
    page.title = "Animar elementos"

    async def animate(e = None):
        while True:
            img.offset.y = -0.3
            img.scale.scale = 1.2
            img.update()
            await asyncio.sleep(4)

            img.offset.y = 0
            img.scale.scale = 1
            img.update()
            await asyncio.sleep(4)

    img = ft.Image(
        src = 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8911a890-1488-4033-b210-287b6a9c5319/df3bxu0-0c23950d-2e9a-4bb4-8d9a-802938fa5e87.png/v1/fill/w_1192,h_670/doctor_strange_portal___png_by_dhv123_df3bxu0-pre.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTA4MCIsInBhdGgiOiJcL2ZcLzg5MTFhODkwLTE0ODgtNDAzMy1iMjEwLTI4N2I2YTljNTMxOVwvZGYzYnh1MC0wYzIzOTUwZC0yZTlhLTRiYjQtOGQ5YS04MDI5MzhmYTVlODcucG5nIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.q1CndPi2_ruQm6CmOf9ycejSRRl84PSKg-mknRVLQlc',
        offset=ft.Offset(x=0, y=0),
        scale=ft.Scale(scale=1),
        animate_offset=ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
        animate_scale=ft.Animation(duration=4000, curve=ft.AnimationCurve.EASE),
    )
    page.add(img)
    page.run_task(animate)


if __name__ == "__main__":
    ft.app(target=main)
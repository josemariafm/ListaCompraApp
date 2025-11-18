import flet as ft

def main(page: ft.Page):
    # --- CONFIGURACIÓN DE LA APP ---
    page.title = "Lista de la Compra"
    page.theme_mode = ft.ThemeMode.SYSTEM 
    page.vertical_alignment = ft.MainAxisAlignment.START
    
    # Dimensiones para probar en PC como si fuera móvil
    page.window_width = 380
    page.window_height = 700

    # --- DATOS Y LÓGICA ---
    def cargar_datos():
        if page.client_storage.contains_key("lista_compra"):
            return page.client_storage.get("lista_compra")
        return []

    def guardar_datos():
        lista_texto = []
        for control in lista_visual.controls:
            if isinstance(control, ft.Checkbox):
                lista_texto.append(control.label)
        page.client_storage.set("lista_compra", lista_texto)

    # --- INTERFAZ VISUAL ---
    entrada = ft.TextField(
        hint_text="¿Qué necesitas comprar?", 
        expand=True, 
        on_submit=lambda e: agregar(None)
    )

    lista_visual = ft.Column()

    def agregar(e):
        if entrada.value:
            chk = ft.Checkbox(label=entrada.value, value=False)
            lista_visual.controls.append(chk)
            entrada.value = ""
            guardar_datos()
            page.update()
            entrada.focus()

    def borrar_marcados(e):
        nuevos_controles = [chk for chk in lista_visual.controls if not chk.value]
        lista_visual.controls.clear()
        lista_visual.controls.extend(nuevos_controles)
        guardar_datos()
        page.update()

    # --- CARGA INICIAL ---
    datos_guardados = cargar_datos()
    if datos_guardados:
        for producto in datos_guardados:
            lista_visual.controls.append(ft.Checkbox(label=producto, value=False))

    # --- MONTAJE DE LA PANTALLA ---
    
    fila_entrada = ft.Row(
        controls=[
            entrada,
            # CORRECCIÓN AQUÍ: ft.Icons (con mayúscula)
            ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=agregar)
        ]
    )

    btn_borrar = ft.ElevatedButton(
        "Borrar Marcados", 
        # CORRECCIÓN AQUÍ: ft.Icons (con mayúscula)
        icon=ft.Icons.DELETE_SWEEP, 
        color="white", 
        bgcolor="red",
        on_click=borrar_marcados
    )

    page.add(
        ft.Text("Mi Lista 🛒", size=30, weight="bold"),
        fila_entrada,
        ft.Divider(),
        lista_visual,
        ft.Divider(),
        ft.Container(content=btn_borrar, alignment=ft.alignment.center)
    )

# Ejecutar
#ft.app(target=main)
ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
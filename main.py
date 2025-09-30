import flet as ft
import sqlite3
from datetime import datetime
import os


class DiarioPersonal:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Diario Personal"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window.width = 800
        self.page.window.height = 600
        self.page.window.resizable = True
        
        # Inicializar base de datos
        self.init_database()
        
        # Componentes de UI
        self.entrada_texto = ft.TextField(
            label="Escribe tu entrada del diario...",
            multiline=True,
            min_lines=5,
            max_lines=10,
            expand=True
        )
        
        self.lista_entradas = ft.ListView(
            expand=True,
            spacing=10,
            padding=ft.padding.all(10)
        )
        
        # Construir interfaz
        self.build()
        self.cargar_entradas()
    
    def init_database(self):
        """Inicializar la base de datos SQLite"""
        self.db_path = "diario.db"
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS entradas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_hora TEXT NOT NULL,
                contenido TEXT NOT NULL
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def guardar_entrada(self, e):
        """Guardar nueva entrada en la base de datos"""
        contenido = self.entrada_texto.value.strip()
        
        if not contenido:
            self.mostrar_snackbar("Por favor, escribe algo antes de guardar.")
            return
        
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO entradas (fecha_hora, contenido) VALUES (?, ?)",
            (fecha_hora, contenido)
        )
        
        conn.commit()
        conn.close()
        
        # Limpiar campo de texto
        self.entrada_texto.value = ""
        self.entrada_texto.update()
        
        # Recargar entradas
        self.cargar_entradas()
        
        self.mostrar_snackbar("Entrada guardada correctamente.")
    
    def cargar_entradas(self):
        """Cargar todas las entradas desde la base de datos"""
        self.lista_entradas.controls.clear()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM entradas ORDER BY fecha_hora DESC")
        entradas = cursor.fetchall()
        
        conn.close()
        
        for entrada in entradas:
            id_entrada, fecha_hora, contenido = entrada
            
            # Crear tarjeta para cada entrada
            tarjeta = ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(
                                fecha_hora,
                                weight=ft.FontWeight.BOLD,
                                color=ft.colors.BLUE_600
                            ),
                            ft.IconButton(
                                icon=ft.icons.DELETE,
                                icon_color=ft.colors.RED,
                                tooltip="Eliminar entrada",
                                on_click=lambda e, entry_id=id_entrada: self.eliminar_entrada(entry_id)
                            )
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Text(
                            contenido,
                            selectable=True,
                            text_align=ft.TextAlign.JUSTIFY
                        )
                    ]),
                    padding=15
                ),
                margin=ft.margin.all(5)
            )
            
            self.lista_entradas.controls.append(tarjeta)
        
        self.lista_entradas.update()
    
    def eliminar_entrada(self, id_entrada):
        """Eliminar una entrada específica"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM entradas WHERE id = ?", (id_entrada,))
        
        conn.commit()
        conn.close()
        
        self.cargar_entradas()
        self.mostrar_snackbar("Entrada eliminada.")
    
    def mostrar_snackbar(self, mensaje):
        """Mostrar mensaje temporal"""
        snackbar = ft.SnackBar(
            content=ft.Text(mensaje),
            duration=3000
        )
        self.page.overlay.append(snackbar)
        snackbar.open = True
        self.page.update()
    
    def build(self):
        """Construir la interfaz de usuario"""
        # Botones de acción
        botones = ft.Row([
            ft.ElevatedButton(
                text="Guardar Entrada",
                icon=ft.icons.SAVE,
                on_click=self.guardar_entrada,
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.GREEN_600,
                    color=ft.colors.WHITE
                )
            ),
            ft.ElevatedButton(
                text="Limpiar",
                icon=ft.icons.CLEAR,
                on_click=lambda e: self.limpiar_campo(),
                style=ft.ButtonStyle(
                    bgcolor=ft.colors.ORANGE_600,
                    color=ft.colors.WHITE
                )
            )
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
        
        # Layout principal
        layout_principal = ft.Column([
            ft.Container(
                content=ft.Text(
                    "📖 Mi Diario Personal",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE_700
                ),
                alignment=ft.alignment.center,
                padding=ft.padding.all(20)
            ),
            
            # Sección para escribir nueva entrada
            ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Text(
                            "Nueva Entrada",
                            size=18,
                            weight=ft.FontWeight.BOLD
                        ),
                        self.entrada_texto,
                        botones
                    ], spacing=15),
                    padding=20
                ),
                margin=ft.margin.all(10)
            ),
            
            # Sección de entradas guardadas
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "Entradas Anteriores",
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=ft.colors.BLUE_700
                    ),
                    ft.Container(
                        content=self.lista_entradas,
                        height=300,
                        border=ft.border.all(1, ft.colors.GREY_400),
                        border_radius=10,
                        padding=5
                    )
                ], spacing=10),
                padding=ft.padding.symmetric(horizontal=10)
            )
        ], expand=True, spacing=5)
        
        self.page.add(layout_principal)
    
    def limpiar_campo(self):
        """Limpiar el campo de texto"""
        self.entrada_texto.value = ""
        self.entrada_texto.update()
        self.mostrar_snackbar("Campo limpiado.")


def main(page: ft.Page):
    DiarioPersonal(page)


if __name__ == "__main__":
    ft.app(target=main)
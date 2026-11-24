import flet as ft

# Dados fictícios para montar a primeira interface.
PRODUCTS = [
    {"id": 1, "name": "Margherita", "description": "Muçarela, tomate, manjericão e molho da casa", "price": 39.90, "category": "Tradicionais", "emoji": "🍅"},
    {"id": 2, "name": "Calabresa", "description": "Calabresa, cebola e muçarela", "price": 42.90, "category": "Tradicionais", "emoji": "🍕"},
    {"id": 3, "name": "Quatro Queijos", "description": "Muçarela, parmesão, provolone e gorgonzola", "price": 49.90, "category": "Especiais", "emoji": "🧀"},
    {"id": 4, "name": "Chocolate", "description": "Chocolate cremoso e granulado", "price": 34.90, "category": "Doces", "emoji": "🍫"},
    {"id": 5, "name": "Refrigerante 2L", "description": "Consulte os sabores disponíveis", "price": 12.00, "category": "Bebidas", "emoji": "🥤"},
]
CATEGORIES = ["Todas", "Tradicionais", "Especiais", "Doces", "Bebidas"]

def money(value: float) -> str:
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main(page: ft.Page):
    page.title = "Minha Pizzaria"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#F7F5F2"
    page.padding = 0
    page.window_min_width = 360
    page.window_min_height = 640

    cart = {}
    selected_category = "Todas"
    content = ft.Column(expand=True, spacing=18, scroll=ft.ScrollMode.AUTO)

    cart_badge = ft.Text("0 itens", color="#FFFFFF", size=12, weight=ft.FontWeight.BOLD)
    cart_total = ft.Text("R$ 0,00", color="#FFFFFF", size=14, weight=ft.FontWeight.BOLD)

    def cart_summary():
        count = sum(cart.values())
        total = sum(next(p["price"] for p in PRODUCTS if p["id"] == pid) * qty for pid, qty in cart.items())
        cart_badge.value = f"{count} {'item' if count == 1 else 'itens'}"
        cart_total.value = money(total)
        page.update()

    def add_to_cart(product):
        cart[product["id"]] = cart.get(product["id"], 0) + 1
        cart_summary()
        page.open(ft.SnackBar(ft.Text(f'{product["name"]} adicionado ao carrinho')))

    def product_card(product):
        return ft.Container(
            bgcolor="#FFFFFF",
            border_radius=18,
            padding=14,
            content=ft.Row(
                [
                    ft.Container(
                        width=76, height=76, border_radius=14, bgcolor="#FFF0E6",
                        alignment=ft.Alignment.CENTER,
                        content=ft.Text(product["emoji"], size=34),
                    ),
                    ft.Column(
                        [
                            ft.Text(product["name"], size=16, weight=ft.FontWeight.BOLD, color="#24211F"),
                            ft.Text(product["description"], size=12, color="#77716B", max_lines=2),
                            ft.Text(money(product["price"]), size=15, weight=ft.FontWeight.BOLD, color="#C64B22"),
                        ],
                        expand=True, spacing=4,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.ADD_CIRCLE,
                        icon_color="#C64B22",
                        icon_size=30,
                        tooltip="Adicionar",
                        on_click=lambda e, p=product: add_to_cart(p),
                    ),
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        )

    def render_products():
        content.controls.clear()
        content.controls.append(
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text("Feita para matar sua fome.", size=23, weight=ft.FontWeight.BOLD, color="#24211F"),
                        ft.Text("Escolha seus favoritos e peça em poucos toques.", size=13, color="#77716B"),
                    ], spacing=4
                )
            )
        )
        filtered = PRODUCTS if selected_category == "Todas" else [p for p in PRODUCTS if p["category"] == selected_category]
        content.controls.extend(product_card(p) for p in filtered)
        page.update()

    def select_category(category):
        nonlocal selected_category
        selected_category = category
        render_products()

    category_row = ft.Row(
        [
            ft.OutlinedButton(
                content=ft.Text(category),
                on_click=lambda e, c=category: select_category(c),
                style=ft.ButtonStyle(
                    color="#C64B22",
                    side=ft.BorderSide(1, "#E8D5CB"),
                    shape=ft.RoundedRectangleBorder(radius=20),
                ),
            )
            for category in CATEGORIES
        ],
        scroll=ft.ScrollMode.AUTO,
        spacing=8,
    )

    def show_cart(e):
        if not cart:
            page.open(ft.SnackBar(ft.Text("Seu carrinho ainda está vazio.")))
            return
        lines = []
        total = 0
        for pid, qty in cart.items():
            product = next(p for p in PRODUCTS if p["id"] == pid)
            subtotal = product["price"] * qty
            total += subtotal
            lines.append(ft.Text(f'{qty}x {product["name"]} — {money(subtotal)}'))
        dlg = ft.AlertDialog(
            modal=True,
            title=ft.Text("Seu pedido"),
            content=ft.Column(
                [*lines, ft.Divider(), ft.Text(f"Subtotal: {money(total)}", weight=ft.FontWeight.BOLD)],
                tight=True,
                width=320,
                spacing=10,
            ),
            actions=[ft.TextButton("Continuar comprando", on_click=lambda ev: page.close(dlg))],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(dlg)

    header = ft.Container(
        bgcolor="#24211F",
        padding=ft.Padding.symmetric(horizontal=20, vertical=18),
        content=ft.Row(
            [
                ft.Row(
                    [
                        ft.Container(
                            width=42, height=42, bgcolor="#C64B22", border_radius=13,
                            alignment=ft.Alignment.CENTER, content=ft.Text("🍕", size=24),
                        ),
                        ft.Column(
                            [
                                ft.Text("MINHA PIZZARIA", size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF"),
                                ft.Text("Sabor que chega até você", size=11, color="#D8C9C1"),
                            ], spacing=1
                        ),
                    ], spacing=10
                ),
                ft.Container(expand=True),
                ft.FilledButton(
                    content=ft.Row([ft.Icon(ft.Icons.SHOPPING_BAG_OUTLINED, size=17), cart_badge, cart_total], spacing=6),
                    on_click=show_cart,
                    style=ft.ButtonStyle(bgcolor="#C64B22", color="#FFFFFF", shape=ft.RoundedRectangleBorder(radius=12)),
                ),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    hero = ft.Container(
        margin=ft.Margin.only(left=16, right=16, top=16),
        padding=20,
        border_radius=20,
        bgcolor="#F2D7C8",
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("HOJE É DIA DE PIZZA!", size=11, weight=ft.FontWeight.BOLD, color="#8E3519"),
                        ft.Text("Seu momento\nmais gostoso.", size=25, weight=ft.FontWeight.BOLD, color="#38251E"),
                        ft.Text("Cardápio demonstrativo", size=12, color="#76584B"),
                    ], spacing=5, expand=True
                ),
                ft.Text("🍕", size=66),
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    page.add(
        ft.Column(
            [
                header,
                hero,
                ft.Container(
                    padding=ft.Padding.only(left=16, right=16, top=8),
                    content=ft.Column(
                        [
                            ft.Text("Explore nosso cardápio", size=18, weight=ft.FontWeight.BOLD, color="#24211F"),
                            category_row,
                            content,
                        ],
                        spacing=14,
                    ),
                    expand=True,
                ),
            ],
            expand=True,
            spacing=0,
        )
    )
    render_products()

ft.run(main)

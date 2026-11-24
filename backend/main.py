import json
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db
from .models import Order, Product
from .schemas import OrderCreate

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Minha Pizzaria API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok", "service": "minha-pizzaria-api"}

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.active == 1).all()

@app.post("/products/demo")
def seed_demo_products(db: Session = Depends(get_db)):
    if db.query(Product).count() > 0:
        return {"message": "Produtos já cadastrados."}
    demo = [
        Product(name="Margherita", description="Muçarela, tomate e manjericão", price=39.90, category="Tradicionais"),
        Product(name="Calabresa", description="Calabresa, cebola e muçarela", price=42.90, category="Tradicionais"),
        Product(name="Quatro Queijos", description="Quatro queijos selecionados", price=49.90, category="Especiais"),
    ]
    db.add_all(demo)
    db.commit()
    return {"message": f"{len(demo)} produtos demonstrativos cadastrados."}

@app.post("/orders", status_code=201)
def create_order(payload: OrderCreate, db: Session = Depends(get_db)):
    # O preço é sempre calculado no servidor, nunca confiando no valor enviado pelo app.
    items = []
    total = 0.0
    for item in payload.items:
        product = db.query(Product).filter(Product.id == item.product_id, Product.active == 1).first()
        if not product:
            raise HTTPException(status_code=404, detail=f"Produto {item.product_id} não encontrado.")
        subtotal = round(product.price * item.quantity, 2)
        total += subtotal
        items.append({
            "product_id": product.id,
            "name": product.name,
            "quantity": item.quantity,
            "unit_price": product.price,
            "subtotal": subtotal,
        })
    order = Order(
        customer_name=payload.customer_name,
        customer_phone=payload.customer_phone,
        delivery_address=payload.delivery_address,
        items_json=json.dumps(items, ensure_ascii=False),
        total=round(total, 2),
    )
    db.add(order)
    db.commit()
    db.refresh(order)
    return {
        "id": order.id,
        "total": order.total,
        "status": order.status,
        "payment_status": order.payment_status,
        "message": "Pedido criado. Pagamento ainda não foi iniciado.",
    }

@app.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    return db.query(Order).order_by(Order.id.desc()).limit(100).all()

from fastapi import FastAPI,HTTPException

app = FastAPI()

@app.get("/health")
def health():
    return {"message":"OK"}

@app.post("/phones")

@app.post("/phones", status_code=201)
def create_phone(phone: Phone):
    phones_db.append(phone)
    return phone

@app.get("/phones")
def get_phones():
    return phones_db

@app.get("/phones/{id}")
def get_phone_by_id(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    raise HTTPException(status_code=404, detail="Identifiant introuvable")


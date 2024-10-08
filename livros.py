from pydantic import BaseModel
from typing import Optional

class Livro(BaseModel):
    id: Optional[int]
    título: str
    autor: str


livros = [
    Livro(id=1, título='O Senhor dos Anéis - A Sociedade do Anel', autor='J.R.R Tolkien'),
    Livro(id=2, título='Harry Potter e a Pedra Filosofal', autor='J.K Rowling'),
    Livro(id=3, título='Hábitos Atômicos', autor='James Clear')
]
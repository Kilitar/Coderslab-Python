from pydantic import BaseModel, Field
from typing import List, Optional

# Tato třída demonstruje Pydantic (analogie k TS interface/class s validací)
class CourseModule(BaseModel):
    id: int
    title: str
    completed: bool = False
    tags: List[str] = Field(default_factory=list)

def process_module(module: CourseModule) -> str:
    # Zde VS Code díky tvému novému nastavení (Strict) bude hlídat typy.
    # Zkus smazat "-> str" nebo změnit návratovou hodnotu na číslo a uvidíš chybu.
    status = "DONE" if module.completed else "TODO"
    return f"Module {module.title}: [{status}]"

# Ukázka inicializace
if __name__ == "__main__":
    m = CourseModule(id=1, title="Introduction to Python", tags=["basics", "syntax"])
    print(process_module(m))
    
    # Zkus sem napsat: process_module(123) 
    # Editor ti to okamžitě podtrhne červeně, protože čeká CourseModule.

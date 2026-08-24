from dataclasses import dataclass, field
 
 
@dataclass
class Aprendiz:
    nombre: str
    programa_formacion: str
    habilidades: list[str] = field(default_factory=list)
 
 
@dataclass
class Vacante:
    titulo: str
    empresa: str
    programa_relacionado: str
    habilidades_requeridas: list[str] = field(default_factory=list)
 
 
def calcular_compatibilidad(aprendiz: Aprendiz, vacante: Vacante) -> float:
    """Devuelve un puntaje de compatibilidad entre 0 y 100."""
 
    # Peso 1: coincidencia de programa de formacion (40%)
    puntaje_programa = 40.0 if aprendiz.programa_formacion == vacante.programa_relacionado else 0.0
 
    # Peso 2: porcentaje de habilidades requeridas que el aprendiz posee (60%)
    habilidades_aprendiz = {h.lower().strip() for h in aprendiz.habilidades}
    requeridas = [h.lower().strip() for h in vacante.habilidades_requeridas]
 
    if requeridas:
        coincidencias = sum(1 for h in requeridas if h in habilidades_aprendiz)
        puntaje_habilidades = (coincidencias / len(requeridas)) * 60.0
    else:
        puntaje_habilidades = 0.0
 
    return round(puntaje_programa + puntaje_habilidades, 1)
 
 
def buscar_vacantes_compatibles(aprendiz: Aprendiz, vacantes: list[Vacante], umbral_minimo: float = 40.0):
    """
    Recorre las vacantes, calcula compatibilidad con el aprendiz,
    filtra por un umbral minimo y devuelve la lista ordenada de
    mayor a menor compatibilidad. Esta es la logica detras de
    RF-06 (Buscar vacantes) en la matriz de requisitos.
    """
    resultados = []
    for vacante in vacantes:
        score = calcular_compatibilidad(aprendiz, vacante)
        if score >= umbral_minimo:
            resultados.append((vacante, score))
 
    resultados.sort(key=lambda par: par[1], reverse=True)
    return resultados
 
 
if __name__ == "__main__":
    aprendiz = Aprendiz(
        nombre="Juan Diaz",
        programa_formacion="Analisis y Desarrollo de Software",
        habilidades=["python", "sql", "html", "css", "git"],
    )
 
    vacantes = [
        Vacante(
            titulo="Auxiliar de desarrollo backend",
            empresa="TechSoluciones SAS",
            programa_relacionado="Analisis y Desarrollo de Software",
            habilidades_requeridas=["python", "sql", "docker"],
        ),
        Vacante(
            titulo="Practicante de soporte de redes",
            empresa="RedesCol",
            programa_relacionado="Redes y Telecomunicaciones",
            habilidades_requeridas=["cisco", "linux"],
        ),
        Vacante(
            titulo="Aprendiz frontend",
            empresa="Interfaz Digital",
            programa_relacionado="Analisis y Desarrollo de Software",
            habilidades_requeridas=["html", "css", "git"],
        ),
    ]
 
    print(f"Vacantes compatibles para {aprendiz.nombre}:\n")
    resultados = buscar_vacantes_compatibles(aprendiz, vacantes)
 
    if not resultados:
        print("No se encontraron vacantes por encima del umbral minimo.")
 
    for vacante, score in resultados:
        print(f"- {vacante.titulo} ({vacante.empresa}): {score}% de compatibilidad")
        
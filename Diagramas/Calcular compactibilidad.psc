Algoritmo CalcularCompatibilidad
	Definir programaAprendiz, programaVacante Como Cadena
    Definir puntajePrograma, puntajeHabilidades, puntajeTotal Como Real
    Definir totalRequeridas, totalAprendiz, coincidencias, i, j Como Entero
    Dimension habilidadesAprendiz[10]
    Dimension habilidadesRequeridas[10]
	
    Leer programaAprendiz
    Leer programaVacante
    Leer totalAprendiz
    Para i <- 1 Hasta totalAprendiz Hacer
        Leer habilidadesAprendiz[i]
    FinPara
    Leer totalRequeridas
    Para i <- 1 Hasta totalRequeridas Hacer
        Leer habilidadesRequeridas[i]
    FinPara
	
    // Peso 1: coincidencia de programa de formación (40%)
    Si programaAprendiz = programaVacante Entonces
        puntajePrograma <- 40
    SiNo
        puntajePrograma <- 0
    FinSi
	
    // Peso 2: coincidencia de habilidades requeridas (60%)
    coincidencias <- 0
    Para i <- 1 Hasta totalRequeridas Hacer
        Para j <- 1 Hasta totalAprendiz Hacer
            Si habilidadesRequeridas[i] = habilidadesAprendiz[j] Entonces
                coincidencias <- coincidencias + 1
            FinSi
        FinPara
    FinPara
	
    Si totalRequeridas > 0 Entonces
        puntajeHabilidades <- (coincidencias / totalRequeridas) * 60
    SiNo
        puntajeHabilidades <- 0
    FinSi
	
    puntajeTotal <- puntajePrograma + puntajeHabilidades
	
    Escribir "Compatibilidad: ", puntajeTotal, "%"
FinAlgoritmo

def interes_compuesto(capital_inicial, tiempo_de_inversion, porcentaje_de_rentabilidad):
    #tu codigo
    final = capital_inicial
    for _ in range(tiempo_de_inversion):
        final += (final * porcentaje_de_rentabilidad) / 100
    return final

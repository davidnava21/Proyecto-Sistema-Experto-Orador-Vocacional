class SistemaExpertoPC:
    def __init__(self):
        self.hechos = {}
        self.reglas = []
        self.conclusiones = {}
        self.traza = []

    def definir_reglas(self):
        self.reglas = [
            # --- reglas somplejas (alta Certeza) ---
            {'id': 1, 'premisas': [('gusta_matematicas', True), ('gusta_fisica', True)], 'conclusion': 'Ingenieria', 'certeza': 0.90},
            {'id': 2, 'premisas': [('gusta_arte', True), ('es_creativo', True)], 'conclusion': 'Diseno_Grafico', 'certeza': 0.85},
            {'id': 3, 'premisas': [('gusta_biologia', True), ('ayudar_personas', True)], 'conclusion': 'Medicina_o_Enfermeria', 'certeza': 0.95},
            {'id': 4, 'premisas': [('gusta_computadoras', True), ('gusta_logica', True)], 'conclusion': 'Desarrollo_Software', 'certeza': 0.90},
            {'id': 5, 'premisas': [('gusta_escribir', True), ('gusta_leer', True)], 'conclusion': 'Periodismo_o_Literatura', 'certeza': 0.80},
            {'id': 6, 'premisas': [('gusta_dinero', True), ('liderazgo', True)], 'conclusion': 'Administracion_Empresas', 'certeza': 0.75},
            {'id': 7, 'premisas': [('Desarrollo_Software', True), ('es_creativo', True)], 'conclusion': 'Desarrollo_Videojuegos', 'certeza': 0.85},
            
            # --- reglas simples (certeza media/baja para cubrir huecos) ---
            {'id': 8, 'premisas': [('gusta_matematicas', True)], 'conclusion': 'Contabilidad_o_Estadistica', 'certeza': 0.60},
            {'id': 9, 'premisas': [('gusta_fisica', True)], 'conclusion': 'Tecnico_Mecanico', 'certeza': 0.60},
            {'id': 10, 'premisas': [('gusta_arte', True)], 'conclusion': 'Historia_del_Arte', 'certeza': 0.60},
            {'id': 11, 'premisas': [('es_creativo', True)], 'conclusion': 'Publicidad_y_Marketing', 'certeza': 0.55},
            {'id': 12, 'premisas': [('gusta_biologia', True)], 'conclusion': 'Veterinaria_o_Ecologia', 'certeza': 0.60},
            {'id': 13, 'premisas': [('ayudar_personas', True)], 'conclusion': 'Trabajo_Social_o_Psicologia', 'certeza': 0.60},
            {'id': 14, 'premisas': [('gusta_computadoras', True)], 'conclusion': 'Soporte_Tecnico_TI', 'certeza': 0.60},
            {'id': 15, 'premisas': [('gusta_logica', True)], 'conclusion': 'Filosofia_o_Derecho', 'certeza': 0.55},
            {'id': 16, 'premisas': [('gusta_escribir', True)], 'conclusion': 'Comunicacion_Social', 'certeza': 0.60},
            {'id': 17, 'premisas': [('gusta_leer', True)], 'conclusion': 'Biblioteconomia_o_Edicion', 'certeza': 0.55},
            {'id': 18, 'premisas': [('gusta_dinero', True)], 'conclusion': 'Ventas_y_Comercio', 'certeza': 0.50},
            {'id': 19, 'premisas': [('liderazgo', True)], 'conclusion': 'Recursos_Humanos_o_Politica', 'certeza': 0.60}
        ]

    def obtener_sintomas(self):
        print("\n" + "="*50)
        print("Sistema Experto: Orientador Vocacional")
        print("="*50)
        print("\nResponda 's' (sí) o 'n' (no) a las siguientes preguntas sobre sus intereses.")
        
        sintomas_posibles = {
            'gusta_matematicas': "¿Te gustan las matemáticas y resolver problemas numéricos?",
            'gusta_fisica': "¿Te interesa cómo funciona el mundo físico (física)?",
            'gusta_arte': "¿Disfrutas dibujando, pintando o creando arte visual?",
            'es_creativo': "¿Te consideras una persona creativa?",
            'gusta_biologia': "¿Te interesa el cuerpo humano y la biología?",
            'ayudar_personas': "¿Sientes vocación por ayudar directamente a otras personas?",
            'gusta_computadoras': "¿Te pasas el día en el ordenador y te da curiosidad cómo funciona?",
            'gusta_logica': "¿Te gustan los acertijos lógicos y el pensamiento estructurado?",
            'gusta_escribir': "¿Disfrutas escribiendo historias o ensayos?",
            'gusta_leer': "¿Lees libros con frecuencia por placer?",
            'gusta_dinero': "¿Te motiva mucho el mundo de las finanzas y el dinero?",
            'liderazgo': "¿Te gusta dirigir equipos o tomar decisiones importantes?"
        }
        for sintoma, pregunta in sintomas_posibles.items():
            respuesta = input(f"{pregunta} (s/n): ").lower().strip()
            self.hechos[sintoma] = (respuesta == 's')

    def obtener_valor_hecho(self, nombre_hecho):
        if nombre_hecho in self.hechos:
            return self.hechos[nombre_hecho], 1.0
        if nombre_hecho in self.conclusiones:
            return True, self.conclusiones[nombre_hecho]
        return False, 0.0

    def motor_inferencia(self):
        cambio = True
        while cambio:
            cambio = False
            for regla in self.reglas:
                if regla['conclusion'] in self.conclusiones:
                    continue
                premisas_cumplidas = True
                certeza_minima = 1.0
                detalles_premisas = []
                for nombre, valor_esperado in regla['premisas']:
                    valor_real, certeza_hecho = self.obtener_valor_hecho(nombre)
                    if valor_esperado == True and valor_real == True:
                        detalles_premisas.append(f"{nombre}={valor_real}")
                        certeza_minima = min(certeza_minima, certeza_hecho)
                    elif valor_esperado == False and valor_real == False:
                        detalles_premisas.append(f"{nombre}={valor_real}")
                    else:
                        premisas_cumplidas = False
                        break
                if premisas_cumplidas:
                    certeza_final = regla['certeza'] * certeza_minima
                    self.conclusiones[regla['conclusion']] = certeza_final
                    self.traza.append({'regla': regla['id'], 'conclusion': regla['conclusion'], 'certeza': certeza_final, 'premisas': detalles_premisas})
                    cambio = True

    def mostrar_resultados(self):
        print("\n" + "="*50)
        print("Resultados del Diagnóstico")
        print("="*50)
        print("\n Conclusiones")
        if not self.conclusiones:
            print("No se pudo llegar a ningún diagnóstico!!!")
        else:
            for concl, certeza in self.conclusiones.items():
                porcentaje = round(certeza * 100, 2)
                print(f"{concl.replace('_', ' ')} ({porcentaje}% confianza)")
        print("\n Trazabilidad de Inferencia ")
        for paso in self.traza:
            print(f"\nRegla #{paso['regla']} activada:")
            print(f"  Conclusion: {paso['conclusion']}")
            print(f"  Premisas: {', '.join(paso['premisas'])}")
            print(f"  Calculo: {paso['certeza']:.2f} de certeza final")

if __name__ == "__main__":
    se = SistemaExpertoPC()
    se.definir_reglas()
    se.obtener_sintomas()
    se.motor_inferencia()
    se.mostrar_resultados()
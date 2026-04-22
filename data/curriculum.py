"""
🍫 Dualita Curriculum — Formación Dual Chocolatería de Autor
Modelo de 18 sesiones sincrónicas y asincrónicas.
"""

SECTIONS = [
    {
        "title": "Cata Sensorial y Perfilación",
        "emoji": "👅",
        "mooc": {
            "intro": "Domina el arte de evaluar el chocolate como un experto. En este módulo, aprenderás a decodificar los sabores del cacao desde el origen hasta el paladar.",
            "recipe_url": "/recipes/guia_cata_profesional.pdf",
            "schedule": [
                {"period": "Mes 1: Fundamentos", "morning": "08:00 - 12:00 (Teoría de Sentidos)", "afternoon": "14:00 - 18:00 (Práctica de Cata)"},
                {"period": "Mes 2: Perfilación", "morning": "08:00 - 12:00 (Rueda de Sabores)", "afternoon": "14:00 - 18:00 (Identificación de Origen)"}
            ],
            "steps": [
                "Preparación: Limpieza de paladar con agua tibia y manzana verde.",
                "Análisis Visual: Evaluación de brillo, color y ausencia de defectos superficiales.",
                "Análisis Auditivo: Verificación del 'snap' limpio al partir la tableta.",
                "Fase Olfativa: Identificación de aromas primarios y secundarios.",
                "Degustación: Fusión lenta en boca y registro del retrogusto."
            ]
        },
        "lessons": [
            {
                "title": "Introducción a los Sentidos",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es el primer sentido que usamos al catar chocolate?", "options": ["Gusto", "Olfato", "Vista", "Oído"], "answer": 2, "explanation": "La vista es el primer paso: evaluamos el color, brillo y si hay defectos como el bloom."},
                    {"type": "tf", "q": "El 'snap' (sonido al partir) indica un buen temperado.", "answer": True, "explanation": "Un buen snap, limpio y seco, es señal de que los cristales de manteca de cacao están estables (Forma V)."},
                    {"type": "choice", "q": "¿Cómo se llama la fase final del sabor en la cata?", "options": ["Ataque", "Evolución", "Retrogusto", "Fusión"], "answer": 2, "explanation": "El retrogusto es el sabor persistente que queda en boca después de tragar el chocolate."},
                ]
            },
            {
                "title": "Rueda de Sabores",
                "questions": [
                    {"type": "choice", "q": "¿Qué grupo de sabores NO es típico en el cacao de origen?", "options": ["Frutos Rojos", "Plástico", "Nueces", "Especias"], "answer": 1, "explanation": "Notas a plástico o goma quemada son defectos graves de fermentación o secado artificial."},
                    {"type": "tf", "q": "La acidez frutal es deseable en cacaos finos de aroma.", "answer": True, "explanation": "Una acidez balanceada, como a cítricos o frutos rojos, aporta brillantez y complejidad al chocolate."},
                    {"type": "choice", "q": "¿Qué nota aromática se relaciona con la familia Forastero?", "options": ["Frutal intenso", "Floral delicado", "Cacao fuerte y terroso", "Especias dulces"], "answer": 2, "explanation": "Los cacaos bulk (Forastero) suelen tener un sabor a 'cacao base' fuerte, terroso o astringente."},
                ]
            },
            {
                "title": "Técnica Profesional",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es la temperatura ideal del salón para catar?", "options": ["10-12°C", "20-22°C", "28-30°C", "35°C"], "answer": 1, "explanation": "Una temperatura ambiente de 20-22°C permite que el chocolate no esté ni muy duro ni derretido."},
                    {"type": "tf", "q": "Se debe masticar el chocolate inmediatamente.", "answer": False, "explanation": "El chocolate debe dejarse fundir en el paladar para liberar todos sus compuestos aromáticos volátiles."},
                    {"type": "choice", "q": "¿Qué limpiador de paladar se recomienda entre catas?", "options": ["Café fuerte", "Agua tibia o manzana", "Leche entera", "Chocolate blanco"], "answer": 1, "explanation": "Agua tibia o trozos de manzana verde o galletas neutras limpian la grasa sin alterar las papilas."},
                ]
            },
        ]
    },
    {
        "title": "Formulación y Porcentajes",
        "emoji": "📊",
        "mooc": {
            "intro": "La ciencia exacta detrás de la barra perfecta. Aprende a calcular porcentajes de cacao, manteca y azúcar para crear fórmulas de autor equilibradas.",
            "recipe_url": "/recipes/manual_formulacion_dualita.pdf",
            "schedule": [
                {"period": "Mes 1: Matemáticas", "morning": "08:00 - 12:00 (Cálculo de Fórmulas)", "afternoon": "14:00 - 18:00 (Manejo de Porcentajes)"},
                {"period": "Mes 2: Aplicación", "morning": "08:00 - 12:00 (Formulación de Blancos)", "afternoon": "14:00 - 18:00 (Formulación de Oscuros)"}
            ],
            "steps": [
                "Cálculo Base: Determinación de sólidos de cacao y manteca añadida.",
                "Equilibrio de Dulzor: Ajuste de azúcar según el perfil del grano.",
                "Refinado: Tiempo y presión ideal para alcanzar micras óptimas.",
                "Conchado: Desarrollo de sabor y eliminación de ácidos volátiles.",
                "Curva de Temperado: Preparación de la cristalización beta."
            ]
        },
        "lessons": [
            {
                "title": "Matemáticas del Chocolate",
                "questions": [
                    {"type": "choice", "q": "¿Qué significa que un chocolate sea 70% cacao?", "options": ["Tiene 70% licor de cacao puro", "Tiene 70% de grasa", "Contiene 70% de sólidos de cacao (licor + manteca añadida)", "Es 70% azúcar"], "answer": 2, "explanation": "El porcentaje incluye todos los derivados del cacao: licor de cacao + manteca de cacao añadida."},
                    {"type": "tf", "q": "Dos chocolates del 70% pueden tener niveles de azúcar diferentes.", "answer": False, "explanation": "Si es 70% sólidos de cacao, el 30% restante suele ser azúcar (o leche). La cantidad de azúcar es fija en un 30% en chocolates oscuros estándar."},
                    {"type": "choice", "q": "¿Qué ingrediente se usa como emulsionante común?", "options": ["Vainilla", "Lecitina de soya", "Sal", "Canela"], "answer": 1, "explanation": "La lecitina de soya o girasol reduce la viscosidad del chocolate usando menos manteca de cacao."},
                ]
            },
            {
                "title": "Chocolates Oscuros",
                "questions": [
                    {"type": "choice", "q": "¿Qué aporta la manteca de cacao extra en una fórmula?", "options": ["Más dulzor", "Mayor fluidez y suavidad", "Más amargor", "Color más oscuro"], "answer": 1, "explanation": "Añadir manteca de cacao hace que el chocolate sea más fluido para coberturas y más suave en boca."},
                    {"type": "tf", "q": "Un chocolate 100% no contiene azúcar añadido.", "answer": True, "explanation": "Es pasta o licor de cacao puro, a veces con un pequeño porcentaje de manteca de cacao extra."},
                    {"type": "choice", "q": "¿Por qué un 85% es más difícil de formular que un 60%?", "options": ["Porque la manteca se separa", "Porque hay poco azúcar para enmascarar defectos del cacao", "Porque no se puede temperar", "Porque necesita mucha vainilla"], "answer": 1, "explanation": "Con 15% de azúcar, los defectos de astringencia o mala fermentación del cacao se notarán inmediatamente."},
                ]
            },
            {
                "title": "Chocolates Blancos y Leche",
                "questions": [
                    {"type": "choice", "q": "¿Qué diferencia legalmente al chocolate blanco?", "options": ["No tiene manteca de cacao", "No contiene sólidos de cacao no grasos (polvo oscuro)", "Lleva colorante blanco", "Solo usa leche condensada"], "answer": 1, "explanation": "El chocolate blanco está hecho de manteca de cacao, leche en polvo y azúcar. No lleva licor de cacao."},
                    {"type": "tf", "q": "El chocolate con leche requiere menos temperatura para fundirse que el oscuro.", "answer": True, "explanation": "La grasa butírica de la leche funde a menor temperatura y hace que el chocolate sea más sensible al calor."},
                    {"type": "choice", "q": "¿Qué proceso industrial es crítico en el chocolate con leche?", "options": ["Alcalinización", "Caramelización de la leche (reacción de Maillard)", "Fermentación láctica", "Secado al sol"], "answer": 1, "explanation": "Durante el conchado, la interacción entre proteínas de leche y azúcares crea notas acarameladas clave."},
                ]
            },
        ]
    },
    {
        "title": "Bombonería y Rellenos",
        "emoji": "🍬",
        "mooc": {
            "intro": "El arte del detalle. Descubre cómo crear casquillos perfectos, rellenos estables y emulsiones (ganaches) que sorprendan por su textura y brillo.",
            "recipe_url": "/recipes/recetario_bomboneria_fina.pdf",
            "schedule": [
                {"period": "Mes 1: Técnica de Casquillos", "morning": "08:00 - 12:00 (Encamisado de Moldes)", "afternoon": "14:00 - 18:00 (Cristalización Controlada)"},
                {"period": "Mes 2: Rellenos Avanzados", "morning": "08:00 - 12:00 (Emulsiones y Ganaches)", "afternoon": "14:00 - 18:00 (Pralinés y Giandujas)"}
            ],
            "steps": [
                "Limpieza de Moldes: Pulido con algodón para brillo espejo.",
                "Encamisado: Creación de casquillos finos y uniformes.",
                "Relleno (Piping): Dosificación precisa de ganaches a 28°C.",
                "Reposo: Estabilización del relleno por 12-24 horas.",
                "Sellado: Cierre de la base y desmolde por contracción térmica."
            ]
        },
        "lessons": [
            {
                "title": "Moldes y Casquillos",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es el grosor ideal de un casquillo de bombón?", "options": ["1-2 milímetros", "4-5 milímetros", "Tan grueso como sea posible", "1 centímetro"], "answer": 0, "explanation": "Un casquillo delgado y uniforme (1-2mm) asegura una mordida crujiente que da paso rápido al relleno."},
                    {"type": "tf", "q": "El molde de policarbonato debe lavarse con agua muy caliente después de cada uso.", "answer": False, "explanation": "No se recomienda lavar con agua frecuentemente. Si se tempera bien, el molde queda brillante y solo se limpia en seco."},
                    {"type": "choice", "q": "¿A qué temperatura debe estar el molde antes de encamisar?", "options": ["10°C (frío)", "20-22°C (ambiente cálido)", "40°C (caliente)", "Congelado"], "answer": 1, "explanation": "El molde debe estar entre 20-22°C. Si está frío provocará shock térmico y el chocolate no brillará."},
                ]
            },
            {
                "title": "Ganaches y Emulsiones",
                "questions": [
                    {"type": "choice", "q": "¿Qué es químicamente una ganache?", "options": ["Una solución de azúcar", "Una emulsión de grasa en agua", "Una mezcla de polvos", "Una cristalización"], "answer": 1, "explanation": "La ganache es una emulsión donde la manteca de cacao y grasa láctea se dispersan en el agua de la crema."},
                    {"type": "tf", "q": "La proporción 1:1 de crema y chocolate da un relleno muy firme para cortar.", "answer": False, "explanation": "1:1 da un relleno fluido o suave. Para cortar, se necesita más chocolate (ej. 2:1 o 3:1)."},
                    {"type": "choice", "q": "¿Qué ingrediente ayuda a evitar que la ganache se separe o corte?", "options": ["Sal", "Glucosa o azúcar invertido", "Más crema fría", "Agua hirviendo"], "answer": 1, "explanation": "Los azúcares invertidos o glucosa ayudan a estabilizar la emulsión, retienen humedad y bajan la Actividad de Agua (Aw)."},
                ]
            },
            {
                "title": "Pralinés y Sellado",
                "questions": [
                    {"type": "choice", "q": "¿Qué es un Praliné clásico?", "options": ["Chocolate con leche", "Pasta de frutos secos caramelizados finamente molida", "Crema de vainilla", "Masa de galleta cruda"], "answer": 1, "explanation": "El praliné se hace caramelizando almendras o avellanas, y luego refinándolas hasta obtener una pasta grasa lisa."},
                    {"type": "tf", "q": "Se debe rellenar el bombón hasta el tope del molde.", "answer": False, "explanation": "Se debe dejar 1-2 milímetros libres para poder sellar o 'tapar' el bombón con chocolate temperado."},
                    {"type": "choice", "q": "¿Por qué un bombón recién sellado se encoge ligeramente en la nevera?", "options": ["Porque el azúcar se cristaliza", "Porque la manteca de cacao se contrae al cristalizar", "Porque la humedad se evapora", "Es un defecto del molde"], "answer": 1, "explanation": "La Forma V de la manteca de cacao es más compacta, contrayéndose hasta un 2%, lo que permite el desmolde."},
                ]
            },
        ]
    },
    {
        "title": "Proyecto: Chocolate Dubai",
        "emoji": "🌟",
        "mooc": {
            "intro": "Lleva las tendencias a la realidad artesanal. Crea la famosa barra de pistacho y kataifi usando técnicas de autor para un resultado premium y viral.",
            "recipe_url": "/recipes/receta_chocolate_dubai.pdf",
            "schedule": [
                {"period": "Mes 1: Preparación", "morning": "08:00 - 12:00 (Tratamiento de Kataifi)", "afternoon": "14:00 - 18:00 (Elaboración de Pasta Pistacho)"},
                {"period": "Mes 2: Montaje", "morning": "08:00 - 12:00 (Vaciado de Barras Chunky)", "afternoon": "14:00 - 18:00 (Marketing y ASMR)"}
            ],
            "steps": [
                "Kataifi: Tostado de los fideos en mantequilla clarificada hasta dorado.",
                "Crema de Pistacho: Elaboración de praliné de pistacho al 100% con chocolate blanco.",
                "Mezcla Texturas: Combinación del kataifi frío con la crema para mantener crunch.",
                "Vaciado: Encamisado de moldes profundos (Chunky) con chocolate oscuro.",
                "Relleno y ASMR: Llenado generoso y sellado final."
            ]
        },
        "lessons": [
            {
                "title": "Análisis de Tendencia",
                "questions": [
                    {"type": "choice", "q": "¿Qué elementos caracterizan a la barra 'Dubai' viral?", "options": ["Chocolate blanco con oro", "Grosor extremo, relleno de pistacho y masa kataifi", "Forma de pirámide", "Colorante rosa y sal"], "answer": 1, "explanation": "El 'Dubai Chocolate' se viralizó por ser barras gruesas rellenas de crema de pistacho untuosa y masa kataifi crujiente."},
                    {"type": "tf", "q": "La masa Kataifi necesita ser tostada con mantequilla antes de incluirse.", "answer": True, "explanation": "La masa cruda absorbería humedad o no aportaría el crujiente esencial. Se tuesta con grasa para sellarla."},
                    {"type": "choice", "q": "¿Por qué este formato tuvo tanto éxito en RRSS?", "options": ["Por su bajo costo", "Por el ASMR del crunch y su atractivo visual exuberante", "Por ser un producto vegano", "Por tener licencias oficiales"], "answer": 1, "explanation": "El sonido al partir la barra (ASMR) y el relleno verde vibrante escurriendo crearon un fenómeno visual perfecto para TikTok/Instagram."},
                ]
            },
            {
                "title": "Producción y Costeo",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es el principal reto técnico en una barra con relleno denso y crujiente?", "options": ["Temperar el chocolate", "Evitar que la humedad del relleno ablande el kataifi", "Conseguir los moldes", "Pegar la etiqueta"], "answer": 1, "explanation": "El relleno de pistacho debe tener bajo contenido de agua (alta grasa) para que el kataifi no pierda su crunch en días posteriores."},
                    {"type": "tf", "q": "La pasta de pistacho pura suele ser económica para la producción en masa.", "answer": False, "explanation": "El pistacho de calidad es uno de los frutos secos más caros. Optimizar el % en la crema es clave para la rentabilidad."},
                    {"type": "choice", "q": "¿Qué grosor mínimo requiere un molde para estilo Dubai?", "options": ["5-8 milímetros", "1-1.5 centímetros (Tabletas profundas)", "1 metro", "Solo moldes de bombón tradicional"], "answer": 1, "explanation": "Requiere moldes tipo 'Chunky' (gruesos) de 1 a 2 cm de profundidad para alojar la gran cantidad de relleno."},
                ]
            },
            {
                "title": "Marketing de Autor",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es el mejor ángulo para promocionar barras rellenas en fotos?", "options": ["Cerradas en su caja", "Desde arriba a 2 metros", "Plano macro de la barra recién partida mostrando el interior (cross-section)", "Totalmente derretidas"], "answer": 2, "explanation": "El 'cross-section' o corte transversal es el rey en redes para mostrar abundancia y textura."},
                    {"type": "tf", "q": "Crear 'escasez artificial' o lanzamientos limitados (Drops) funciona en chocolates de tendencia.", "answer": True, "explanation": "El modelo de Drops genera sentido de urgencia y eleva el prestigio y demanda de los lotes artesanales."},
                    {"type": "choice", "q": "¿Cómo adaptar la tendencia a 'Chocolatería de Autor'?", "options": ["Copiar la receta exacta", "Usar pistachos artificiales", "Mezclar el concepto con cacaos finos locales e ingredientes autóctonos", "Bajar el precio al mínimo"], "answer": 2, "explanation": "La diferenciación viene de aplicar la tendencia usando el terroir local y calidad superior de mantecas y cacaos origen."},
                ]
            },
        ]
    },
    {
        "title": "Migao Evolucionado",
        "emoji": "☕",
        "mooc": {
            "intro": "Tradición y vanguardia en una taza. Aprende a formular chocolates de taza premium y a evolucionar el concepto cultural del 'Migao' con técnicas modernas.",
            "recipe_url": "/recipes/guia_migao_evolucionado.pdf",
            "schedule": [
                {"period": "Mes 1: El Origen de la Taza", "morning": "08:00 - 12:00 (Historia y Especias)", "afternoon": "14:00 - 18:00 (Molienda y Texturas)"},
                {"period": "Mes 2: Evolución Culinaria", "morning": "08:00 - 12:00 (Maridaje con Quesos)", "afternoon": "14:00 - 18:00 (Espumas y Aireados)"}
            ],
            "steps": [
                "Base de Taza: Molienda de licor de cacao con especias seleccionadas.",
                "Emulsión en Caliente: Batido vigoroso para generar espuma estable.",
                "Selección de Quesos: Maridaje de quesos maduros y frescos.",
                "Texturas: Preparación de colaciones (buñuelos, pandebono) de alta calidad.",
                "Servicio: Montaje por capas para la experiencia 'Evolución'."
            ]
        },
        "lessons": [
            {
                "title": "Historia y Cultura",
                "questions": [
                    {"type": "choice", "q": "¿Qué es tradicionalmente el 'Migao' en la cultura de chocolate caliente?", "options": ["Chocolate frío con menta", "Chocolate de taza espeso acompañado de pan/colaciones y queso picado", "Un tipo de bombón suizo", "Una trufa francesa"], "answer": 1, "explanation": "El migao es una preparación tradicional de hundir queso y carbohidratos en chocolate de taza caliente."},
                    {"type": "tf", "q": "El chocolate para taza tradicional suele ser bajo en grasa (manteca) y alto en azúcar.", "answer": True, "explanation": "Históricamente, la manteca se extraía para exportación y se dejaba polvo mezclado con mucho azúcar para mercado local."},
                    {"type": "choice", "q": "¿Qué aporta el quesito o queso fresco al chocolate caliente?", "options": ["Sabor a vainilla", "Contraste salado, grasa extra y textura chiclosa", "Lo vuelve más líquido", "Evita que se enfríe"], "answer": 1, "explanation": "El contraste dulce/salado y la textura hilada del queso derretido en el fondo es el atractivo principal del Migao."},
                ]
            },
            {
                "title": "Formulación de Taza",
                "questions": [
                    {"type": "choice", "q": "¿Qué especias son clásicas en un chocolate de taza latinoamericano?", "options": ["Azafrán y romero", "Canela, clavos y nuez moscada", "Curry y comino", "Menta y eucalipto"], "answer": 1, "explanation": "Las especias cálidas como canela y clavo han acompañado al chocolate desde la colonia."},
                    {"type": "tf", "q": "Para hacer un Migao Evolucionado, se usa cacao 100% en lugar de mezcla comercial.", "answer": True, "explanation": "Un producto de autor formula el chocolate usando licor de cacao premium, ajustando el azúcar a gusto."},
                    {"type": "choice", "q": "¿Qué espesante natural se usa históricamente en Centro/Suramérica?", "options": ["Gelatina", "Masa de maíz o fécula", "Algas marinas", "Huevo crudo"], "answer": 1, "explanation": "Las harinas o masas de maíz se han usado desde los aztecas para espesar y espumar las bebidas de cacao."},
                ]
            },
            {
                "title": "Texturas y Maridaje",
                "questions": [
                    {"type": "choice", "q": "¿Cómo se puede modernizar (evolucionar) el queso en el Migao?", "options": ["Usar queso azul fuerte", "Servirlo congelado", "Usar esferificaciones, emulsiones de queso o quesos maduros balanceados", "Quitar el queso"], "answer": 2, "explanation": "La evolución culinaria involucra aplicar técnicas modernas (espumas, emulsiones) o quesos de mayor perfil de sabor."},
                    {"type": "tf", "q": "El batido en molinillo o licuadora mejora la experiencia del chocolate de taza.", "answer": True, "explanation": "La aireación mecánica (espuma) es vital para la liberación de aromas y mejora la textura en boca."},
                    {"type": "choice", "q": "¿Qué 'colación' (acompañamiento) aporta mejor contraste textural?", "options": ["Puré", "Gomitas dulces", "Galletas crocantes, buñuelos o pandebono crujiente", "Sopa"], "answer": 2, "explanation": "El crujiente (crispiness) complementa la suavidad líquida del chocolate y la elasticidad del queso fundido."},
                ]
            },
        ]
    },
    {
        "title": "Empaques Sostenibles",
        "emoji": "📦",
        "mooc": {
            "intro": "El empaque es la cara de tu marca. Aprende a seleccionar materiales biodegradables que protejan tu chocolate y cuenten la historia de sostenibilidad de tu emprendimiento.",
            "recipe_url": "/recipes/manual_empaques_sostenibles.pdf",
            "schedule": [
                {"period": "Mes 1: Materiales", "morning": "08:00 - 12:00 (Fibras Naturales)", "afternoon": "14:00 - 18:00 (Certificaciones FSC)"},
                {"period": "Mes 2: Diseño de Marca", "morning": "08:00 - 12:00 (Estructura Isotérmica)", "afternoon": "14:00 - 18:00 (Etiquetado Nutricional)"}
            ],
            "steps": [
                "Análisis de Barrera: Prueba de permeabilidad de grasas y humedad.",
                "Estructura: Diseño de troqueles sin pegamentos tóxicos.",
                "Branding: Impresión con tintas vegetales sobre fibras de caña.",
                "Certificaciones: Obtención de sellos FSC y compostabilidad.",
                "Isotermia: Selección de gel pack y cajas para envío seguro."
            ]
        },
        "lessons": [
            {
                "title": "Materiales Biodegradables",
                "questions": [
                    {"type": "choice", "q": "¿Qué reemplazo ecológico existe para la bolsa de plástico interior?", "options": ["Papel aluminio grueso", "Bolsas de bioplástico compostable (PLA, celulosa)", "Cajas de metal", "Plástico PVC"], "answer": 1, "explanation": "Los bioplásticos derivados del maíz o películas de celulosa compostable protegen la humedad sin ser plástico fósil."},
                    {"type": "tf", "q": "Todo papel 'Kraft' o marrón es 100% ecológico y reciclado.", "answer": False, "explanation": "No siempre. A veces es papel virgen teñido. Hay que verificar certificaciones FSC y porcentajes de reciclado."},
                    {"type": "choice", "q": "¿Qué certificación garantiza manejo forestal responsable del cartón?", "options": ["FDA", "ISO 9001", "FSC (Forest Stewardship Council)", "Fairtrade"], "answer": 2, "explanation": "El sello FSC indica que el papel/cartón proviene de bosques manejados de manera sostenible."},
                ]
            },
            {
                "title": "Diseño y Protección",
                "questions": [
                    {"type": "choice", "q": "¿Cuál es el enemigo principal del chocolate en su empaque?", "options": ["Oxígeno", "Humedad y olores externos", "Gravedad", "Polvo"], "answer": 1, "explanation": "La manteca de cacao es altamente higroscópica (absorbe humedad) y lipofílica (absorbe olores fuertes del ambiente)."},
                    {"type": "tf", "q": "Una caja de cartón por sí sola sella 100% contra la humedad.", "answer": False, "explanation": "El cartón respira. Se requiere una barrera interna (como bioplástico o foil de aluminio) para evitar el bloom de azúcar."},
                    {"type": "choice", "q": "¿Qué es la 'temperatura de estrés' que el empaque debe mitigar en transporte?", "options": ["10°C", "20°C", "Encima de 30°C", "Menos de 0°C"], "answer": 2, "explanation": "Por encima de 30°C, el chocolate pierde el temperado o se funde. Empaques isotérmicos con gel frío ayudan a mitigar esto."},
                ]
            },
            {
                "title": "Etiquetado y Branding",
                "questions": [
                    {"type": "choice", "q": "¿Qué se entiende por 'Clean Label' (Etiqueta Limpia)?", "options": ["Una etiqueta blanca", "Lista de ingredientes corta, natural y fácil de entender", "Etiqueta sin calorías", "Etiqueta lavable"], "answer": 1, "explanation": "Un producto clean label evita aditivos artificiales y usa nombres de ingredientes reales (ej: Cacao, Azúcar, Manteca de cacao)."},
                    {"type": "tf", "q": "Tinta a base de soya o vegetales es preferible para empaques sostenibles.", "answer": True, "explanation": "Las tintas de petróleo dificultan el reciclaje/compostaje. Tintas vegetales son el estándar en empaques eco-amigables."},
                    {"type": "choice", "q": "¿Qué información añade más valor en un chocolate de autor?", "options": ["Código de barras gigante", "Fecha de caducidad en el frente", "Historia del origen del cacao, productor y notas de cata", "Historia de marca y sostenibilidad"], "answer": 2, "explanation": "El storytelling del origen conecta al consumidor con el producto, justificando el valor artesanal del chocolate."},
                ]
            },
        ]
    }
]

def get_section(idx):
    return SECTIONS[idx]

def get_lesson(section_idx, lesson_idx):
    return SECTIONS[section_idx]["lessons"][lesson_idx]

def get_questions(section_idx, lesson_idx):
    return SECTIONS[section_idx]["lessons"][lesson_idx]["questions"]

def total_sections():
    return len(SECTIONS)

def total_lessons(section_idx):
    return len(SECTIONS[section_idx]["lessons"])

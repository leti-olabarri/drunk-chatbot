# drunk-chatbot

Proyecto de Machine Learning para el bootcamp de CORE Code School.

## Resumen

Se ha entrenado un modelo gpt-2 para ver si era capaz de responder imitando la manera de hablar de su creadora.

## Datos

Los datos que se han utilizado para entrenar el modelo son conversaciones exportadas de Whatsapp. Por razones de privacidad, este archivo no se encuentra en el repositorio, pero tenía 55k líneas de texto, etiquetadas como [ME] cuando se trataba de mensajes míos, y como [OTHERS] cuando eran de otras personas.

## Modelo

El modelo utilizado es uno ya existente, hecho ad-hoc para generación de texto. Se llama [gpt-2](https://github.com/openai/gpt-2), y pertenece a [OpenAI](https://openai.com/). Este modelo se ha utilizado mucho con textos en inglés, pero había pocas pruebas con castellano. Encontré una de ellas en este [blog](https://planetachatbot.com/lo-que-aprendi-entrenando-al-primer-chatbot-gpt-2-en-espanol/), y decidí hacer una prueba personal.

El modelo se entrenó con el dataset arriba mencionado. El entrenamiento se completó en 18,5h, y el modelo resultante se puede descargar de [este link](https://drive.google.com/file/d/1HtE2MXuSD3fFhiKFlGMLOiNSu3SgIS3p/view?usp=sharing), con su correspondiente [checkpoint](https://drive.google.com/file/d/1VOgUCg4dpr9AnlsLt5WiAZg52M9BXEPp/view?usp=sharing).

## Resultados

Los resultados, con un único entrenamiento y ese dataset, son bastante mejorables. Dejo aquí un extracto de algo del texto generado al azar.

`[ME] 👍🏼👍🏼👍🏼👍🏼` 

`[ME] ¡Ánimo, Marta!` 

`[ME] ¿Estás en casa?`  

`[OTHERS] Ajajjajjajjajaj`  

`[OTHERS] Siii`  

`[OTHERS] Ya estoy`  

`[ME] Jajajajajajajaja`  

`[ME] Hoy estoy`  

`[ME] Marta, he ido a Misa en la farmacia, pero no me preocupen tener que ser en el grupo de secretaría`  

`[ME] Pero voy a intentar comprar una cerveza`  

`[ME] La verdad es que no me compraría ningún backlogado`  

`[ME] Marta, tengo que ir a comprarme unos días para la cerveza`  

`[OTHERS] 😂😂😂😂`  

`[OTHERS] Muy bien`  

`[OTHERS] Jajajajajajajaj`  

`[ME] 🤣🤣🤣🤣🤣🤣`  

`[OTHERS] Ya me he hecho unos días`  

`[OTHERS] Muy bien`  

`[ME] Ok`  

`[ME] ¿Cómo te encuentras?`  

`[OTHERS] En el grupo de secretaría`  

`[OTHERS] Pues eso te digo`  

`[ME] ¡Estamos en el grupo!`  

`[OTHERS] Es una amiga de mi madre que tenía que hacerte fenomenal que van a mandar agosto`  

`[OTHERS] En el grupo sentido`  

`[OTHERS] Es para mí`  

`[OTHERS] Que eso que he visto que en el grupo me encuentro`  

`[ME] Vale, sí`  

`[ME] ¿Qué tal has visto a César?`  

`[OTHERS] Aún no me entiende, que me he costado mucho`  

`[OTHERS] 🙏🏽🙏🏽🙏🏽🙏🏽🙏`  

`[ME] 👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼`  

`[ME] Pues entonces no te preocupen`  

`[ME] ¿En serio te has mandado?`  

`[ME] Porque mañana no sé cuánto, pero empezaron a entender que me había metido en el mundo`  

`[OTHERS] Siii`  

`[OTHERS] Te lo has hecho ya??`  

`[ME] Lo he hecho es por la mañana`  

`[ME] Pero puedes aprovechadrar a Ana han cambiado el caso y he estado en el grupo de secretaría, porque me puedo quejar`  

`[OTHERS] Me ha dicho que ha sido a mi cambio y también`

Como se ve, en función de los parámetros que se le pasen al modelo, se puede generar más o menos cantidad de texto, partiendo de un breve inicio. De primeras, el resultado es muy malo. Sin embargo, se pueden sacar algunas conclusiones:

1. El uso de signos de apertura en las interrogaciones (¿) y las exclamaciones (¡), que no son habituales en los chats informales y, sin embargo, yo los uso. Como se ve, siempre que [ME] pregunta o exclama, utiliza ambos signos, mientras que [OTHERS] no.
2. Lo mismo se puede decir del uso de las comas (,), mucho más abundante en los extractos correspondientes a [ME] que a [OTHERS].
3. ¿Por qué la conversación generada es tan caótica e inconexa? En el dataset pasado no había ninguna referencia temporal, por lo que se podía haber entendido como una sola conversación larguísima. Si hubiera puesto algún tipo de separador temporal, para delimitar mejor qué frases responden a qué frases, el modelo quizá hubiera aprendido la relación entre unas frases y las posibles contestaciones.
4. Las referencias a Misas y cervezas indican que el modelo ha comprendido perfectamente por dónde van los tiros de mi vida.

## Mini-chatbot

Para aprovechar un poco el modelo, he hecho un pequeño chatbot con un back en Flask y un front en Streamlit. Como no está desplegado, dejo las instrucciones para levantarlo en local:

1. Installar `requirements.py` para ambos componentes.
2. Descargar el [checkpoint](https://drive.google.com/file/d/1VOgUCg4dpr9AnlsLt5WiAZg52M9BXEPp/view?usp=sharing), descomprimirlo y meterlo en la carpeta **src/controllers**.
3. Back: ir a directorio **src** y ejecutar: `python run server.py`
4. Front: ir a directorio **streamlit** y ejecutar: `streamlit run home.py`

## Extras

Este repositorio contiene algunos extras:

- Carpeta **jupyter**: contiene un par de Jupyter Notebooks para el pre-procesado de los chats de whatsapp, con la manera para convertirlos en un dataframe anonimizado.
- Carpeta **models**: contiene varios jupyter-notebook en los que se ven mis distintos intentos de entrenar modelos.
    - Basic_classification: utiliza un modelo secuencial entrenado con un dataset parecido para poder predecir si un texto lo he escrito yo u otra persona.
    - Chatbot: el entrenamiento del chatbot descrito arriba.
    - Classification_with_more_features: un intento de hacer una red con más de un input, pero no llegó a buen puerto.
    - Sentiment-analyzer: una prueba de concepto con un par de librerías para análisis de sentimientos, llegando a la conclusión de que mis mensajes de whatsapp con bastante deprimentes.
